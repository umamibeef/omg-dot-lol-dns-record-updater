import os
import requests

def update():
    try:
        # get relevant environemnt variables
        api_key = os.getenv('OMG_API_KEY')
        omg_address = os.getenv('OMG_ADDRESS')
        dns_record_name = '.'.join((os.getenv('OMG_DNS_RECORD_NAME'),omg_address))
        # get public IP
        ip = requests.get('https://api.ipify.org').content.decode('utf8')
        print(f'Got a public IP of {ip} from https://api.ipify.org')
        # get a list of records from the specified omg.lol username
        url = f'https://api.omg.lol/address/{omg_address}/dns'
        headers = {'Authorization': api_key}
        response = requests.get(url, headers=headers).json()
        id = None
        for dns_record in response['response']['dns']:
            if dns_record['name'] == dns_record_name:
                id = dns_record['id']
                print(f'Found ID:{id} for DNS record {dns_record_name}')
                # Check if DNS record already has the correct IP
                print(dns_record)
                if dns_record['data'] == ip:
                    print('DNS record already has the correct IP! Nothing left to do here :)')
                    exit(0)
        # update record if we got an ID for it
        if id:
            url = f'https://api.omg.lol/address/{omg_address}/dns/{id}'
            # same header as above
            payload = {'type': 'A', 'name': '@', 'data': ip}
            response = requests.patch(url, json=payload, headers=headers).json()
            response_message = response['response']['message']
            if response['request']['success']:
                print('Successfully updated DNS record! omg.lol API response:' + response_message)
            else:
                print('Failed to update DNS record! omg.lol API response:' + response_message)

    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    update()
