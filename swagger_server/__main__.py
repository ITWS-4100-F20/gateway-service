import connexion
import os
import msal
from flask_cors import CORS
from flask_session import Session 
from swagger_server import encoder
from swagger_server import app_config

app=connexion.FlaskApp(
        __name__, 
        specification_dir='./swagger'
    )

flask_app = app.app
flask_app.config.from_object(app_config)
CORS(flask_app, resources={r"/*": {"origins": "*"}})
Session(flask_app)
app.add_api('swagger.yaml', strict_validation=True, options={ "swagger_ui_config": {"oauth2RedirectUrl": "http://localhost:3030/api/ui/oauth2-redirect.html"}} )
flask_app.json_encoder = encoder.JSONEncoder


if __name__ == '__main__':
    app.run(port=3030)