from socket import timeout
import sys
from flask_restx import Resource
from gevent import config
from pytz import timezone
from urllib3 import Retry
from models.shipment_details import api, check_status_and_insert_user_details, get_shipment_details_output, get_shipment_details_input
from dal.shipment_details import insert_user_details, select_all_records, check_duplicate_entry_by_tx_id, get_shipment_details_by_tx_id
from utilities.Jwt_auth import token_required, get_token_info
from bl.shipment_details_lookup_solscan import validate_burning_by_tx_id
import config
from flask import request
from utilities.cache import cache
import datetime
import base64


@api.route('/shipment_details')
class InsertShipmentDetails(Resource):
    # @api.expect(check_status_and_insert_user_details)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        """ Push Shipment Details to Database """
        args = check_status_and_insert_user_details.parse_args()
        AccessToken = request.headers["AccessToken"]
        TransactionId = args['TransactionId']
        AccessToken64bytes = base64.b64decode(AccessToken)
        if((TransactionId+config.buddiezSecretKey)!=AccessToken64bytes.decode()):
            return "Not Authorized"
        print(AccessToken64bytes+config.buddiezSecretKey)

        # status = validate_burning_by_tx_id(args['TransactionId'], args['cluster'])
        # breakpoint()
        # if status[0] != 200:
            # return status[0],status[1]
        Name = args['Name']
        EmailId = args['EmailId']
        address = args['Address']
        time_stamp = str(datetime.datetime.now(timezone("UTC")).strftime('&Y-%m-%d %H:%M:%S'))
        size = args['Size']
        check_duplicate_status = check_duplicate_entry_by_tx_id(args['TransactionId'])
        if check_duplicate_status[0] != 200:
            return check_duplicate_status[0],check_duplicate_status[1]
        res = insert_user_details((time_stamp,Name,address,EmailId,size,TransactionId))
        return res
            
    @api.marshal_with(get_shipment_details_output)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    @api.doc(security='apikey')
    @token_required
    def get(self):
        """ Get All Shipment Details From Database """
        res = select_all_records()
        print(res)
        return res
  

@api.route('/check_shipment_status_by_tx_id')
class CheckShipmentStatus(Resource):
    @api.expect(get_shipment_details_input)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        args = get_shipment_details_input.parse_args()
        get_status = get_shipment_details_by_tx_id(args['TransactionId'])
        if len(get_status) != 0:
            return (f"Your request has been submitted with details \n {get_status}")
        else:
            return (f"No orders. Please Contact the Administrator for further assistance")

@cache.cached(timeout=3600)
def testing(i):
    print('w/o cach')
    return i


@api.route('/test')
class test(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def get(self):
        for i in range(10):
            print(f'calling cache for {i}th time')
            testing(i)
        return 1
        
