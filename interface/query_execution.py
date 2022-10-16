import logging
# from connections.mysql_connection import connection
import sqlparse
import traceback
import sys
from pymysql.cursors import DictCursor
from connections.mysql_connection import connection as mysql_connections

def sql_query_type(query_string):
    '''Get Query Type'''
    query_type = str(sqlparse.parse(query_string)[0].get_type()).upper()
    return query_type


def execute_query(query, query_params=None):
    logging.basicConfig(level=logging.INFO)
    try:
        query_type = sql_query_type(query_string=query)
        with mysql_connections()as con:
            conn = con.cursor()
            logging.info('Query Executed')
            if query_type == 'SELECT':
                conn.execute(query,query_params)
                records = conn.fetchall()
                columns = list(map(lambda x: x[0], conn.description))
                result_set = [dict(zip(columns, row)) for row in records]
                return result_set
            else:
                cursor = conn.execute(query,query_params)
                con.commit()
                return cursor
    except Exception as err_msg: 
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            logging.error(f"Error in creating connection object for mysql {text} on line {lineno} with error as {err_msg} ")
        return -1

