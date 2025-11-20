# news_scraper.py

import requests
from bs4 import BeautifulSoup

# URL of the news website (example: BBC)
url = "https://www.bbc.com/news"

try:
    # Fetch the HTML content
    response = requests.get(url)
    response.raise_for_status()  # check for request errors
    html_content = response.text

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find headline tags (common example: <h3> for BBC)
    headlines = soup.find_all(["h3", "h2", "title"])  

    # Extract text and remove duplicates
    headline_texts = list({headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)})

    # Save headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for idx, headline in enumerate(headline_texts, 1):
            file.write(f"{idx}. {headline}\n")

    print(f"Scraped {len(headline_texts)} headlines successfully! Check 'headlines.txt'.")
    
except requests.exceptions.RequestException as e:
    print("Error fetching the website:", e)
