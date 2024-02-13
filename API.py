
import requests
url = 'https://reqres.in/api/users?page=2'

def test_api_get():
    resp = requests.get(url)
    assert (resp.status_code == 200), "Status code is not 200. Rather found:" +str(resp.status_code)
    print(resp.json())
    for record in resp.json()['data']:
        if record['id'] == 4:
           assert record['first name'] == 'Eve'


           assert record['last name'] == 'Holt'

def test_api_post():
    data = {'name': 'Simon', 'job':'QA'}
    resp = requests.post(url = 'https://reqres.in/api/users?page=2', data = data)
    data = resp.json()
    assert (resp.status_code == 201), "status code is not 201. Rather Found:" + str(resp.status_code)
    assert data['name'] =='Simon', "User created with wrong name. Expected : Simon , but found " + str(data['name'])
    assert data['job'] == 'QA' , "User created with wrong job. Expected: QA , but found :" + str(data['name'])