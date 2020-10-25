import connexion
import six

from swagger_server import util


def ping_server():  # noqa: E501
    """Check if system is up and running

    Pings the server to check for a healthy response # noqa: E501


    :rtype: None
    """
    return {"message":"Active!"}, 200
