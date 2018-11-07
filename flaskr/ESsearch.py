from elasticsearch import Elasticsearch
import json
import time

class ESearch:
    def __init__(self):
        self.ES = Elasticsearch([{'host':'localhost','port':9200}])
    
    def insert(self, id, author_id, created, upvotes, title, body, bestAnswer):
        print ("created: ", created)
        js = {"id":id,
        "author_id":author_id,
        "created":created,
        "upvotes":upvotes,
        "title":title,
        "body":body,
        "bestAnswer":bestAnswer,}
        
        res = self.ES.index(index="stackoverflow", doc_type="question",id=id,body=js)
        
    def Elsearch(self, pattern):
        res = self.ES.search(index="stackoverflow", doc_type="question", body={
            'query':{
                'match':{
                    "body":str(pattern)
                }
            }
        })
        return res
    
    def search(self, pattern):
        resp = self.Elsearch(pattern)
        res = []
        print 
        for item in resp['hits']['hits']:
            dic = {}
            dic.update({"score" : item['_score']})
            dic.update({'qid': item['_source']['id']})
            dic.update({'author_id':item['_source']['author_id']})
            dic.update({"created":item['_source']['created']})
            dic.update({"upvotes":item['_source']['upvotes']})
            dic.update({"title":item['_source']['title']})
            dic.update({"body":item['_source']['body']})
            dic.update({"bestAnswer":item['_source']['bestAnswer']})
            res.append(dic)
        return res

if __name__ == "__main__":
    obj = ESearch()
    # obj.insert(1, 1,888,2,"Stackoverflow Question", "does nitish loves to eat watermelon?", "yes he does")
    res = obj.search("watermelon")
    for item in res:
        print (item)