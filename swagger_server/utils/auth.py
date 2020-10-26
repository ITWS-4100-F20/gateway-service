import jwt
import requests
import base64
from swagger_server import app_config
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def tokenInfo(token):
    return jwt.decode(token, verify=False)