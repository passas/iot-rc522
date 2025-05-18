import os
from dotenv import load_dotenv
import requests
import datetime

class WebClient:
    API_IP = '127.0.0.1'
    API_PORT = '8000'
    API_V = 'v1'

    @classmethod
    def load_env(cls):
        load_dotenv()
        cls.API_IP=os.getenv('API_IP', '127.0.0.1')
        cls.API_PORT=os.getenv('API_PORT', '8000')
        cls.API_V=os.getenv('API_V', 'v1')

    @classmethod
    def login(cls, email, password):
        client = None
        code = -1
        msg = 'Empty credentials'
        if email and password:
            data = {}
            data['username']=email
            data['password']=password
            try:
                r = requests.post(f'http://{cls.API_IP}:{cls.API_PORT}/api/login', data=data)
                code = r.status_code
                if code==200:
                    client = cls(r.json()['access'])
                else:
                    msg = r.json()['detail']
            except requests.exceptions.ConnectionError:
                code = 500
                msg = 'Server down'
            except requests.exceptions.JSONDecodeError:
                pass
            except requests.exceptions.RequestException:
                pass
        return client, code, msg
    
    def __init__(self, token=''):
        self._token = token

    @property
    def token(self):
        return self._token
    
    @token.setter
    def token(self, t):
        self._token=t

    @token.deleter
    def token(self):
        del self._token

    def postNewClient(self, new_client, card_id):
        msg = ''
        status = -1
        data = {}
        data['card_id'] = card_id
        data['email'] = new_client['email']
        data['first_name'] = new_client['first_name']
        data['last_name'] = new_client['last_name']
        if self.token:
            header = {
                'Authorization': f'Bearer {self.token}'
            }
            try:
                r = requests.post(f'http://{self.API_IP}:{self.API_PORT}/api/client', headers=header, data=data)
                status = r.status_code
                msg = r.json()['message']
            except requests.ConnectionError:
                pass
            except requests.JSONDecodeError:
                pass
            except requests.RequestException:
                pass
        return status, msg
    
    def getContracts(self):
        code = -1
        contracts = None
        if self.token:
            header = {
                'Authorization': f'Bearer {self.token}'
            }
            try:
                r = requests.get(f'http://{self.API_IP}:{self.API_PORT}/api/contracts', headers=header)
                code = r.status_code
                contracts = r.json()
            except requests.ConnectionError:
                pass
            except requests.JSONDecodeError:
                pass
            except requests.RequestException:
                pass
        return code, contracts
    
    def postNewContract(self, new_contract, card_id):
        msg = ''
        status = -1
        data = {}
        data['card_id'] = card_id
        data['contract'] = new_contract['contract']
        data['c_zone1'] = new_contract['c_zone1']
        data['c_zone2'] = new_contract['c_zone2']
        data['c_price'] = new_contract['c_price']
        data['c_expire'] = new_contract['c_expire']
        if self.token:
            header = {
                'Authorization': f'Bearer {self.token}'
            }
            try:
                r = requests.post(f'http://{self.API_IP}:{self.API_PORT}/api/contracts', headers=header, data=data)
                status = r.status_code
                msg = r.json()['message']
            except requests.ConnectionError:
                pass
            except requests.JSONDecodeError:
                pass
            except requests.RequestException:
                pass
        return status, msg
    
    def postNewTicket(self, new_ticket, card_id):
        msg = ''
        status = -1
        data = {}
        data['card_id'] = card_id
        data['ticket'] = new_ticket['ticket']
        data['t_zone1'] = new_ticket['t_zone1']
        data['t_zone2'] = new_ticket['t_zone2']
        data['t_amount'] = new_ticket['t_amount']
        if self.token:
            header = {
                'Authorization': f'Bearer {self.token}'
            }
            try:
                r = requests.post(f'http://{self.API_IP}:{self.API_PORT}/api/tickets', headers=header, data=data)
                status = r.status_code
                msg = r.json()['message']
            except requests.ConnectionError:
                pass
            except requests.JSONDecodeError:
                pass
            except requests.RequestException:
                pass
        return status, msg
    
    def putNewTicket(self, new_ticket, card_id):
        msg = ''
        status = -1
        data = {}
        data['card_id'] = card_id
        data['ticket'] = new_ticket['ticket']
        data['t_zone1'] = new_ticket['t_zone1']
        data['t_zone2'] = new_ticket['t_zone2']
        data['t_amount'] = new_ticket['t_amount']
        if self.token:
            header = {
                'Authorization': f'Bearer {self.token}'
            }
            try:
                r = requests.put(f'http://{self.API_IP}:{self.API_PORT}/api/tickets', headers=header, data=data)
                status = r.status_code
                msg = r.json()['message']
            except requests.ConnectionError:
                pass
            except requests.JSONDecodeError:
                pass
            except requests.RequestException:
                pass
        return status, msg


def main():
    c = WebClient()
    c.token = "ABC"
    print(c.token)

if __name__=="__main__":
    main()
