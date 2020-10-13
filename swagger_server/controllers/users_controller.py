import connexion
import six

from swagger_server.models.create_user import CreateUser  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(user=None):  # noqa: E501
    """create a user

    Creates new user in the system with given information # noqa: E501

    :param user: user to create
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = CreateUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(user=None):  # noqa: E501
    """delete a user

    deletes an existing user # noqa: E501

    :param user: user to remove
    :type user: dict | bytes

    :rtype: Success
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_user(user=None):  # noqa: E501
    """edit a user

    Modifies user information # noqa: E501

    :param user: user to create
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = CreateUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_users(filterBy=None):  # noqa: E501
    """get list of users

    Retrieves a list of all current users in the system including information about them # noqa: E501

    :param filterBy: optional argument to filter by regular users or agents
    :type filterBy: str

    :rtype: List[User]
    """
    return 'do some magic!'
