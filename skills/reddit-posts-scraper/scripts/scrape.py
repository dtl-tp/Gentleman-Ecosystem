import os
import json
import time
import sys
import argparse
from playwright.sync_api import sync_playwright

# Fix for Playwright on Windows environments where HOME might not be set
if "HOME" not in os.environ and "USERPROFILE" in os.environ:
    os.environ["HOME"] = os.environ["USERPROFILE"]

def get_top_post_urls(subreddit: str, count: int = 3) -> list:
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=all"
    urls = []
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/53.36"
            )
            page = context.new_page()
            
            print(f"[*] Navigating to r/{subreddit} top posts...")
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(3000)
            
            # Generic selectors for post links
            links = page.query_selector_all('a[href*="/comments/"]')
            
            for link in links:
                href = link.get_attribute("href")
                if href and "/comments/" in href:
                    if href.startswith("/"):
                        href = f"https://www.reddit.com{href}"
                    
                    href = href.split("?")[0]
                    # Filter out user profiles or other non-post comment links
                    if "/r/" + subreddit + "/comments/" in href.lower() and not href.endswith("/comments/"):
                        if href not in urls:
                            urls.append(href)
                            if len(urls) >= count:
                                break
            browser.close()
        except Exception as e:
            print(f"[!] Error finding post URLs: {e}")
            
    return urls

def extract_post_details(url: str, num_comments: int = 3) -> dict:
    """Extracts title, body, upvotes, and top comments from a Reddit post URL."""
    details = {
        "url": url,
        "title": "Unknown Title",
        "body": "",
        "upvotes": 0,
        "comments": []
    }
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/53.36"
            )
            page = context.new_page()
            
            page.goto(url, wait_until="networkidle")
            # Wait for content to render
            page.wait_for_timeout(4000)
            
            # Extract Title
            title_selectors = [
                'shreddit-post h1[slot="title"]',
                'h1[slot="title"]',
                'h1'
            ]
            for selector in title_selectors:
                elem = page.query_selector(selector)
                if elem:
                    text = elem.inner_text().strip()
                    if text:
                        details["title"] = text
                        break

            # Extract Upvotes
            post_elem = page.query_selector('shreddit-post')
            if post_elem:
                score = post_elem.get_attribute("score")
                if score:
                    try:
                        details["upvotes"] = int(score)
                    except:
                        pass
            
            # Extract Body Text
            body_selectors = [
                'shreddit-post-text-body div[slot="text-body"]',
                'div[data-click-id="text_body"]',
                '.RichTextJSON-root',
                'div[slot="text-body"]'
            ]
            for selector in body_selectors:
                elem = page.query_selector(selector)
                if elem:
                    text = elem.inner_text().strip()
                    if text:
                        details["body"] = text
                        break
            
            # Extract Top Comments
            comment_elems = page.query_selector_all('shreddit-comment')
            found_comments = 0
            for comment_elem in comment_elems:
                depth = comment_elem.get_attribute("depth")
                if depth == "0" or depth is None:
                    author = comment_elem.get_attribute("author") or "anonymous"
                    content_elem = comment_elem.query_selector('div[slot="comment"]')
                    if not content_elem:
                        content_elem = comment_elem.query_selector('.md')
                    
                    if content_elem:
                        content = content_elem.inner_text().strip()
                        if content:
                            details["comments"].append({
                                "author": author,
                                "text": content
                            })
                            found_comments += 1
                            if found_comments >= num_comments:
                                break
                            
            browser.close()
        except Exception as e:
            print(f"[!] Error extracting details for {url}: {e}")
            
    return details

def main():
    parser = argparse.ArgumentParser(description="Scrape top posts from a subreddit.")
    parser.add_argument("subreddit", help="Name of the subreddit (e.g., 'python')")
    parser.add_argument("--posts", type=int, default=3, help="Number of top posts to scrape")
    parser.add_argument("--comments", type=int, default=3, help="Number of top comments per post")
    parser.add_argument("--output", help="Output file path (JSON)")
    
    args = parser.parse_args()
    
    print(f"[*] Starting scrape for r/{args.subreddit} (Top {args.posts} posts)...")
    post_urls = get_top_post_urls(args.subreddit, args.posts)
    print(f"[*] Found {len(post_urls)} posts. Extracting details...")
    
    results = []
    for i, url in enumerate(post_urls, 1):
        print(f"[*] Post {i}/{len(post_urls)}: {url}")
        details = extract_post_details(url, args.comments)
        results.append(details)
        time.sleep(2)
    
    final_data = {
        "subreddit": args.subreddit,
        "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "posts": results
    }
    
    output_path = args.output
    if not output_path:
        output_path = f"{args.subreddit}_scrape.json"
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=4)
        
    print(f"[+] Scrape complete! Data saved to: {output_path}")

if __name__ == "__main__":
    main()
