# data_persistence.py

import os
import csv
from typing import Dict, List, Any

PRODUCTS_FILE = 'data/products.csv'
SALES_FILE = 'data/sales.csv'

def initialize_data_directory():
    """Ensures the 'data' directory exists."""
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"[INFO] Created directory: {data_dir}")

def load_data(products: Dict[str, Dict[str, Any]], sales_records: List[Dict[str, Any]]):
    """
    Loads PRODUCTS and SALES_RECORDS from CSV files into the provided dictionaries/lists.
    If files don't exist, it initializes default data.
    """
    initialize_data_directory() # Ensure the data folder is ready

    # 1. Load Products
    try:
        if os.path.exists(PRODUCTS_FILE):
            with open(PRODUCTS_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products[row['id']] = {
                        'name': row['name'],
                        'price': float(row['price'])
                    }
            print(f"[INFO] Loaded {len(products)} products from {PRODUCTS_FILE}.")
        else:
            # Default technical product list (as updated previously)
            products.update({
                'T001': {'name': 'High-Speed USB-C Hub', 'price': 49.99},
                'T002': {'name': '1TB NVMe SSD', 'price': 129.50},
                'T003': {'name': '4K LED Monitor (27 inch)', 'price': 399.99},
                'T004': {'name': 'Wireless Ergonomic Mouse', 'price': 25.00},
                'T005': {'name': 'Noise Cancelling Headphones', 'price': 189.95}
            })
            save_data(products, sales_records) # Save defaults immediately
            print(f"[INFO] {PRODUCTS_FILE} not found. Starting with default product list and saving.")
    except Exception as e:
        print(f"[ERROR] Could not load products from CSV: {e}")
        products.clear() # Clear products if loading fails critically

    # 2. Load Sales Records
    try:
        if os.path.exists(SALES_FILE):
            with open(SALES_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert necessary fields back to numeric types
                    row['quantity'] = int(row['quantity'])
                    row['price'] = float(row['price'])
                    row['line_total'] = float(row['line_total'])
                    sales_records.append(row)
            print(f"[INFO] Loaded {len(sales_records)} sales records from {SALES_FILE}.")
        else:
            print(f"[INFO] {SALES_FILE} not found. Starting with empty sales records.")
    except Exception as e:
        print(f"[ERROR] Could not load sales records from CSV: {e}")
        sales_records.clear()

def save_data(products: Dict[str, Dict[str, Any]], sales_records: List[Dict[str, Any]]):
    """Saves current PRODUCTS and SALES_RECORDS to CSV files."""

    # 1. Save Products
    try:
        product_fieldnames = ['id', 'name', 'price']
        with open(PRODUCTS_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=product_fieldnames)
            writer.writeheader()
            for pid, data in products.items():
                writer.writerow({
                    'id': pid,
                    'name': data['name'],
                    'price': f"{data['price']:.2f}"
                })
    except Exception as e:
        print(f"[CRITICAL ERROR] Failed to save products to CSV: {e}")

    # 2. Save Sales Records
    try:
        sales_fieldnames = ['sale_id', 'product_id', 'quantity', 'price', 'line_total', 'date']
        with open(SALES_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=sales_fieldnames)
            writer.writeheader()
            writer.writerows(sales_records)
    except Exception as e:
        print(f"[CRITICAL ERROR] Failed to save sales records to CSV: {e}")