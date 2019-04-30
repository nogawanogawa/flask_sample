from elasticsearch import Elasticsearch

class MyApp():
    
    def __init__(self):
        self.es = Elasticsearch("elasticsearch:9200")
        self.index = "sample"

    def search(self):

        res = self.es.search(index=self.index,  body={"query": {"match_all": {}}})
        return res

    def register(self, title="title", contents="contents"):

        document = {}
        document["title"] = title
        document["contents"] = contents

        res = self.es.index(index=self.index, doc_type=self.index, body=document)

        return res

if __name__ == "__main__":
    myapp = MyApp()
    print(str(myapp.register(title="hoge", contents="fuga")))

