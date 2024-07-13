from app import app
from appCore import *


@app.route('/total_status_count', methods=['GET'])
def get_total_status_count():
    return total_status_count()

@app.route('/pesalink-status-count', methods=['GET'])
def get_status_counts():
    return status_counts()

@app.route('/powercard-status-count', methods=['GET'])
def get_status_counts_powercard():
    return status_counts_powercard()

@app.route('/whizztransactions-status-count', methods=['GET'])
def get_status_counts_whizz():
    return status_counts_whizz()

# @app.route('/filter', methods=['POST'])
# def filter_transactions():
#     return filter_transactions

