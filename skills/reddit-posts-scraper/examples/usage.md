# Example: Scraping r/n8n

### Request
"Scrape the top 3 posts from r/n8n and save them to n8n_data.json."

### Process
1.  Agent identifies the `reddit-posts-scraper` skill.
2.  Agent runs the command:
    ```bash
    python C:/Users/danif/.gemini/antigravity/skills/reddit-posts-scraper/scripts/scrape.py n8n --posts 3 --comments 3 --output d:/SKILLs creator/output/reddit/n8n_data.json
    ```
3.  Agent reads the generated JSON file to summarize the findings.

### Result Output (Abbreviated)
```json
{
    "subreddit": "n8n",
    "scraped_at": "2026-02-22 16:30:00",
    "posts": [
        {
            "url": "https://www.reddit.com/r/n8n/comments/1jy1wdc/i_made_an_n8n_cheat_sheet/",
            "title": "I made an n8n Cheat Sheet!",
            "body": "",
            "upvotes": 2046,
            "comments": [
                {
                    "author": "MttGhn",
                    "text": "Bravo for this work. How to get it in good quality?"
                }
            ]
        }
    ]
}
```
