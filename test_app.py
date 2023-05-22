import requests as rq
import json

PORT = 8080
headers = {
'Content-Type': 'application/json',
}

def get_response(dollar):
    json_data = {
        'dollar': dollar,
    }
    try:
        url = 'http://localhost:{}/conversion'.format(PORT)
        resp = rq.post(headers=headers, url=url, json=json_data)
        resul = json.loads(resp.text.replace('\n', ''))
        return float(resul['real'])
    except Exception as e:
        print(e)
        
    

def test_conversion():
    assert 4.97 == get_response(1)