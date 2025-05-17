import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin, urlparse

visited = set()

def is_internal_link(link, base_url):
    parsed_link = urlparse(link)
    base_domain = urlparse(base_url).netloc
    return (parsed_link.netloc == "" or parsed_link.netloc == base_domain)

def get_full_url(base_url, link):
    return urljoin(base_url, link)

def scrape_page(url, base_url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "No Title"
        headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        images = [get_full_url(base_url, img['src']) for img in soup.find_all('img') if img.get('src')]
        links = [get_full_url(base_url, a['href']) for a in soup.find_all('a', href=True) if is_internal_link(a['href'], base_url)]

        return {
            "url": url,
            "title": title,
            "headings": "|".join(headings),
            "paragraphs": "|".join(paragraphs),
            "images": "|".join(images),
            "internal_links": links
        }

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def crawl(start_url, max_pages=10):
    pages_scraped = 0
    to_visit = [start_url]
    all_data = []

    while to_visit and pages_scraped < max_pages:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        page_data = scrape_page(current_url, start_url)
        if page_data:
            all_data.append(page_data)
            pages_scraped += 1
            for link in page_data["internal_links"]:
                if link not in visited:
                    to_visit.append(link)
            time.sleep(1)  # Be polite with delays

    return all_data

def save_to_csv(data, filename="scraped_output.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["url", "title", "headings", "paragraphs", "images"])
        writer.writeheader()
        for row in data:
            writer.writerow({
                "url": row["url"],
                "title": row["title"],
                "headings": row["headings"],
                "paragraphs": row["paragraphs"],
                "images": row["images"]
            })


user_url = input("Enter the website URL (e.g., https://www.shadowfox.in/): ").strip()
max_pages = input("Enter number of pages to scrape (default 10): ").strip()
max_pages = int(max_pages) if max_pages.isdigit() else 10
scraped_data = crawl(user_url, max_pages=max_pages)
save_to_csv(scraped_data)
print(f"\n✅ Scraping complete! Data saved to 'scraped_output.csv'.")
