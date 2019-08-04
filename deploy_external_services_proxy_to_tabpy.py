import tabpy_client
client = tabpy_client.Client('http://127.0.0.1:9004')

def external_services_say_hello(message, service):
    import requests
    if service == 'PYTHON':
        r = requests.post('http://127.0.0.1:5000/python_says_hello', data = {
                                                                    'message': message})
    elif service == 'R':
        r = requests.post('http://127.0.0.1:6313/r_says_hello', data = {
                                                                    'message': message,})

    serviceResult = r.json()
    return serviceResult['result']

client.deploy('external_services_say_hello', external_services_say_hello, 'Make Python or R say Hello or anything you want.', override = True)
print('*** Model deployed successfully ***')
