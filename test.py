import os
from riak import RiakClient, RiakNode

r= RiakClient()
r(protocol='http', host=os.getenv('MJDSYS_RIAK_HTTPCONNECT'), http_port=8098)
r(nodes=[{'host': os.getenv('MJDSYS_RIAK_HTTPCONNECT'),'http_port':8098}])
r(protocol='http', nodes=[RiakNode()])

r.ping()

print r.ping()

