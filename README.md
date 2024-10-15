# Book Scraper
A Python-based web scraper that extracts book data from the [Books to Scrape](https://books.toscrape.com) website. The scraper retrieves details such as the title, price, stock availability, rating, and link to each book, and saves the data into CSV and Excel files.

## Features
+ Scrapes multiple pages of book data from the site.
+ Extracts book titles, prices, stock status, ratings, and links.
+ Saves the scraped data into both CSV and Excel formats.
+ Error handling for failed requests or unavailable pages (404 errors).How to Use
## How to Use:
1. Clone the repository:
```
  git clone https://github.com/your-username/book-scraper.git
  cd book-scraper
```
2. Run the scraper script:
```
python scraper.py
```
This will scrape the book data from [Books to Scrape](https://books.toscrape.com) and save the output to books.csv and books.xlsx in the current directory.

## Script Breakdown 
+ `get_page_content(url, headers)`
 Fetches the HTML content of a given URL using `requests` and parses it with `BeautifulSoup`.

+ `scrape_books_from_page(soup)`
Extracts book data (title, price, stock status, rating, and link) from the parsed HTML of a single page.

+ `save_data_to_file(data, file_name_csv, file_name_excel)`
Saves the scraped book data into both CSV and Excel formats.

+ `scrape_books(base_url, headers)`
Iterates through multiple pages of the website, scraping data from each until there are no more pages to scrape.

## Example Output
After running the script, you'll find two files in the current directory:
+ `books.csv`: Contains the scraped book data in CSV format.
+ `books.xlsx`: Contains the scraped book data in Excel format.
## Notes
The script uses custom headers to mimic a real browser request and avoid potential blocking.
The scraper stops automatically when it encounters a 404 error or an empty page.
## License
This project is licensed under the MIT License. See the [LICENCE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for more details.
  
