import connexion
import six

from swagger_server.models.bid_event import BidEvent  # noqa: E501
from swagger_server.models.compensation_summary import CompensationSummary  # noqa: E501
from swagger_server.models.timeline_event import TimelineEvent  # noqa: E501
from swagger_server.models.volunteer import Volunteer  # noqa: E501
from swagger_server.models.volunteer_details import VolunteerDetails  # noqa: E501
from swagger_server import util


def get_simulation(limit=None, id=None):  # noqa: E501
    """Lists simulations with no id. With id it returns data for simulation

     # noqa: E501

    :param limit: max amount of recent simulations to retrieve
    :type limit: int
    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def options_simulation():  # noqa: E501
    """Shows simulation types and options

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def post_simulation():  # noqa: E501
    """Creates new simulation. Starts simulation if given id.

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def simulation_bids(id=None):  # noqa: E501
    """View bid history for a given simulation

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: List[BidEvent]
    """
    return 'do some magic!'


def simulation_compensation(id=None):  # noqa: E501
    """View all compensation for a given simulation

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: CompensationSummary
    """
    return 'do some magic!'


def simulation_passenger(id=None, passengerid=None):  # noqa: E501
    """View simulation details for a given passenger

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int
    :param passengerid: ID of passenger
    :type passengerid: int

    :rtype: VolunteerDetails
    """
    return 'do some magic!'


def simulation_summary(id=None):  # noqa: E501
    """Retrieve summary details for a specific simulation

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: object
    """
    return 'do some magic!'


def simulation_timeline(id=None):  # noqa: E501
    """View chronological list of events for a given simulation

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: List[TimelineEvent]
    """
    return 'do some magic!'


def simulation_volunteers(id=None):  # noqa: E501
    """View list of all volunteers for a given simulation

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: List[Volunteer]
    """
    return 'do some magic!'
