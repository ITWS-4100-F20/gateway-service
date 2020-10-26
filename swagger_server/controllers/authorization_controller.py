from typing import List
from ..utils import auth
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_OAuth2(token):
    decoded = auth.tokenInfo(token)
    #fix naming difference in JWT
    decoded['scope'] = decoded['scp']
    return decoded

def validate_scope_OAuth2(required_scopes, token_scopes):
    return set(required_scopes).issubset(token_scopes.split())


