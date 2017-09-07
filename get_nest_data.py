#!/home/brian/anaconda3/bin/python
# coding: utf-8

import nest
import datetime
import os
from tinydb import TinyDB


client_id = '747bc52b-a233-4f6e-8897-d8024825cafa'
client_secret = 'aBjNY0fqY31Jeiy1MT1lGE857'

# root_dir = os.path.join(os.path.expanduser("~"), 'Documents', 'nest_logger')
root_dir = os.environ['NEST_LOG_ROOT']
access_token_cache_file = os.path.join(root_dir,'nest.json')

napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)

import pyowm

owm = pyowm.OWM(API_key='9c1add868b3c394269fe9c2059d99dad')  # You MUST provide a valid API key
observation = owm.weather_at_place('Cedar Park, TX')
w = observation.get_weather()

structure = napi.structures[0]
devices = structure.thermostats

ignores = ['structure', 'where_id', 'serial', 'device_id']


# In[3]:

db = TinyDB(os.path.join(root_dir, 'db.json'))

for device in devices:
    props = {}
    for prop in dir(device):
        if prop[0] != '_' and prop not in ignores:
            try:
                props[prop] = getattr(device, prop)

            except NotImplementedError:
                pass
    props['request_time'] = datetime.datetime.now().strftime('%c')



    props['ext_wind'] = w.get_wind()
    props['ext_humidity'] = w.get_humidity()
    props['ext_temperature'] = w.get_temperature('fahrenheit')['temp']
    props['ext_heat_index'] = w.get_heat_index()
    props['ext_rain'] = w.get_rain()
    props['ext_status'] = w.get_detailed_status()
    
    db.insert(props)

print(props['last_connection'], props['temperature'], props['target'])



