import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util
from ..utils import auth

def get_users():  # noqa: E501
    """gets currently authenticated user

    Retrieves information about the current user from the microsoft Graph API # noqa: E501


    :rtype: None
    """
    authHeader = connexion.request.headers.get('authorization')
    return auth.tokenInfo(authHeader.split()[1])