# -*- encoding: utf-8 -*-

import json
import ovh
import sys

with open("secrets.json") as fin:
    secrets = json.loads(fin.read())

serviceName = secrets['ovhSslGatewayService']['name']
id = secrets['ovhSslGatewayService']['id']

client = ovh.Client(
    endpoint='ovh-eu',
    application_key=secrets['ovhApiKey']['applicationKey'],
    application_secret=secrets['ovhApiKey']['applicationSecret'],
    consumer_key=secrets['ovhApiKey']['consumerKey'],
)

# print("Welcome", client.get('/me')['firstname'])

def get_ip():
    """
    {
        "port": 80,
        "state": "ok",
        "address": "83.99.56.222",
        "id": 43941
    }
    """ 
    return client.get('/sslGateway/{}/server/{}'.format(serviceName, id))

def set_ip(new_ip):
    # Change IP adress of ssl-gateway
    return client.put('/sslGateway/{}/server/{}'.format(serviceName, id, new_ip), 
        address=new_ip,
        port=80,
    )

print("Current status")
server_check = get_ip()
print(json.dumps(server_check, indent=4))

if len(sys.argv) == 2:
    new_ip = sys.argv[1]
    if len(sys.argv[1].split(".")) == 4:
        
        if server_check["address"] == new_ip:
            print("New IP identical to old. No change required.")
        else:
            print("New IP set:", new_ip)
            result = set_ip(new_ip)
            print(json.dumps(result, indent=4))
    elif sys.argv[1] == "test":
        # Try setting current adress
        set_ip(server_check["address"])
    else:
        print("Incorrect IP given: ", new_ip)
