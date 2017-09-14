# basic server for responding to data requests from a device

import secret
import requests
import json
import os
import sys

OWM_TEMPLATE = "http://api.openweathermap.org/data/2.5/weather?q=22902&appid={}"
OWM_URL = OWM_TEMPLATE.format(secret.OPENWEATHERMAP_API_KEY)

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

scaled_temp = 0

req = requests.get(OWM_URL)
if (req.status_code == 200):
    content = json.loads(req.content)
    temp_K = content['main']['temp']
    temp_F = (temp_K - 273.15)* 1.8 + 32
    print(temp_F)
    temp_F = scale(temp_F, (0, 100), (0, 255))
    temp_F = int(temp_F)
    print(temp_F)
    scaled_temp = temp_F

cmds = ["export LD_LIBRARY_PATH=/usr/local/lib", "cd ~/RF24/librf24-bbb/librf24/examples/"]


TEMPERATURE = scaled_temp
cmds.append("./update_temp {}".format(TEMPERATURE))

cmd = ";".join(cmds)

print(cmd)

os.system(cmd)
