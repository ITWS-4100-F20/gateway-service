import connexion
import six

from swagger_server.models.bid_event import BidEvent  # noqa: E501
from swagger_server.models.compensation_summary import CompensationSummary  # noqa: E501
from swagger_server.models.compensation_record import CompensationRecord
from swagger_server.models.timeline_event import TimelineEvent  # noqa: E501
from swagger_server.models.volunteer import Volunteer  # noqa: E501
from swagger_server.models.volunteer_details import VolunteerDetails  # noqa: E501
from swagger_server import util
from swagger_server.utils.database import client


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


def post_simulation(name, id=None):  # noqa: E501
    """Creates new simulation. Starts simulation if given id.

     # noqa: E501

    :param name: name of scenario
    :type name: str
    :param id: id of existing simulation
    :type id: str

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
    bids = []
    for bid in dict(client["simulation_data"]["Simulation-Volunteers"].find_one({"sim_id" : id},{"_id":False}))["vol_list"]:
        for b in bid["bid_history"]:
            bids.append(b)
    return [BidEvent.from_dict(b) for b in bids]


def simulation_compensation(id=None):  # noqa: E501
    """View all compensation for a given simulation

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: CompensationSummary
    """
    comps = []
    total = 0
    for vol in dict(client["simulation_data"]["Simulation-Volunteers"].find_one({"sim_id" : id},{"_id":False}))["vol_list"]:
        for comp in vol["compensation"]:
            comps.append(comp)
            total += comp["comp_amount"]
    return CompensationSummary.from_dict({"comp_list" : comps, "total_comp": total})
    


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
    return [TimelineEvent.from_dict(i) for i in dict(client["simulation_data"]["Simulation-Events"].find_one({"sim_id" : id},{"_id":False}))["event_list"]]


def simulation_volunteers(id=None):  # noqa: E501
    """View list of all volunteers for a given simulation

     # noqa: E501

    :param id: ID of simulation info you would like to retrieve
    :type id: int

    :rtype: List[Volunteer]
    """
    return [VolunteerDetails.from_dict(i) for i in dict(client["simulation_data"]["Simulation-Volunteers"].find_one({"sim_id" : id},{"_id":False}))["vol_list"]]
