from interface.query_execution import execute_query

def insert_user_details(params):
    Insert_query = """ INSERT INTO BUDDIEZZ_NFT
                        (TIME_STAMP, NAME, ADDRESS, EMAIL_ID, SIZE, TX_ID)
                        VALUES (%s, %s, %s, %s,  %s, %s) """
    # print('params=========================================',params)
    res = execute_query(query = Insert_query, query_params = params)
    if res != -1:
        return 'Success'
    else:
        return 'Insertion failed'

def check_duplicate_entry_by_tx_id(tx_id):
    select_query = """SELECT * FROM BUDDIEZZ_NFT WHERE TX_ID = (%s)"""
    res = execute_query(query = select_query,query_params = (tx_id,))
    if res != -1:
        if len(res) == 0:
            return 200, 'Success'
        else:
            return 401, 'You have already redeemed your nft'
    else:
        return 500, 'Select failed'

def get_shipment_details_by_tx_id(tx_id):
    select_query = """SELECT * FROM BUDDIEZZ_NFT WHERE TX_ID = (%s)"""
    res = execute_query(query = select_query,query_params = (tx_id,))
    return res


def select_all_records(params=None):
    select_query = """SELECT * FROM BUDDIEZZ_NFT"""
    res = execute_query(query = select_query)
    if res != -1:
        return res
    else:
        return 'Select failed'


def select_test():
    select_query = """SELECT * FROM BUDDIEZZ_NFT"""
    res = execute_query(query = select_query)
    print(res)
    if res != -1:
        return res
    else:
        return 'Select failed'


# def insert_test(params):
#     Insert_query = """ INSERT INTO BUDDIEZZ_NFT
#                         (TIME_STAMP, NAME, ADDRESS, EMAIL_ID, SIZE, TX_ID)
#                         VALUES (%s, %s, %s, %s,  %s, %s)"""
#     # print('params=========================================',params)
#     res = execute_query(query = Insert_query, query_params = params)
#     if res != -1:
#         return 'Success'
#     else:
#         return 'Insertion failed'

# data = ('21-05-2022 16:33 IST', 'USER NAME', 'User address', 'emailid@domain.com', 'XL', '4H56SoxLHQL4oJrNdH1kXPfteR7pk1MduAHHZpXZXB8ss6H2M7QZtrdooHKyP7KAtNPwYdpSQvbk1UW7rLVUT4zz')
# insert_test(data)
# select_test()

    
