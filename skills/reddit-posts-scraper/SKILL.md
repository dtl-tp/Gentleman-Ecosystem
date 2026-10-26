---
name: reddit-posts-scraper
description: Scrapes the top N posts from any subreddit, including their title, body text, upvotes, and top comments. Use this to gather community sentiment, trending topics, or specific information from Reddit without an API key.
---
# Reddit Posts Scraper

## Goal
To extract structured data (JSON) from Reddit subreddits by scraping the "Top" posts of all time (or a specified timeframe) using Playwright.

## Instructions
1.  **Environment Setup**: Ensure `playwright` is installed in the Python environment. If not, run:
    ```bash
    pip install playwright
    python -m playwright install chromium
    ```
2.  **Define Subreddit**: Identify the target subreddit name (e.g., `n8n`, `python`, `technology`).
3.  **Execute Scraper**: Use the `run_command` tool to execute the scraping script:
    ```bash
    python scripts/scrape.py <subreddit_name> --posts 3 --comments 3 --output <output_path.json>
    ```
4.  **Parse Output**: The result will be a JSON file containing an array of posts with their metadata and comments.
5.  **Self-Correction**: If the script fails due to environment issues (e.g., `$HOME` not set on Windows), the script already includes a polyfill, but ensure the terminal has access to the user profile.

## Constraints
- Max 10 posts per scrape to avoid rate limiting.
- Headless mode is enabled by default to minimize resource usage.
- Scraped data is saved to a JSON file; do not output raw large text blocks to the terminal unless requested.
- Respect Reddit's terms—do not use this for aggressive crawling.

## Example Usage
- "Scrape the top 3 posts from r/n8n and tell me what people are saying about their new AI features."
- "Get the top 5 posts from r/python and summarize the most upvoted comments."
