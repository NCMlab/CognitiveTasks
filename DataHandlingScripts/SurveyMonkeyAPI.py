from client import Client
# If you do not have access_token, run
CLIENT_ID = 'D_kzOb9fSo2zC64qMNt7Xg'
CLIENT_SECRET = '32248023616401215046166317729204720865'
REDIRECT_URI = 'https://www.surveymonkey.com'
cl = client.Client(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, access_token=None)
# If you have access_token, run
survey_id = 190091421
client=Client(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, access_token=ACCESS_TOKEN)
    
    
    
curl -i -X GET -H "Authorization:bearer -MMu4iKFM1vKiFeMgM7kpEVLeQQ8AqhD-BnE-3hBeNHrwupDZfsyE-sIZ9.cmyFKGnWrHHr0g0k2exW1BS.d0qzzCd.-Msqn9VqeVCN4RHkKGYaWC2QOYa1hvwQ9VXVh" -H "Content-Type": "application/json" https://api.surveymonkey.com/v3/surveys/190091421/responses/bulk