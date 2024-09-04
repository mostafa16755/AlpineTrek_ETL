# AlpineTrek ETL Project
## Overview
This project is an ETL pipeline designed to utilize product data from the AlpineTrek website, specifically focusing on men's outdoor clothing. The tool scrapes data from multiple product pages, cleans the data, and stores it in both JSON format and an SQLite database. The project follows the ETL (Extract, Transform, Load) process to ensure the data is well-organized and ready for analysis.

## Project Structure
The project is organized into four main components:
Extract
Transform
Load
Main Script

<p>1. Extract</p> 
The extract.py module handles the data extraction process, which includes fetching HTML content from the AlpineTrek website and parsing it to extract relevant product information.
<ul>
<li>Fetching HTML: The fetch_html function uses the httpx library to make HTTP GET requests to the website. It returns the HTML content, which is then parsed using selectolax.</li>
<li>Fetching HTML: The fetch_html function uses the httpx library to make HTTP GET requests to the website. It returns the HTML content, which is then parsed using selectolax.</li>
<li>Parsing Search Pages: The parse_search_page function extracts product links from the search results pages, allowing the scraper to visit each product's detail page.<br>
<li>Parsing Detail Pages: The parse_detail_page function extracts detailed product information (like price, availability, and manufacturer) from each product's page. The data is extracted from structured data embedded in the HTML.</li>
</ul>

<p>2. Transform</p>
The transform.py module is responsible for cleaning and standardizing the raw data extracted from the website.
<ul><li>Cleaning Data: The clean_data function processes each product's data to ensure consistency. It trims whitespace, converts prices to floating-point numbers, standardizes currency and availability fields, and handles missing data gracefully.</li></ul>

<p>3. Load</p>
The load.py module deals with saving the cleaned data into different storage formats.
<ul>
<li>Saving to SQLite Database: The save_to_db function inserts the data into an SQLite database named products.db. It creates a table for storing product information and ensures data integrity by using SQL's INSERT OR REPLACE functionality.</li>
</ul>
<p>4. Main Script</p>
The main.py script orchestrates the entire ETL process.
<ul>
  <li>Main Function: The main function initializes the HTTP client, fetches and parses product pages, cleans the data, and finally saves the results in JSON and SQLite formats. It loops through all product pages, ensuring that data from multiple pages is collected and processed.</li>
</ul>
