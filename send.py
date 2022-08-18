from filereader import Filereader

number_list = Filereader('ultimate').search()
numbers = ','.join(number_list)


class Send:

    def __init__(self,payload={'api_token': '', 'to': 'numbers', 'body': '', 'from': '', 'gateway': '0',
                                              'append_sender': '0'}):
        self.url = 'https://www.bulksmsnigeria.com/api/v2/sms/create'
        self.payload = payload
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    def main(self):
        import requests
        response = requests.request("POST", self.url, headers=self.headers, params=self.payload)
        print(response.status_code)
        print(response.text)
