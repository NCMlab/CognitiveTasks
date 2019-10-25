# https://digitalborn.org/get-survey-monkey-data-using-the-rest-api/
survey_id = 190091421
    
    
    
curl -i -X GET -H "Authorization:bearer -MMu4iKFM1vKiFeMgM7kpEVLeQQ8AqhD-BnE-3hBeNHrwupDZfsyE-sIZ9.cmyFKGnWrHHr0g0k2exW1BS.d0qzzCd.-Msqn9VqeVCN4RHkKGYaWC2QOYa1hvwQ9VXVh" -H "Content-Type": "application/json" https://api.surveymonkey.com/v3/surveys/190091421/responses/bulk


import requests
import json

client = requests.session()

headers = {
    "Authorization": "bearer %s" % "MMu4iKFM1vKiFeMgM7kpEVLeQQ8AqhD-BnE-3hBeNHrwupDZfsyE-sIZ9.cmyFKGnWrHHr0g0k2exW1BS.d0qzzCd.-Msqn9VqeVCN4RHkKGYaWC2QOYa1hvwQ9VXVh",
    "Content-Type": "application/json"
}

data = {}

HOST = "https://api.surveymonkey.net"
#SURVEY_LIST_ENDPOINT = "/v3/surveys/%s/responses/%s/details" %("85160626","161")
SURVEY_LIST_ENDPOINT = "/v3/surveys/190091421/responses"

uri = "%s%s" % (HOST, SURVEY_LIST_ENDPOINT)

response = client.get(uri, headers=headers, data=json.dumps(data))

response_json = response.json()
#survey_list = response_json["data"]["surveys"]

print(response_json)