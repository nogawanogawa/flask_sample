from microservice import create_app
import json

def test_search(client):
    response = client.get('/myapp/search/')
    data = json.loads(response.data)    
    shards= data['_shards']

    assert shards['failed'] == 0

def test_register(client):
    response = client.post('/myapp/register/',  data=dict(title="hoge", contents="piyo"))

    data = json.loads(response.data)

    assert data['result'] == 'created'
