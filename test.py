from urllib import urlencode
from urlparse import urlparsde, parse_qs

import json
import os
import random
import string
import sys
import requests
import sys


url = 'https://eappiot-api.sensbysigma.com/api/v2/SensorCollections'

auth = 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzIjoiMjAxNy0wOC0wNFQwOTo1OToyMi4xMDgrMDA6MDAiLCJleHAiOjE1MDE4NDA3NjIsIm5iZiI6LTYyMTM1NTk2ODAwLCJpYXQiOi02MjEzNTU5NjgwMCwibmFtZSI6InRlc3QiLCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlzc3VlZCI6IjAwMDEtMDEtMDFUMDA6MDA6MDArMDA6MDAiLCJ1c2VySWQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAifQ==.vyN7qMIzy4lRj/GdXH2+rMntU82kOU8KQ6T3GSHc3ik='

headers = {'Authorization': auth, 'X-DeviceNetwork': '501a86f6-c3da-4b27-ab3d-2fb5e7963a7e', 'Content-type': 'application/json'}

response = requests.get(url, headers=headers)

print(json.dumps(response.text, default=jdefault))