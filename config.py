import os

client_id = '747bc52b-a233-4f6e-8897-d8024825cafa'
client_secret = 'aBjNY0fqY31Jeiy1MT1lGE857'

root_dir = os.environ['NEST_LOG_ROOT']
access_token_cache_file = os.path.join(root_dir,'nest.json')
db_file = os.path.join(root_dir, 'db.json')