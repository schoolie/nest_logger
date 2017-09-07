import nest
import sys

from config import *

napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)

if napi.authorization_required:
    print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
    if sys.version_info[0] < 3:
        pin = raw_input("PIN: ")
    else:
        pin = input("PIN: ")
    napi.request_token(pin)