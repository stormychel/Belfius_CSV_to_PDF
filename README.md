# Belfius CSV to PDF Converter

This script automatically converts CSV bank statements into a Belfius-style PDF format. 
It processes all CSV files in the current directory and generates matching PDFs with proper transaction formatting.

## Features

✅ Batch Processing – Automatically processes all .csv files in the folder.
✅ Professional Formatting – Matches Belfius bank statement layout.
✅ Auto-Naming – Output PDFs use the same name as the input CSV files.
✅ Monospaced & Aligned – Ensures correct column alignment for transactions.
✅ Multi-Page Support – Handles long transaction lists across multiple pages.
✅ File Reference in Header – Displays the original CSV filename at the top.
✅ Belfius Header (Commented Out) – Can be re-enabled for bank-style branding.

## Installation

**Clone the repository:**

``` bash
git clone https://github.com/stormychel/Belfius_CSV_to_PDF.git
cd Belfius_CSV_to_PDF
```

**Install dependencies:**

``` bash
pip install -r requirements.txt
```

## Usage

**Run the script in any directory containing CSV files:**

``` bash
python3 csv_to_pdf_formatter.py
```

It will automatically generate PDFs for all .csv files in the folder.

## Example

**Before:**

transactions_2024.csv  
transactions_2025.csv  

**After Running Script:**

transactions_2024.pdf  
transactions_2025.pdf  

## Contributing

Feel free to fork, improve, and submit PRs! Suggestions and enhancements are always welcome.
