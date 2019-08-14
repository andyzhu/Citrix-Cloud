import json
import requests


def readClient_ID():
    with open('azStudio_client') as clientid_file:
        data = json.load(clientid_file)
        return data['Client_Id']


def readClient_Secret():
    with open('azStudio_client') as clientid_file:
        data = json.load(clientid_file)
        return data['Client_Secret']


def getBearerToken():

    api_url_base = 'https://trust.citrixworkspacesapi.net/andzhudev/tokens/clients'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}

    # payload = {'clientId':'9d2aaf66-9d2d-4a79-9b7c-cf1de1c76c15',
    #            'clientSecret': 'XX_l4KtGw36hxZE5BFqzwQ=='
    # }
    payload = {
        'clientId': readClient_ID(),
        'clientSecret': readClient_Secret()
    }

    response = requests.post(url=api_url_base, headers=headers, json=payload)

    # print(response.json()['token'])
    return response.json()['token']


def getCVADSite(token):
    api_url_base = 'https://andzhudev.xdtesting.net/citrix/orchestration/api/techpreview/me'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
               }
    # print(headers)
    response = requests.get(url=api_url_base, headers=headers)
    print(response.status_code)
    print(response.json()['Customers'][0]['Sites'][0]['Id'])
    print(response.json()['Customers'][0]['Id'])


def main():
    mytoken = getBearerToken()
    getCVADSite(mytoken)


if __name__ == '__main__':
    main()

