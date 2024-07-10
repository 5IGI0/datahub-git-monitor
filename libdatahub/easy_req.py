# if i can avoid adding dependencies (to `requests` in this case)
# i'll do it (i don't want to bother with pipenv)
import urllib.request
import json

from .config import DATAHUB_API_BASE, DATAHUB_API_KEY

def easy_req(endpoint:str, post_data:dict|None=None) -> dict:
    encoded_data = None

    if post_data is not None:
        encoded_data = json.dumps(post_data).encode('utf-8')
    
    request = urllib.request.Request(
        DATAHUB_API_BASE+endpoint,
        data=encoded_data,
        method='POST' if encoded_data is not None else 'GET')

    if DATAHUB_API_KEY:
        request.add_header('Authorization', 'Bearer '+str(DATAHUB_API_KEY))

    if encoded_data is not None:
        request.add_header('Content-Type', 'application/json')

    with urllib.request.urlopen(request) as response:
        response_data = json.loads(response.read())

    if response_data["success"] == False:
        raise ApiErrorException(response_data["error_code"], response_data["error_message"])

    return response_data["data"]