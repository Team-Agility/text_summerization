import requests
import json

ENDPOINT= 'https://fdkjp120qd.execute-api.ap-southeast-1.amazonaws.com/dev/'
MEETING_IDS = ['ES2002a', 'ES2003a', 'ES2004a', 'ES2005a']
DATASET_DIR = 'dataset'

for meeting_id in MEETING_IDS:
    req = requests.post(ENDPOINT, json = {
            "operation": "get",
            "meeting_id": meeting_id,
            "sk": "confidence"
        })
    confidents = {}
    for conf in req.json()['data']['data']:
        confidents[int(conf['sk'].replace('confidence_', ''))] = conf['data']
     
    with open(f'{DATASET_DIR}/{meeting_id}/confidence.json', 'w') as f:
        json.dump(confidents, f, indent=4)