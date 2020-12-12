# gateway-service

Communication layer for the United project

## Requirements

Python 3.7.9+

## Usage

Before you begin, you must fill in the variables in the swagger_server/app_config.py file.

To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:3030/api/ui/
```

Your Swagger definition lives here:

```
http://localhost:3030/api/openapi.json
```

To launch the integration tests, use tox:

``` bash
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .


```

Additional deployment information can be found at the root of this project. 