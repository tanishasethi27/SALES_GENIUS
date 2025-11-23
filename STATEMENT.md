![logo](https://github.com/tanishasethi27/SALES_GENIUS/blob/main/VITYARTHI%20PROJECT.png)
# Problem Statement
The challenge remains for small businesses to track high-demand items, but the solution must be practical and persistent. The initial problem of relying on manual or volatile tracking systems is compounded by the need to capture financial metrics (like revenue) alongside unit sales. An effective solution requires data persistence and the flexibility to define the business's unique product catalog.

# Scope of the Project
The scope is expanded to create a robust, console-based application in Python that features persistent, user-defined data storage using the CSV (Comma Separated Values) file format. This choice of persistence provides a human-readable and accessible ledger system.

# In Scope:
1. Persistent Data Storage (CSV): Loading and saving PRODUCTS and SALES_RECORDS to dedicated CSV files.
2. Product Definition (CRUD): Allowing the user to add new products with Name, ID, and Price.
3. Enhanced Data Capture: Recording the price at the time of sale and calculating the line-item total revenue.
4. Advanced Reporting: Aggregating total units sold and total revenue to display the top 5 products by unit quantity (The Apex ranking).
5. File I/O Error Handling.

# Out of Scope (Future Enhancements):
1. Deleting or editing existing sales records (full CRUD for sales).
2. Filtering reports by date range or specific product.
3. Integrating a GUI or web interface.
4. Tracking real-time inventory levels.

# Target Users

The primary target users are:

1. Small Business Owners/Entrepreneurs: Requiring a durable, zero-cost solution to monitor sales and revenue across sessions, with data accessible in a standard spreadsheet format (CSV).
2. Retail Store Managers: Needing persistent records to analyze long-term trends and inform reordering decisions.
3. Python Students: To demonstrate proficiency in file handling (csv, os), error management, and complex data aggregation.

# High-level Features

1. Data Persistence Module (CSV): Handles automatic loading and saving of all data to local CSV files using csv.DictWriter and csv.DictReader.
2. Product Management Module: Allows users to define their product catalog (ID, Name, Price) which forms the basis of all future sales.
3. Sales Recording Module: Captures transaction details, including calculating line-item revenue.
4. Analytics & Reporting Module: Generates a ranked Top 5 list based on units sold, prominently featuring total revenue for the system and for each top product (The Apex Report).
