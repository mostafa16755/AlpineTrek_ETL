import sqlite3
import json
from typing import List, Dict

def save_to_json(results: List[Dict]):
    try:
        with open("results.json", "w") as f:
            json.dump(results, f, indent=4)
    except IOError as e:
        print(f"An error occurred while saving results to JSON: {e}")

def save_to_db(results: List[Dict]):
    try:
        with sqlite3.connect('products.db') as conn:
            c = conn.cursor()
            
            # Create table if it doesn't exist
            c.execute('''
            CREATE TABLE IF NOT EXISTS products (
                identifier TEXT PRIMARY KEY,
                parentIdentifier TEXT,
                name TEXT,
                sku TEXT,
                image TEXT,
                url TEXT,
                price REAL,
                currency TEXT,
                availability TEXT,
                condition TEXT,
                manufacturer TEXT,
                color TEXT,
                gtin13 TEXT
            )
            ''')

            # # Create table for additional properties if needed
            # c.execute('''
            # CREATE TABLE IF NOT EXISTS additional_properties (
            #     identifier TEXT,
            #     property_name TEXT,
            #     property_value TEXT,
            #     FOREIGN KEY (identifier) REFERENCES products (identifier)
            # )
            # ''')

            # Insert data into products table
            for item in results:
                c.execute('''
                INSERT OR REPLACE INTO products 
                (identifier, parentIdentifier, name, sku, image, url, price, currency, availability, condition, 
                manufacturer, color, gtin13)
                VALUES 
                (:identifier, :parentIdentifier, :name, :sku, :image, :url, :price, :currency, :availability, :condition, 
                :manufacturer, :color, :gtin13)
                ''', item)
                
                # # Insert additional properties
                # for key, value in item.items():
                #     if key.startswith('additionalProperty_'):
                #         index = key.split('_')[2]
                #         prop_name = item.get(f'additionalProperty_{index}_name', '')
                #         prop_value = item.get(f'additionalProperty_{index}_value', '')
                #         c.execute('''
                #         INSERT INTO additional_properties (identifier, property_name, property_value)
                #         VALUES (?, ?, ?)
                #         ''', (item['identifier'], prop_name, prop_value))

            conn.commit()
    except sqlite3.DatabaseError as e:
        print(f"An error occurred while saving results to the database: {e}")
