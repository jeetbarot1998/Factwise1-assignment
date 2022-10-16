import json
import sys
import traceback
import requests
from sqlalchemy import true
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


cluster_to_url_mapping = {
    'devnet':'https://api-devnet.solscan.io/transaction?tx=',
    'testnet': 'https://api-testnet.solscan.io/transaction?tx=',
    'mainnet': 'https://api.solscan.io/transaction??tx='
}
# 4H56SoxLHQL4oJrNdH1kXPfteR7pk1MduAHHZpXZXB8ss6H2M7QZtrdooHKyP7KAtNPwYdpSQvbk1UW7rLVUT4zz
def web_scraper(tx_id,cluster='devnet'):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = cluster_to_url_mapping[cluster]+tx_id
    try:
        print(f'Hitting url: "{url}"')
        transaction_details = requests.get(url=url,headers=headers)
        response = transaction_details.content.decode()
        response_dict = json.loads(response)
        for each_tx in response_dict['parsedInstruction']:
            if each_tx['type'] == 'burn':
                return True
        return False
    except Exception as err_msg:
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in web_scraper for mysql {text} on line {lineno} with error as {err_msg} ")
        return False

    
print(web_scraper('3BD86R72cFG5CkrZL1DcV8uiqMu4MzCNTPv1uF9BH3aDSA9XnemTMwCQLjxXhaENvCCHiQeEeHwBGRL5dWcqq6jh'))
print(web_scraper('4H56SoxLHQL4oJrNdH1kXPfteR7pk1MduAHHZpXZXB8ss6H2M7QZtrdooHKyP7KAtNPwYdpSQvbk1UW7rLVUT4zz'))





