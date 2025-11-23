![logo](https://github.com/tanishasethi27/SALES_GENIUS/commit/a0716b97e38149bf5b6e4fc7ba479ff5e91a4a73)
# Sales Genius: Persistent Sales and Apex Product Tracker

✨Overview of the Project✨

The Sales Genius is a robust, console-based Python application designed to address the challenges faced by small businesses relying on volatile, in-memory sales tracking. It provides a durable, user-friendly system for sales data management and basic financial analytics.
The application allows users to define their product catalog and record sales transactions persistently via CSV files (products.csv and sales.csv). Its core functionality is generating a report, which immediately identifies the top 5 revenue-generating and unit-selling products, providing actionable insights for inventory planning and decision-making. The project relies solely on the Python Standard Library, demonstrating proficiency in file handling, input validation, and data aggregation algorithms.

✨Features✨

The system is built on four core functional modules:
Persistent Data Storage (CSV): Automatically loads and saves all product and sales data to dedicated local CSV files, ensuring data integrity and survival across program sessions.
Product Management (CRUD): Allows users to define new products, including a unique ID, Name, and Price, forming a dynamic, user-defined product catalog.
Enhanced Sales Recording: Records new sales, performs input validation, and calculates the line_total revenue at the time of the transaction, ensuring accurate historical reporting even if prices change later.
Analytics & Apex Reporting: Aggregates all sales records to calculate the total units sold and total revenue for every product, then displays the Top 5 best-selling items ranked by quantity.

✨Technologies/Tools Used✨

Component           Technology                          Rationale
Language            Python 3.x                          Standard language for data processing and application development.
Persistence         CSV (Comma Separated Values)        Chosen for human-readability and accessibility, allowing end-users to view data in spreadsheet software.
Libraries           Python Standard Library             csv, os, uuid, and datetime. Reliance solely on the standard library minimizes dependencies and memory overhead (NFR5.0).
Data Structure      collections.defaultdict             Used for efficient, clean, and zero-initialization of data during the reporting/aggregation phase.

✨Steps to Install & Run the Project✨

The project is packaged in a single Python script, making deployment simple and fast.

1. Clone or Download: Obtain the product_tracker.py file.
2. Open Terminal/Command Prompt: Navigate to the directory where the file is saved.
3. Run the Script: Execute the following command:
python product_tracker.py
4. Automatic Setup: The application will automatically create the necessary data files (products.csv and sales.csv) in the same directory upon the first run, pre-populated with default technical product examples.

✨Instructions for Testing✨

A combination of manual and system testing is recommended to ensure all requirements are met:
1. Test Persistence (FR3.0):
 • Run the program, add a new product (Option 1), and record a sale (Option 2).
 • Verify that products.csv and sales.csv files have been created and contain the data.
 • Exit the program (Option 4), then run it again. Check the report (Option 3) to confirm the data was loaded correctly from the CSV files.

2. Test Input Validation & Data Integrity (FR1.1, NFR4.0):
  • Use Option 1 (Manage Products) and try to enter an existing Product ID; the system must prevent this.
  • Use Option 2 (Add a New Sales Record) and try entering non-numeric text (e.g., 'abc') for the Quantity or Price; the application must handle the error gracefully and prompt for valid input.

3. Test Revenue Calculation (FR2.0):
  • Record a sale for a known price and quantity (e.g., 5 units of a product priced at 100.00).
  • Run the report (Option 3) and check the "Total Revenue Processed" and the individual product's "Revenue" to ensure the calculation is correct (e.g., 500.00).

4. Test Top 5 Ranking (FR4.1):
  • Record sales to ensure Product A has the highest quantity sold, followed by Product B.
  • Check the report (Option 3) to confirm Product A is ranked #1 and Product B is ranked #2.
