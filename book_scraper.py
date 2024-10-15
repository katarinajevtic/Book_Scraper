import requests
from bs4 import BeautifulSoup
import pandas as pd


# Function to get page content
def get_page_content(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {url}, Error: {str(e)}")
        return None


# Function to scrape book data from the page
def scrape_books_from_page(soup):
    books = []
    if soup:
        all_books = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in all_books:
            item = {}
            item['Title'] = book.find('img').attrs['alt']
            item['Link'] = "https://books.toscrape.com/catalogue/" + book.find('a').attrs['href']
            item['Price'] = book.find('p', class_="price_color").text[2:]
            item['Stock'] = book.find('p', class_="instock availability").text.strip()
            rating = book.find('p', class_="star-rating")['class'][1]  # Extracting star rating
            item['Rating'] = rating
            books.append(item)
    return books


# Function to save data to CSV and Excel
def save_data_to_file(data, file_name_csv="books.csv", file_name_excel="books.xlsx"):
    """Saves the scraped data into both CSV and Excel formats."""
    df = pd.DataFrame(data)

    # Save to CSV and Excel directly in the current directory
    df.to_csv(file_name_csv, index=False)
    df.to_excel(file_name_excel, index=False)

    print(f"Data successfully saved to {file_name_csv} and {file_name_excel}")


# Main scraper function
def scrape_books(base_url, headers):
    current_page = 1
    all_data = []
    proceed = True

    while proceed:
        print(f"Currently scraping page {current_page}")
        url = f"{base_url}page-{current_page}.html"
        soup = get_page_content(url, headers)

        # If the page is not found, stop the scraping
        if soup is None or soup.title.text == "404 Not Found":
            print("No more pages to scrape, stopping.")
            proceed = False
        else:
            page_books = scrape_books_from_page(soup)
            if not page_books:
                print(f"No books found on page {current_page}, stopping.")
                proceed = False
            else:
                all_data.extend(page_books)

        current_page += 1

    return all_data


# Program entry point
if __name__ == "__main__":
    BASE_URL = "https://books.toscrape.com/catalogue/"

    # Headers to mimic a real browser request
    HEADERS = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0"),
        "Accept-Language": "en-US, en;q=0.5"
    }

    # Scrape the book data
    scraped_data = scrape_books(BASE_URL, HEADERS)

    # Save the data to files in the current directory
    if scraped_data:
        save_data_to_file(scraped_data)
    else:
        print("No data scraped, exiting.")
