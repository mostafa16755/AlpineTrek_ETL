from typing import Dict

def clean_data(item: Dict) -> Dict:
    try:
        cleaned_item = {
            'identifier': item.get('identifier', '').strip(),
            'parentIdentifier': item.get('parentIdentifier', '').strip(),
            'name': item.get('name', '').strip(),
            'sku': item.get('sku', '').strip(),
            'image': item.get('image', '').strip(),
            'url': item.get('url', '').strip(),
            'price': float(item.get('offers_price', 0)) if item.get('offers_price') else 0.0,
            'currency': item.get('offers_priceCurrency', 'GBP').strip().upper(),
            'availability': item.get('offers_availability', '').split('/')[-1].lower() if '/' in item.get('offers_availability', '') else item.get('offers_availability', '').lower(),
            'condition': item.get('offers_itemCondition', '').split('/')[-1].lower() if '/' in item.get('offers_itemCondition', '') else item.get('offers_itemCondition', '').lower(),
            'manufacturer': item.get('manufacturer_name', '').strip(),
            'color': item.get('color', '').strip(),
            'gtin13': item.get('gtin13', '').strip(),
        }
    except ValueError as e:
        print(f"Error while cleaning data: {e}")
        cleaned_item = {}
    
    return cleaned_item