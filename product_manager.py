# product_manager.py

from typing import Dict, Any

def manage_products(products: Dict[str, Dict[str, Any]]):
    """
    Allows user to add new products to the system.
    Note: products dictionary is passed by reference and modified directly.
    """
    print("\n--- MANAGE PRODUCTS ---")

    while True:
        product_id = input("Enter NEW Product ID (e.g., P006, max 5 chars, leave blank to return): ").strip().upper()
        if not product_id:
            print("[INFO] Returning to main menu.")
            return

        if len(product_id) > 5:
            print("[ERROR] Product ID must be 5 characters or less.")
        elif product_id in products:
            print(f"[ERROR] Product ID '{product_id}' already exists.")
        else:
            break

    product_name = input("Enter Product Name: ").strip()
    if not product_name:
        print("[ERROR] Product name cannot be empty.")
        input("Press Enter to continue...")
        return

    while True:
        try:
            price = float(input("Enter Price (e.g., 999.50): "))
            if price > 0:
                break
            else:
                print("[ERROR] Price must be greater than zero.")
        except ValueError:
            print("[ERROR] Invalid input. Please enter a valid number for price.")

    # Update the products dictionary
    products[product_id] = {'name': product_name, 'price': price}
    print(f"\n[SUCCESS] Product '{product_name}' (ID: {product_id}) added.")
    input("Press Enter to continue...")