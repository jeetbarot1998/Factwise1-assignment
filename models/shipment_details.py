from flask_restx import Namespace, reqparse, fields, inputs

api = Namespace('ShipmentDetails', description='User Shipment details')

# get_shipment_details_input = api.parser()
get_shipment_details_input = reqparse.RequestParser()
get_shipment_details_input.add_argument('TransactionId', type=str, default='string',location = 'form', required=True)

check_status_and_insert_user_details =  reqparse.RequestParser()
# check_status_and_insert_user_details.add_argument('burning_tx_id', type=str, default='string',location = 'form', required=True)
check_status_and_insert_user_details.add_argument('cluster', type=str, default='string',location = 'form', required=False)
check_status_and_insert_user_details.add_argument('Name', type=str, default='string',location = 'form', required=False)
check_status_and_insert_user_details.add_argument('Address', type=str, default='string',location = 'form', required=True)
check_status_and_insert_user_details.add_argument('EmailId', type=str, default='string',location = 'form', required=True)
check_status_and_insert_user_details.add_argument('Size', type=str, default='string',location = 'form', required=False)
check_status_and_insert_user_details.add_argument('TransactionId', type=str, default='string',location = 'form', required=True)

insert_shipment_details = api.model(
    'shipment_details', {
        'burning_tx_id' : fields.String(attribute='burning_tx_id'),
        'cluster' : fields.String(attribute='cluster'),
        'first_name': fields.String(attribute='first_name'),
        'last_name': fields.String(attribute='last_name'),
        'Address': fields.String(attribute='Address'),
        'ContactNumber': fields.String(attribute='ContactNumber')
    }
)

get_shipment_details_output = api.model(
    'get_shipment_details',{
        'ID': fields.Integer(attribute='ID'),
        'Name': fields.String(attribute='NAME'),
        'Address': fields.String(attribute='ADDRESS'),
        'EmailId': fields.String(attribute='EMAIL_ID'),
        'Size': fields.String(attribute='SIZE'),
        'TransactionId': fields.String(attribute='TX_ID'),
        'TimeStamp': fields.String(attribute='TIME_STAMP'),

    }
)
