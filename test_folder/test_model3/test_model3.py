import os
from sre_constants import SUCCESS
from unittest import result
import requests
import json

# définition de l'adresse de l'API
api_address = '172.16.0.10'
# port de l'API
api_port = 5000

# requêtes pour alice v1 
r = requests.post(
    url='http://{address}:{port}/predict1'.format(address=api_address, port=api_port),
    headers= {
        'Authorization': 'alice=wonderland',
        'Content-Type': 'application/json'
        },
    json= {"MinTemp":18.0,"MaxTemp":22.4,"Rainfall":0.4,"Evaporation":5.180128166,"Sunshine":7.5983459299,"WindGustSpeed":38.3230212746,"WindSpeed9am":4.0,"WindSpeed3pm":9.0,"Humidity9am":87.0,"Humidity3pm":96.0,"Pressure9am":1018.2548732497,"Pressure3pm":1015.8020086033,"Cloud9am":8.0,"Cloud3pm":8.0,"Temp9am":18.8,"Temp3pm":18.8,"RainToday":0.0,"Year":2008.0,"Month":12.0,"Day":12.0,"Location_Adelaide":0.0,"Location_Brisbane":0.0,"Location_Canberra":0.0,"Location_GoldCoast":0.0,"Location_Melbourne":0.0,"Location_Newcastle":1.0,"Location_Perth":0.0,"Location_Sydney":0.0,"WindGustDir_E":0.0,"WindGustDir_ENE":0.0,"WindGustDir_ESE":0.0,"WindGustDir_N":0.0,"WindGustDir_NE":0.0,"WindGustDir_NNE":0.0,"WindGustDir_NNW":0.0,"WindGustDir_NW":0.0,"WindGustDir_S":0.0,"WindGustDir_SE":0.0,"WindGustDir_SSE":1.0,"WindGustDir_SSW":0.0,"WindGustDir_SW":0.0,"WindGustDir_W":0.0,"WindGustDir_WNW":0.0,"WindGustDir_WSW":0.0,"WindDir9am_E":0.0,"WindDir9am_ENE":0.0,"WindDir9am_ESE":0.0,"WindDir9am_N":0.0,"WindDir9am_NE":1.0,"WindDir9am_NNE":0.0,"WindDir9am_NNW":0.0,"WindDir9am_NW":0.0,"WindDir9am_S":0.0,"WindDir9am_SE":0.0,"WindDir9am_SSE":0.0,"WindDir9am_SSW":0.0,"WindDir9am_SW":0.0,"WindDir9am_W":0.0,"WindDir9am_WNW":0.0,"WindDir9am_WSW":0.0,"WindDir3pm_E":0.0,"WindDir3pm_ENE":0.0,"WindDir3pm_ESE":0.0,"WindDir3pm_N":0.0,"WindDir3pm_NE":1.0,"WindDir3pm_NNE":0.0,"WindDir3pm_NNW":0.0,"WindDir3pm_NW":0.0,"WindDir3pm_S":0.0,"WindDir3pm_SE":0.0,"WindDir3pm_SSE":0.0,"WindDir3pm_SSW":0.0,"WindDir3pm_SW":0.0,"WindDir3pm_W":0.0,"WindDir3pm_WNW":0.0,"WindDir3pm_WSW":0.0}
    )


output = '''
============================
       Model3 test
============================

request done at "/predict3"
| username="alice"
| password="wonderland"

expected result = Rain tomorrow
actual result = {test_result}

==> {test_status}

'''



data = r.text
status_code  = r.status_code

if  'prevue' in data :
    test_status = 'SUCCESS'
    test_result = 'Rain tomorrow'
else:
    test_status = 'FAILURE'
    test_result = 'No Rain tomorrow'

print(output.format(test_result=test_result, test_status=test_status))


r = requests.post(
    url='http://{address}:{port}/predict1'.format(address=api_address, port=api_port),
    headers= {
        'Authorization': 'bob=builder',
        'Content-Type': 'application/json'
        },
    json= {"MinTemp":18.0,"MaxTemp":22.4,"Rainfall":0.4,"Evaporation":5.180128166,"Sunshine":7.5983459299,"WindGustSpeed":38.3230212746,"WindSpeed9am":4.0,"WindSpeed3pm":9.0,"Humidity9am":87.0,"Humidity3pm":96.0,"Pressure9am":1018.2548732497,"Pressure3pm":1015.8020086033,"Cloud9am":8.0,"Cloud3pm":8.0,"Temp9am":18.8,"Temp3pm":18.8,"RainToday":0.0,"Year":2008.0,"Month":12.0,"Day":12.0,"Location_Adelaide":0.0,"Location_Brisbane":0.0,"Location_Canberra":0.0,"Location_GoldCoast":0.0,"Location_Melbourne":0.0,"Location_Newcastle":1.0,"Location_Perth":0.0,"Location_Sydney":0.0,"WindGustDir_E":0.0,"WindGustDir_ENE":0.0,"WindGustDir_ESE":0.0,"WindGustDir_N":0.0,"WindGustDir_NE":0.0,"WindGustDir_NNE":0.0,"WindGustDir_NNW":0.0,"WindGustDir_NW":0.0,"WindGustDir_S":0.0,"WindGustDir_SE":0.0,"WindGustDir_SSE":1.0,"WindGustDir_SSW":0.0,"WindGustDir_SW":0.0,"WindGustDir_W":0.0,"WindGustDir_WNW":0.0,"WindGustDir_WSW":0.0,"WindDir9am_E":0.0,"WindDir9am_ENE":0.0,"WindDir9am_ESE":0.0,"WindDir9am_N":0.0,"WindDir9am_NE":1.0,"WindDir9am_NNE":0.0,"WindDir9am_NNW":0.0,"WindDir9am_NW":0.0,"WindDir9am_S":0.0,"WindDir9am_SE":0.0,"WindDir9am_SSE":0.0,"WindDir9am_SSW":0.0,"WindDir9am_SW":0.0,"WindDir9am_W":0.0,"WindDir9am_WNW":0.0,"WindDir9am_WSW":0.0,"WindDir3pm_E":0.0,"WindDir3pm_ENE":0.0,"WindDir3pm_ESE":0.0,"WindDir3pm_N":0.0,"WindDir3pm_NE":1.0,"WindDir3pm_NNE":0.0,"WindDir3pm_NNW":0.0,"WindDir3pm_NW":0.0,"WindDir3pm_S":0.0,"WindDir3pm_SE":0.0,"WindDir3pm_SSE":0.0,"WindDir3pm_SSW":0.0,"WindDir3pm_SW":0.0,"WindDir3pm_W":0.0,"WindDir3pm_WNW":0.0,"WindDir3pm_WSW":0.0}
    )


output = '''
============================
       Model3 test
============================

request done at "/predict3"
| username="bob"
| password="builder"

expected result = Rain tomorrow
actual result = {test_result}

==> {test_status}

'''



data = r.text
status_code  = r.status_code

if  'prevue' in data :
    test_status = 'SUCCESS'
    test_result = 'Rain tomorrow'
else:
    test_status = 'FAILURE'
    test_result = 'No Rain tomorrow'

print(output.format(test_result=test_result, test_status=test_status))


r = requests.post(
    url='http://{address}:{port}/predict1'.format(address=api_address, port=api_port),
    headers= {
        'Authorization': 'clementine=mandarine',
        'Content-Type': 'application/json'
        },
    json= {"MinTemp":18.0,"MaxTemp":22.4,"Rainfall":0.4,"Evaporation":5.180128166,"Sunshine":7.5983459299,"WindGustSpeed":38.3230212746,"WindSpeed9am":4.0,"WindSpeed3pm":9.0,"Humidity9am":87.0,"Humidity3pm":96.0,"Pressure9am":1018.2548732497,"Pressure3pm":1015.8020086033,"Cloud9am":8.0,"Cloud3pm":8.0,"Temp9am":18.8,"Temp3pm":18.8,"RainToday":0.0,"Year":2008.0,"Month":12.0,"Day":12.0,"Location_Adelaide":0.0,"Location_Brisbane":0.0,"Location_Canberra":0.0,"Location_GoldCoast":0.0,"Location_Melbourne":0.0,"Location_Newcastle":1.0,"Location_Perth":0.0,"Location_Sydney":0.0,"WindGustDir_E":0.0,"WindGustDir_ENE":0.0,"WindGustDir_ESE":0.0,"WindGustDir_N":0.0,"WindGustDir_NE":0.0,"WindGustDir_NNE":0.0,"WindGustDir_NNW":0.0,"WindGustDir_NW":0.0,"WindGustDir_S":0.0,"WindGustDir_SE":0.0,"WindGustDir_SSE":1.0,"WindGustDir_SSW":0.0,"WindGustDir_SW":0.0,"WindGustDir_W":0.0,"WindGustDir_WNW":0.0,"WindGustDir_WSW":0.0,"WindDir9am_E":0.0,"WindDir9am_ENE":0.0,"WindDir9am_ESE":0.0,"WindDir9am_N":0.0,"WindDir9am_NE":1.0,"WindDir9am_NNE":0.0,"WindDir9am_NNW":0.0,"WindDir9am_NW":0.0,"WindDir9am_S":0.0,"WindDir9am_SE":0.0,"WindDir9am_SSE":0.0,"WindDir9am_SSW":0.0,"WindDir9am_SW":0.0,"WindDir9am_W":0.0,"WindDir9am_WNW":0.0,"WindDir9am_WSW":0.0,"WindDir3pm_E":0.0,"WindDir3pm_ENE":0.0,"WindDir3pm_ESE":0.0,"WindDir3pm_N":0.0,"WindDir3pm_NE":1.0,"WindDir3pm_NNE":0.0,"WindDir3pm_NNW":0.0,"WindDir3pm_NW":0.0,"WindDir3pm_S":0.0,"WindDir3pm_SE":0.0,"WindDir3pm_SSE":0.0,"WindDir3pm_SSW":0.0,"WindDir3pm_SW":0.0,"WindDir3pm_W":0.0,"WindDir3pm_WNW":0.0,"WindDir3pm_WSW":0.0}
    )


output = '''
============================
       Model1 test
============================

request done at "/predict3"
| username="clementine"
| password="mandarine"

expected result = Rain tomorrow
actual result = {test_result}

==> {test_status}

'''



data = r.text
status_code  = r.status_code

if  'prevue' in data :
    test_status = 'SUCCESS'
    test_result = 'Rain tomorrow'
else:
    test_status = 'FAILURE'
    test_result = 'No Rain tomorrow'

print(output.format(test_result=test_result, test_status=test_status))