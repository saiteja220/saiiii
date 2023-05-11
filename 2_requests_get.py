import requests

## If Credentials required
#res = requests.get('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('uname', 'password'))

## To get all customers details
res_obj = requests.get('http://127.0.0.1:5000/get')

print('\n response code is  :', res_obj.status_code)
print('\n CUST details are  :', res_obj.json())

assert res_obj.status_code == 200, ' Response status_code is not expected '
assert res_obj.json()['CUST-1'] == 'KUMAR', ' Customer name is not expected '



