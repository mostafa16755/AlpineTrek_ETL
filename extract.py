import json
import httpx
from selectolax.parser import HTMLParser
from typing import Optional, List, Generator

def fetch_html(client: httpx.Client, url: str) -> Optional[HTMLParser]:
    try:
        res = client.get(url)
        res.raise_for_status()
        return HTMLParser(res.text)
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {url}: {e}")
        return None

def parse_search_page(html: Optional[HTMLParser]) -> List[str]:
    if html is None:
        return []
    return [link.attributes["href"] for link in html.css('li a.product-link')]

def parse_detail_page(html: Optional[HTMLParser]) -> Generator[dict, None, None]:
    if html is None:
        return
    element_list = html.css("script[type='application/ld+json']")
    for data in element_list:
        try:
            json_data = json.loads(data.text())
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")
            continue
        if isinstance(json_data, list):
            for item in json_data:
                if "offers" in item:
                    yield item
        elif "offers" in json_data:
            yield json_data

def parse_pagination(html: Optional[HTMLParser]) -> int:
    if html is None:
        return 1
    page_block = html.css("div[data-codecept='pagination']")
    if page_block:
        total_pages = page_block[0].css("a")[-1].text()
        try:
            return int(total_pages)
        except ValueError:
            print(f"Unable to convert total pages to int: {total_pages}")
            return 1
    return 1
