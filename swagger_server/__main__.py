import connexion
import os
import msal
from flask_session import Session 
from swagger_server import encoder
from swagger_server import config

app=connexion.FlaskApp(
        __name__, 
        specification_dir='./swagger'
    )

# @app.route("/login")
# def login():
#     session["state"] = str(uuid.uuid4())
#     # Technically we could use empty list [] as scopes to do just sign in,
#     # here we choose to also collect end user consent upfront
#     auth_url = _build_auth_url(scopes=config.SCOPE, state=session["state"])
#     return render_template("login.html", auth_url=auth_url, version=msal.__version__)

# @app.route(config.REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
# def authorized():
#     if request.args.get('state') != session.get("state"):
#         return redirect(url_for("index"))  # No-OP. Goes back to Index page
#     if "error" in request.args:  # Authentication/Authorization failure
#         return render_template("auth_error.html", result=request.args)
#     if request.args.get('code'):
#         cache = _load_cache()
#         result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
#             request.args['code'],
#             scopes=config.SCOPE,  # Misspelled scope would cause an HTTP 400 error here
#             redirect_uri=url_for("authorized", _external=True))
#         if "error" in result:
#             return render_template("auth_error.html", result=result)
#         session["user"] = result.get("id_token_claims")
#         _save_cache(cache)
#     return redirect(url_for("index"))

# @app.route("/logout")
# def logout():
#     session.clear()  # Wipe out user and its token cache from session
#     return redirect(  # Also logout from your tenant's web session
#         config.AUTHORITY + "/oauth2/v2.0/logout" +
#         "?post_logout_redirect_uri=" + url_for("index", _external=True))

# @app.route("/graphcall")
# def graphcall():
#     token = _get_token_from_cache(config.SCOPE)
#     if not token:
#         return redirect(url_for("login"))
#     graph_data = requests.get(  # Use token to call downstream service
#         config.ENDPOINT,
#         headers={'Authorization': 'Bearer ' + token['access_token']},
#         ).json()
#     return render_template('display.html', result=graph_data)

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
        config.CLIENT_ID, authority=authority or config.AUTHORITY,
        client_credential=config.CLIENT_SECRET, token_cache=cache)

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

flask_app = app.app
flask_app.config.from_object(config)
Session(flask_app)
app.add_api('swagger.yaml', strict_validation=True, options={ "swagger_ui_config": {"oauth2RedirectUrl": "http://localhost:3030/api/ui/oauth2-redirect.html"}} )
flask_app.json_encoder = encoder.JSONEncoder

if __name__ == '__main__':
    app.run(port=3030)