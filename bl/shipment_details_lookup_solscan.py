import json
from multiprocessing import context
import sys
import traceback
import requests
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cluster_to_url_mapping = {
    'devnet':'https://api-devnet.solscan.io/transaction?tx=',
    'testnet': 'https://api-testnet.solscan.io/transaction?tx=',
    'mainnet': 'https://api.solscan.io/transaction??tx='
}
cluster_to_url_mapping_for_address = {
    'devnet': 'https://api-devnet.solscan.io/account?address=',
    'mainnet': 'https://api.solscan.io/account?address=',
}


# address_to_nfts_type_mapping{
#     # Address to symbol mapping
#     '6XhoCkFsGjZ65hqSgj1FXuWau7SujBtZ6L3CsqeP23oL': 'Test Cap'
# }
# 5TgDEnm9hA8MQx5wz9D65syAozW9354BUfG9cgLGo74DA1crgavH9Yy8epn3pNbFx5kkyNriV94Zi2hzcV85PJPH
# 4H56SoxLHQL4oJrNdH1kXPfteR7pk1MduAHHZpXZXB8ss6H2M7QZtrdooHKyP7KAtNPwYdpSQvbk1UW7rLVUT4zz
token_program = 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'
def validate_burning_by_tx_id(tx_id,cluster='devnet'):
    if cluster not in cluster_to_url_mapping.keys():
        cluster = 'devnet'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        url = cluster_to_url_mapping[cluster]+tx_id
        print(f'Hitting url: "{url}"')
        transaction_details = requests.get(url=url,headers=headers, verify=False)
        response = transaction_details.content.decode()
        response_dict = json.loads(response)
        print(response_dict)
        for each_tx in response_dict['parsedInstruction']:
            if each_tx['type'] == 'burn' and each_tx['programId'] == token_program:
                # mint_address_verify = each_tx['params']['mint']
                # url_for_address = cluster_to_url_mapping_for_address['devnet'] + str(mint_address_verify)
                # token_details = requests.get(url=url_for_address,headers=headers, verify=False)
                # print(token_details)
                return 200, 'Success'
        return 401, 'Please burn the correct token'
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in web_scraper for mysql {text} on line {lineno} with error as {err_msg} ")
        return 500, 'Error in fetching values'

    
# print(validate_burning_by_tx_id('5TgDEnm9hA8MQx5wz9D65syAozW9354BUfG9cgLGo74DA1crgavH9Yy8epn3pNbFx5kkyNriV94Zi2hzcV85PJPH'))
# print(validate_burning_by_tx_id('4H56SoxLHQL4oJrNdH1kXPfteR7pk1MduAHHZpXZXB8ss6H2M7QZtrdooHKyP7KAtNPwYdpSQvbk1UW7rLVUT4zz'))





