from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from dbModels import Pesalink, Card, Whizz


def total_status_count():
    try:
        total_count = Pesalink.query.count()
        return jsonify({"total_status_count": total_count})
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to fetch the count of successful ('ACCP') and failed ('RJCT
def status_counts():
    try:
        total_count = Pesalink.query.count()
        successful_count = Pesalink.query.filter_by(status='ACCP').count()
        failed_count = Pesalink.query.filter_by(status='RJCT').count()

        successful_percentage = round((successful_count / total_count) * 100) if total_count > 0 else 0
        failed_percentage = round((failed_count / total_count) * 100) if total_count > 0 else 0
        response = jsonify({
            "successful_count": successful_count,
            "successful_percentage": f"{successful_percentage}",
            "failed_count": failed_count,
            "failed_percentage": f"{failed_percentage}"
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


def status_counts_powercard():
    try:
        total_count = Card.query.count()
        successful_count = Card.query.filter_by(p_action='Approved').count()
        failed_count = total_count - successful_count

        successful_percentage = round((successful_count / total_count) * 100) if total_count > 0 else 0
        failed_percentage = round((failed_count / total_count) * 100) if total_count > 0 else 0
        response = jsonify({
            "successful_count": successful_count,
            "successful_percentage": f"{successful_percentage}",
            "failed_count": failed_count,
            "failed_percentage": f"{failed_percentage}"
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


def status_counts_whizz():
    try:
        total_count = Whizz.query.count()
        successful_count = Whizz.query.filter_by(recipient_status='SUCCESS').count()
        failed_count = total_count - successful_count

        successful_percentage = round((successful_count / total_count) * 100) if total_count > 0 else 0
        failed_percentage = round((failed_count / total_count) * 100) if total_count > 0 else 0
        response = jsonify({
            "successful_count": successful_count,
            "successful_percentage": f"{successful_percentage}",
            "failed_count": failed_count,
            "failed_percentage": f"{failed_percentage}"
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

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
            

#           for transaction in pesalink_transactions:
#             filtered_transactions.append({
#                 "transaction_id": transaction.end_to_end_id,
#                 "status": transaction.status,
#                 "transaction_time": transaction.transaction_time.strftime("%Y-%m-%d %H:%M:%S") if transaction.transaction_time else None,
#                 "channel": transaction.channel  # Assuming channel is an attribute in your model
#             })

#         return jsonify({"filtered_transactions": filtered_transactions})

#     except SQLAlchemyError as e:
#         return jsonify({"error": str(e)}), 500