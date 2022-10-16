import gevent.monkey

gevent.monkey.patch_all()

from flask import Flask
from flask_restx import Api
import os
from utilities.cache import cache  
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

##############Import service###############
from services.Service_jwt_auth import api as token_jwt
from services.Service_shipment_details import api as admin_panel
from services.Service_user import api as user_module
from services.Service_team import api as team_module
from services.Service_project import api as project_module

flask_app = Flask(__name__)
CORS(flask_app)

# ================================= HEROKU DB START ==================================
# FOR LOCAL HOST DB
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ucmdkokipuljyi:3911ddbd4da67f64a3cf80355b0bf7a1cb2221337a43e32c83851f49eeffcfba@ec2-3-226-211-228.compute-1.amazonaws.com:5432/ddvlni5bs2bil6'
# FOR STAGE DB
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flask_app)
flask_app.db = db
# ================================= HEROKU DB END ==================================

# ================================= API CACHE START ==================================
# cache = Cache()
CACHE_CONFIG = {'CACHE_TYPE' : 'simple',
                'CACHE_DEFAULT_TIMEOUT' : 600}
cache.init_app(flask_app, CACHE_CONFIG)
# ================================= API CACHE START ==================================

# ==================================== JWT START =====================================
AUTH = {
    'apikey' :{
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'Authorization'
    }
}
API = Api(flask_app, authorizations= AUTH)
# ================================= JWT END ==========================================

############Append Namespace##############
API.add_namespace(token_jwt)
API.add_namespace(admin_panel)
API.add_namespace(user_module)
API.add_namespace(team_module)
API.add_namespace(project_module)

if __name__ == '__main__':
    flask_app.run(port=8080,debug=True)