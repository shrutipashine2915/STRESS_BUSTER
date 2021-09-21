import requests
import json

class message:
    def __init__(self,no,name):
        url = "https://www.fast2sms.com/dev/bulk"

        str='Alert!! THIS IS STRESSBUSTER TEAM HERE WE ARE INFORMING U TO THAT YOUR CHILD/FRIEND ' +name+ ' IS SUFFERING FROM STRESS PLS CONTACT'
        my_data = {
            
            'sender_id': 'TXTIND',

            
            'message': str,

            'language': 'english',
            'route': 'p',

           
            'numbers': no
        }


        headers = {
            'authorization': 'umMyc9p0KZenVO2DXHboiwGAFr1kshL5zdlT7IPq8CWvSgUEBfRuPzBnCJr0LKeIHF1tVkp6UodfYOX2',
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST",
                                    url,
                                    data=my_data,
                                    headers=headers)
        # load json data from source
        returned_msg = json.loads(response.text)

        # print the send message
        print(returned_msg['message'])
