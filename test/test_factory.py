from microservice import create_app
import urllib.request, json

def test_search(client):
    response = client.get('/myapp/search/')
    data = json.loads(response.data)    
    shards= data['_shards']

    assert shards['failed'] == 0

def test_register(client):
    rv = client.post('/myapp/register/', json={'title': 'flask', 'contents': 'secret'})
    json_data = json.loads(rv.data)
    s  = json_data['result']
    assert s == 'created'
