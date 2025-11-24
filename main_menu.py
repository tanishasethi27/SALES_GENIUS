# main.py

from typing import Dict, List, Any
import os

# Import modules
from data_persistence import load_data, save_data
from product_manager import manage_products
from sales_analytics import add_new_sale, generate_most_sold_report

# Global data containers (will be populated by load_data)
PRODUCTS: Dict[str, Dict[str, Any]] = {}
SALES_RECORDS: List[Dict[str, Any]] = []

# --- MAIN CONTROL LOOP (Presentation Tier) ---

def main_menu():
    """
    The main control loop for the application, handling user input and navigation.
    Initializes data and saves data upon exit.
    """
    # Load persistent data at startup
    load_data(PRODUCTS, SALES_RECORDS)

    while True:
        # Clear/refresh console for cleaner output (basic usability feature)
        # Note: This won't truly clear the screen in all environments, but it helps.
        # You can also use 'cls' for Windows: os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 50)

        print("===================================================")
        print("  VITyarthi Product Sales Tracker ")
        print("  Developed by: Tanisha Sethi 25BAI11491  ")
        print("===================================================")
        print("1. Manage Products (Add New Products)")
        print("2. Add a New Sales Record (Data Entry)")
        print("3. Generate Top Products Report (Analytics)")
        print("4. Exit Application")
        print("---------------------------------------------------")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            manage_products(PRODUCTS)
            save_data(PRODUCTS, SALES_RECORDS) # Save products after creation
        elif choice == '2':
            add_new_sale(PRODUCTS, SALES_RECORDS)
            # Sales are saved inside the add_new_sale function for immediate persistence
        elif choice == '3':
            generate_most_sold_report(PRODUCTS, SALES_RECORDS)
        elif choice == '4':
            # Final save is handled robustly throughout, but we can ensure a final save here
            save_data(PRODUCTS, SALES_RECORDS)
            print("\nThank you for using the Sales Genius. All data has been saved.")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    # The __init__.py file is just an empty file to make 'src' a package
    # but the interpreter needs to be run from the root directory to find 'src/main.py'
    # and for relative file paths like 'data/products.csv' to work.
    main_menu()