import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

whizztransactions_file_path='Whizz Transactions 08072024.csv'
powercard_file_path = 'Powercard Transactions 08072024.csv'
pesalink_file_path='Pesalink Transactions 08072024.csv'
def main():
    # Creating connection to db
    db_conn = psycopg2.connect(
        host='localhost',
        dbname='postgres',
        user='postgres',
        password='cozlin',
        port='5432'
    )

     # Store csv data into dataframe
    whizztransactions_df=pd.read_csv(whizztransactions_file_path)
 
    
    
    powercard_df = pd.read_csv(powercard_file_path)
    powercard_df['Local time'] = pd.to_datetime(powercard_df['Local time'], format='%m/%d/%Y %H:%M').dt.strftime('%Y-%m-%d %H:%M:%S')
    powercard_df['Internal time'] = pd.to_datetime(powercard_df['Internal time'], format='%m/%d/%Y %H:%M').dt.strftime('%Y-%m-%d %H:%M:%S')
    
    pesalink_df=pd.read_csv(pesalink_file_path)

    i_powercard_query = """
    INSERT INTO public.powercard (
        external_stan, reference, p_source, p_destination, message, processing_code, p_action, pan, local_time, internal_time, transaction_amount, terminal_no, acceptor_point, authorization_reference, current_table_indicator
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    i_whizztransactions_query = """
    INSERT INTO public.whizztransactions (
        transaction_date, customer_ref, profits_ref, phone_number, recipient, transaction_type, amount, recipient_status, status_description, extra
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    i_pesalink_query="""
    INSERT INTO public.pesalink ( 
    End_To_End_ID, Status, Amount, narration, debtor_bank_Code, debtor_bank_name, creditor_bank_code, creditor_bank_name, transaction_time, debtor_acct, debtor_name, creditor_acct, creditor_name, failure_code , transfer_type
     )VALUES(%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
     """
    db_cursor = db_conn.cursor()
    insert_df(db_cursor, powercard_df, i_powercard_query)
    insert_df(db_cursor, whizztransactions_df, i_whizztransactions_query)
    insert_df(db_cursor, pesalink_df, i_pesalink_query)
    db_conn.commit()
    db_cursor.close()
    db_conn.close()

def insert_df(cursor, df,query):
    try:
        rows= [tuple(row) for row in df.itertuples(index=False)]
    
        cursor.executemany(query, rows)

        #commit the transaction
        print("Data inserted successfully.")
    except Exception as e:
        #conn.rollback()
        print("Error: ", e)

          #close connection 
main()





