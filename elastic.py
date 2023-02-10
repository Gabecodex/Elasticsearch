from elasticsearch import Elasticsearch
##setup connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=('elastic', 'Ggl8QRDuWiJucOxgzSxz'))
print(es.ping())
##create index
es.indices.create(index="first-2_9_2023")
##display all indices
indices=es.indices.get_alias()
for index in indices:
    print(index)