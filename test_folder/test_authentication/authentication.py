import os
import requests

# définition de l'adresse de l'API
api_address = '172.16.0.10'
# port de l'API
api_port = 5000


r = requests.get(
    url='http://{address}:{port}/Authorization'.format(address=api_address, port=api_port),
    headers= {
        'Authorization': 'alice=wonderland'
        }
)

output = '''
============================
    Authentication test
============================

request done at "/Authorization"
| username="alice"
| password="wonderland"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))



# requête bob
r = requests.get(
    url='http://{address}:{port}/Authorization'.format(address=api_address, port=api_port),
     headers= {
        'Authorization': 'bob=builder'
        }
)

output = '''
============================
    Authentication test
============================

request done at "/Authorization"
| username="bob"
| password="builder"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))



r = requests.get(
    url='http://{address}:{port}/Authorization'.format(address=api_address, port=api_port),
     headers= {
        'Authorization': 'clementine=mandarine'
        }
)

output = '''
============================
    Authentication test
============================

request done at "/Authorization"
| username="clementine"
| password="mandarine"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))
