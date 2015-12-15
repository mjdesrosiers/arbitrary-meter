# basic server for responding to data requests from a device

from flask import Flask
import secret
import requests
import json
app = Flask(__name__)

OWM_TEMPLATE = "http://api.openweathermap.org/data/2.5/weather?q=22902&appid={}"
OWM_URL = OWM_TEMPLATE.format(secret.OPENWEATHERMAP_API_KEY)

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

@app.route('/data-request/<devid>/<source>')
def serve_data(devid, source):
    req = requests.get(OWM_URL)
    if (req.status_code == 200):
        content = json.loads(req.content)
        temp_K = content['main']['temp']
        temp_F = (temp_K - 273.15)* 1.8 + 32
        temp_F = scale(temp_F, (0, 100), (0, 1023))
        temp_F = int(temp_F)
        print(temp_F)
        return str(temp_F)
    else:
        return -1

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)