# News Headlines Scraper

## Objective
Scrape top news headlines from a news website and save them into a `.txt` file.

## Tools Used
- Python
- requests
- BeautifulSoup4

## Features
- Fetches HTML content of a news website.
- Extracts headlines from `<h2>`, `<h3>`, or `<title>` tags.
- Saves all headlines in `headlines.txt` file.
- Handles HTTP request errors gracefully.

## How to Use
1. Install required packages:
   ```bash
   pip install requests beautifulsoup4
Run the script:

bash
Copy code
python news_scraper.py
Check the headlines.txt file for the scraped headlines.

Notes
The script is tested with BBC News.

Tag names might need adjustment for other websites.

yaml
Copy code

---

✅ **How it works:**
1. Fetch HTML with `requests`.  
2. Parse with `BeautifulSoup`.  
3. Extract headlines (`<h2>`, `<h3>` or `<title>`).  
4. Write to `headlines.txt`.
