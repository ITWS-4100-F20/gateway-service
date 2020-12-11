import connexion
import six
from sklearn.neural_network import MLPClassifier
from swagger_server import util
from swagger_server.utils.database import client
import json
import pymongo
import numpy
import pickle
import requests
from swagger_server import app_config
new_client = pymongo.MongoClient(app_config.MONGO_CONNECTION_STRING)

from swagger_server.models.model_definition import ModelDefinition  # noqa: E501
def flatten(data:list):
    res = []
    for row in data:
        rowdata = {}
        for point in row["fields"]:
            rowdata[point["field"]] = point["value"]
            if point["datatype"] == "int":
                rowdata[point["field"]] = int(point["value"])
            elif point["datatype"] == "float":
                rowdata[point["field"]] = float(point["value"])
            elif point["datatype"] == "bool":
                rowdata[point["field"]] = bool(point["value"])
        res.append(rowdata)
    return res


def delete_model():  # noqa: E501
    """Deletes model of id

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'

def define_model(body):  # noqa: E501
    """Creates new model definition

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ModelDefinition.from_dict(connexion.request.get_json())  # noqa: E501

    proxyResponse = requests.post(app_config.ANALYTICS_ENGINE_ENDPOINT+"/simulation", json=connexion.request.get_json())
    #may need to modify this response based on return type

    ret = proxyResponse.json()
    return ret 


def get_model():  # noqa: E501
    """gets model of id

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def options_model():  # noqa: E501
    """Gets all models

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def post_model():  # noqa: E501
    """Adds new version of model of id

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def create_model(body, id, name, prediction, schema_id, version):  # noqa: E501
    """Adds new version of model of id

     # noqa: E501


    :rtype: None
    """
    '''
    print(id)
    print(name)
    print(prediction)
    print(schema_id)
    print(version)'''
    tmp = new_client["simulation_data"]
    tmpcol = tmp["model"]
    #X = [[0., 0.], [1., 1.]]
    #y = [0, 1]
    model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    #model.fit(X, y)
    data_model = pickle.dumps(model)
    #print(data_model)
    mydict = {"id": id, "name": name, "prediction": prediction, "schema_id": schema_id, "version": version, "model": data_model}
    x = tmpcol.insert_one(mydict)
    print("MODEL IS INSERTED")
    return 'do some magic!'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def train_model(body, model_id, collection_name):  # noqa: E501
    """
    SHOULD TRY INCLUDING SOMETHING LIKE TRANING MODEL NAME SO THAT WHEN THE NEURAL NET MODEL IS STORED IT WILL BE EASIER TO FIND
    When training yu look at the schema associated wit hthe model (model_name) look at the database for the collection with that name. Pull all the data from that collection and train with it. Will have to look at the schema's datatypes and cut out non-numeric/convert non numerics. Also use predicted as the 'y' value

    For train take the existing model, train it, and store it as the next version of the model (a new object in the database)
    """
    #print("The model id is:",model_id)
    #print("The collection name for the data is:",collection_name)
    db = new_client["simulation_data"]
    collection = db[collection_name].find().sort("_id")
    model_db = db["model"]
    my_model = model_db.find({"id": model_id})
    version = 0
    for f in model_db.find({},{"id": model_id,"prediction":1,"version":1}):
        if f["version"] > version:
            version = f["version"]
            predict_title = f["prediction"]
    flatten_collection = flatten(collection)

    x = []
    y = []
    prediction = {}
    prediction_value = 0
    for col in flatten_collection:
        #print(col[predict_title])
        x_value = []
        for i in col:
            if i == predict_title:
                if is_number(col[i]) == False:
                    if col[i] not in prediction:
                        prediction[col[i]] = prediction_value
                        prediction_value += 1
                    y.append(prediction[col[i]])
                else:
                    y.append(float(col[i]))
            else:
                x_value.append(float(col[i]))

        x.append(x_value)
    y = numpy.array(y)
    x = numpy.array(x)
    print(x.shape)
    y = y.reshape(-1,1)
    print(y.shape)
    for z in my_model:
        model = pickle.loads(z["model"])
        model.fit(x,y)
        version = z["version"] + 1

        data_model = pickle.dumps(model)
        mydict = {"id": z["id"], "name": z["name"], "prediction": predict_title, "schema_id": z["schema_id"], "version": version, "model": data_model}
        new_model_insert = model_db.insert_one(mydict)
    return 'Training is done'


def predict_model(body, model_name, schema_id):
    #Ther is something in scikit learn that can just return the probabilities. RETURN JUST THAT
    print("The model name is:",model_name)
    print("The schema_id is:",schema_id)
    db = new_client["simulation_data"]
    prediction_title = ""
    model_db = db["model"]
    #my_model = model_db.find({"name": model_name})
    version = 0
    for f in model_db.find({},{"name": model_name,"prediction":1,"version":1}):
        if f["version"] > version:
            version = f["version"]
            prediction_title = f["prediction"]
    my_model = model_db.find({"version": version})
    #print(prediction)
    for x in my_model:
        model = pickle.loads(x['model'])

    collection = db[schema_id].find().sort("_id")
    flatten_collection = flatten(collection)
    x = []
    for col in flatten_collection:
        #print(col[predict_title])
        x_value = []
        for i in col:
            if i == prediction_title:
                continue
            else:
                x_value.append(float(col[i]))
        x.append(x_value)

    x = numpy.array(x)
    #print(x.shape)



    pred_val = model.predict_proba(x)
    result = pred_val.tolist()
    resulting_set = set()
    for l in result:
        for item in l:
            resulting_set.add(item)
    return json.dumps(list(resulting_set))

    '''
    tmp = new_client["simulation_data"]
    tmpcol = tmp["model"]
    my_model = tmpcol.find({"id": schema_id})
    for x in my_model:
        model = pickle.loads(x['model'])
    prediction = model.predict([[2., 2.], [-1., -2.]])
    print("PREDICTION:",prediction)
    '''
    return 'do some magic!'
    


def put_model():  # noqa: E501
    """Adds new model

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


'''
Use this link to access the API: http://localhost:3030/api/ui/#/Data
Everytime you open the page or refresh it you must hit the authorize button and enter: 
05d3667c-b1d5-4b17-861e-f589b8c0e468
'''