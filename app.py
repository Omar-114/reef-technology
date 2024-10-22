from flask import Flask, render_template
from api.reef_api import *
from dotenv import load_dotenv
import pdfkit

load_dotenv()
app = Flask(__name__)

retrieve_auth_token()

@app.route('/')
def home():
  data = retrieve_data()
  return render_template('employee_timesheet.html', **data)
  
if __name__ == "__main__":  
  app.run(debug=True)
  