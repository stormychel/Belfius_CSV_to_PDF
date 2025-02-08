import pandas as pd
import sys
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib import colors

def format_transactions(csv_path):
    # Load the CSV file, skipping metadata rows
    df = pd.read_csv(csv_path, delimiter=';', skiprows=12, engine='python', dtype=str)
    
    # Rename columns to match expected format
    df.rename(columns={
        'Boekingsdatum': 'Date',
        'Valutadatum': 'Value Date',
        'Bedrag': 'Amount',
        'Mededelingen': 'Description'
    }, inplace=True)
    
    # Ensure only necessary columns are used
    df = df[['Date', 'Value Date', 'Amount', 'Description']]
    
    # Convert amount format (assuming it uses comma as decimal separator)
    df['Amount'] = df['Amount'].str.replace('.', '').str.replace(',', '.').astype(float)
    
    # Replace NaN values in Description with an empty string
    df['Description'] = df['Description'].fillna('')
    
    return df

def generate_pdf(transactions, output_pdf_path, original_filename):
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    width, height = A4
    
    # Commenting out the Belfius Header
    # c.setFont("Helvetica-Bold", 12)
    # c.drawString(50, height - 40, "Belfius Bank NV")
    # c.setFont("Helvetica", 10)
    # c.drawString(50, height - 60, "Karel Rogierplein 11 - 1210 Brussel")
    # c.drawString(50, height - 75, "IBAN: BE23 0529 0064 6991 - BIC: GKCCBEBB")
    # c.drawString(50, height - 90, "Verzekeringsagent FSMA nr. 019649  A - MEZ 4944")
    # c.line(50, height - 100, width - 50, height - 100)
    
    # Title and file reference
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 40, f"Original file: {original_filename}")
    
    # Column headers
    c.setFont("Helvetica-Bold", 10)
    y_position = height - 70
    c.drawString(50, y_position, "Nr")
    c.drawString(90, y_position, "Datum")
    c.drawString(170, y_position, "Val.")
    c.drawString(250, y_position, "Bedrag")
    c.drawString(350, y_position, "Omschrijving")
    c.line(50, y_position - 5, width - 50, y_position - 5)
    y_position -= 20
    
    c.setFont("Helvetica", 9)
    line_height = 12
    
    for index, row in transactions.iterrows():
        amount_str = f"{row['Amount']:,.2f}".replace(',', ' ')  # Ensure proper spacing
        c.drawString(50, y_position, f"{index+1:04d}")
        c.drawString(90, y_position, row['Date'])
        c.drawString(170, y_position, row['Value Date'])
        c.drawRightString(310, y_position, amount_str)
        
        description_lines = simpleSplit(row['Description'], "Helvetica", 9, 200)
        for desc in description_lines:
            c.drawString(350, y_position, desc)
            y_position -= line_height
        
        y_position -= line_height  # Extra space between transactions
        
        if y_position < 50:  # Create a new page if needed
            c.showPage()
            c.setFont("Helvetica", 9)
            y_position = height - 50
    
    c.save()

if __name__ == "__main__":
    # Get all CSV files in the current directory
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        sys.exit(1)
    
    for csv_file in csv_files:
        output_pdf_path = os.path.splitext(csv_file)[0] + ".pdf"  # Automatically name output file
        transactions = format_transactions(csv_file)
        generate_pdf(transactions, output_pdf_path, csv_file)
        print(f"PDF generated successfully: {output_pdf_path}")
