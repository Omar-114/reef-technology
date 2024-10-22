import os
import sys
import pdfkit
from flask import Flask, render_template
from datetime import datetime
# Add the directory containing app.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')  # Adjust the path as necessary

from app import app, retrieve_data

def generate_pdf():
  with app.app_context():
    data = retrieve_data() 
    rendered = render_template('employee_timesheet.html', **data)  # Render the HTML template
    
    # Convert HTML to PDF
    pdf = pdfkit.from_string(rendered, False)

    # Get the current date for the filename
    current_date = datetime.now().strftime("%Y-%m-%d")
    pdf_file_path = os.path.join(os.getcwd(), f'employee_timesheet_{current_date}.pdf')  # Updated filename

    with open(pdf_file_path, 'wb') as f:
      f.write(pdf)

if __name__ == "__main__":
  generate_pdf()
