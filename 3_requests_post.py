import requests

## To create new customer record
response = requests.post('http://127.0.0.1:5000/create', json={"CUST-3":"RRR"})

print('\n response code is :', response.status_code)
print('\n response DATA is :', response.json())

assert response.status_code == 200, 'Response status_code is not expected'
assert response.json()['CUST-3'] == 'RRR', ' Customer is not created '

