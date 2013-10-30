import os
from riak import RiakClient, RiakNode

RiakClient()
RiakClient(protocol='http', host=os.getenv(MJDSYS_RIAK_HTTPCONNECT), http_port=8098)
RiakClient(nodes=[{'host': os.getenv(MJDSYS_RIAK_HTTPCONNECT),'http_port':8098}])
RiakClient(protocol='http', nodes=[RiakNode()])

print RiakClient
