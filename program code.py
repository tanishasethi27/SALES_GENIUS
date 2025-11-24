import datetime
import uuid
import os
import csv
from collections import defaultdict # Used for easier aggregation in reports

# --- 1. CONFIGURATION AND DATA STORAGE ---

# Filenames for persistent data storage using CSV format
PRODUCTS_FILE = 'products.csv'
SALES_FILE = 'sales.csv'

# Global variables (will be loaded from files)
PRODUCTS = {} # {id: {'name': name, 'price': price}}
SALES_RECORDS = [] # List of dictionaries