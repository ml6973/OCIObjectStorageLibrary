import configuration.globalVars as globalVars
import requests
import json


def putObject(token_id, fileName, objectData):
    url = globalVars.chameleonObjectStorageURL + "/" + globalVars.chameleonContainerName + "/" + fileName

    my_headers = {"Content-Type": 'binary/octet-stream', "X-Auth-Token": token_id}

    r = requests.put(url, data=objectData, headers=my_headers)
    return r
