# sales_analytics.py

import datetime
import uuid
from collections import defaultdict
from typing import Dict, List, Any

def display_products(products: Dict[str, Dict[str, Any]]):
    """Helper function to display available products."""
    print("--------------------------------------------------")
    print(f"| {'ID':<5} | {'Product Name':<30} | {'Price':<8} |")
    print("--------------------------------------------------")
    for pid, data in products.items():
        print(f"| {pid:<5} | {data['name']:<30} | {data['price']:<8.2f} |")
    print("--------------------------------------------------")


def add_new_sale(products: Dict[str, Dict[str, Any]], sales_records: List[Dict[str, Any]]):
    """
    Records a new sale, calculates line total, and updates the sales_records list.
    """
    print("\n--- NEW SALE ENTRY ---")

    if not products:
        print("[ERROR] No products defined. Please add a product first via the 'Manage Products' menu.")
        input("Press Enter to continue...")
        return

    display_products(products)

    # Input validation for Product ID
    while True:
        product_id = input("Enter Product ID to sell: ").strip().upper()
        if product_id in products:
            break
        else:
            print(f"[ERROR] Product ID '{product_id}' not found. Please try again.")

    # Input validation for Quantity
    while True:
        try:
            quantity = int(input("Enter Quantity Sold: "))
            if quantity > 0:
                break
            else:
                print("[ERROR] Quantity must be a positive integer.")
        except ValueError:
            print("[ERROR] Invalid input. Please enter a whole number for quantity.")

    # Calculate line total
    price = products[product_id]['price']
    line_total = price * quantity

    # Record the sale
    new_sale = {
        'sale_id': str(uuid.uuid4()),
        'product_id': product_id,
        'quantity': quantity,
        'price': price, # Store price at time of sale
        'line_total': line_total,
        'date': datetime.date.today().strftime('%Y-%m-%d')
    }
    sales_records.append(new_sale)

    print("\n[SUCCESS] Sale recorded!")
    print(f"  Product: {products[product_id]['name']} | Quantity: {quantity} | Revenue: {line_total:,.2f}")
    input("\nPress Enter to continue...")


def generate_most_sold_report(products: Dict[str, Dict[str, Any]], sales_records: List[Dict[str, Any]]):
    """
    Analyzes sales records to determine total quantity sold and revenue for each product,
    then displays the top 5 most-sold products by quantity.
    """
    print("\n--- MOST-SOLD PRODUCTS REPORT ---")

    if not sales_records:
        print("[REPORT] No sales data available yet. Please add some sales first.")
        input("\nPress Enter to continue...")
        return

    # 1. Aggregate Sales Data
    product_stats = defaultdict(lambda: {'total_quantity': 0, 'total_revenue': 0.0})
    total_system_revenue = 0.0

    for sale in sales_records:
        pid = sale['product_id']
        quantity = sale['quantity']
        line_total = sale['line_total']
        total_system_revenue += line_total

        product_stats[pid]['total_quantity'] += quantity
        product_stats[pid]['total_revenue'] += line_total

    # 2. Sort Data (Top 5 Report logic)
    sorted_products = []
    for pid, stats in product_stats.items():
        sorted_products.append((stats['total_quantity'], pid, stats['total_revenue']))

    sorted_products.sort(key=lambda x: x[0], reverse=True) # Sort by quantity

    # 3. Display the Report
    top_n = 5
    print(f"\nTotal Revenue Processed: {total_system_revenue:,.2f}")
    print("\nTop 5 Products by Units Sold:")
    print("-----------------------------------------------------------------------")
    print(f"| {'Rank':<4} | {'Product Name':<25} | {'Units Sold':<10} | {'Revenue':<12} |")
    print("-----------------------------------------------------------------------")

    for i, (total_units, pid, total_revenue) in enumerate(sorted_products[:top_n]):
        product_name = products.get(pid, {}).get('name', f'UNKNOWN ({pid})')

        print(f"| {i + 1:<4} | {product_name:<25} | {total_units:<10} | {total_revenue:<12,.2f} |")

    print("-----------------------------------------------------------------------")
    print(f"[REPORT] Total unique sales transactions processed: {len(sales_records)}")
    input("\nPress Enter to continue...")