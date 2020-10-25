import connexion
import os
import msal
from flask_session import Session 
from swagger_server import encoder
from swagger_server import config

def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache

def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        app_config.CLIENT_ID, authority=authority or app_config.AUTHORITY,
        client_credential=app_config.CLIENT_SECRET, token_cache=cache)

def _build_auth_url(authority=None, scopes=None, state=None):
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri=url_for("authorized", _external=True))

def _get_token_from_cache(scope=None):
    cache = _load_cache()  # This web app maintains one cache per session
    cca = _build_msal_app(cache=cache)
    accounts = cca.get_accounts()
    if accounts:  # So all account(s) belong to the current signed-in user
        result = cca.acquire_token_silent(scope, account=accounts[0])
        _save_cache(cache)
        return result

def main():
    app=connexion.FlaskApp(
        __name__, 
        specification_dir='./swagger'
    )
    app.add_api('swagger.yaml', strict_validation=True)
    flask_app = app.app
    flask_app.config.from_object(config)
    Session(flask_app)
    flask_app.json_encoder = encoder.JSONEncoder
    app.run(port=3030)

if __name__ == '__main__':
    main()