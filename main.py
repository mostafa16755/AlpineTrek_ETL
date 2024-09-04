import httpx
from extract import fetch_html, parse_search_page, parse_detail_page, parse_pagination
from transform import clean_data
from load import save_to_json, save_to_db

def main():
    base_url = 'https://www.alpinetrek.co.uk/outdoor-clothing/for--men/'
    client = httpx.Client()
    
    # Fetch the first page and determine the total number of pages
    first_page_html = fetch_html(client, base_url)
    total_pages = parse_pagination(first_page_html)
    
    all_items = []
    
    for page_num in range(1, total_pages + 1):
        page_url = f"{base_url}{page_num}/"
        html = fetch_html(client, page_url)
        print(f"Page Number {page_num} from {total_pages} Pages")
        
        # Parse the product links on the current page
        product_links = parse_search_page(html)
        
        for link in product_links:
            # Fetch and parse detail page
            detail_html = fetch_html(client, link)
            items = list(parse_detail_page(detail_html))
            
            # Clean data
            cleaned_items = [clean_data(item) for item in items]
            all_items.extend(cleaned_items)
    
    # Save results
    save_to_json(all_items)
    save_to_db(all_items)

if __name__ == '__main__':
    main()