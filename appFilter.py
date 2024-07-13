# from flask import jsonify
# from sqlalchemy.exc import SQLAlchemyError
# from datetime import datetime
# from dbModels import Pesalink, Card, Whizz, db

# def filter_transactions(transaction_date=None, transaction_status=None, channel=None):
#     try:
#         filtered_transactions = []

#         # Filtering Pesalink transactions
#         if transaction_date and transaction_status and channel:
#             pesalink_transactions = Pesalink.query.filter(
#                 Pesalink.transaction_date == transaction_date,
#                 Pesalink.status == transaction_status,
#                 Pesalink.channel == channel
#             ).all()
#         elif transaction_date and transaction_status:
#             pesalink_transactions = Pesalink.query.filter(
#                 Pesalink.transaction_date == transaction_date,
#                 Pesalink.status == transaction_status
#             ).all()
#         elif transaction_date and channel:
#             pesalink_transactions = Pesalink.query.filter(
#                 Pesalink.transaction_date == transaction_date,
#                 Pesalink.channel == channel
#             ).all()
#         elif transaction_status and channel:
#             pesalink_transactions = Pesalink.query.filter(
#                 Pesalink.status == transaction_status,
#                 Pesalink.channel == channel
#             ).all()
#         elif transaction_date:
#             pesalink_transactions = Pesalink.query.filter_by(
#                 transaction_date == transaction_date
#             ).all()
#         elif transaction_status:
#             pesalink_transactions = Pesalink.query.filter_by(
#                 transaction_status == transaction_status
#             ).all()
#         elif channel:
#             pesalink_transactions = Pesalink.query.filter_by(
#                 channel == channel
#             ).all()
#         else:
#             pesalink_transactions = Pesalink.query.all()

#         # Filtering Card transactions
#         # Similar logic can be applied for Card and Whizz models

#         for transaction in pesalink_transactions:
#             filtered_transactions.append({
#                 "transaction_id": transaction.end_to_end_id,
#                 "status": transaction.status,
#                 "transaction_time": transaction.transaction_time.strftime("%Y-%m-%d %H:%M:%S") if transaction.transaction_time else None,
#                 "channel": transaction.channel  # Assuming channel is an attribute in your model
#             })

#         return jsonify({"filtered_transactions": filtered_transactions})

#     except SQLAlchemyError as e:
#         return jsonify({"error": str(e)}), 500
