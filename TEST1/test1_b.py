import requests
import flask
from flask import Flask,request
from elasticsearch import Elasticsearch
import os

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def checkProcessStatus():
   stat = os.system('service rbcapp1 status')
   print(stat)
   if stat == 768 :
      returnCode="DOWN"
   else :
      returnCode="UP"
   return str(returnCode)

@app.route('/add', methods = ['POST'])
def postJsonHandler():

    if request.is_json :
	print("TEST")
        content = request.get_json(silent=True)
        print(content)
        print("TEST")
    	try:
          print("TEST")
          checkElasticSearch(content)
          print("TEST")
        except:
          print("Error in writing to elastic search index")
    return content

@app.route('/uploadjson', methods = ['POST'])
def postJsonUpload():

    file = request.files['file']
    file.seek(0)
    myfile = file.read()

def checkElasticSearch(content):
    print("TEST")
    print("Writing Data to Elastic Search")
    print(content)
    res =  requests.get('http://localhost:9200')
    print(res.content)
    es=Elasticsearch([{'host':'localhost','port':9200}])
    res = es.index(index=content["service_name"]-{now/d},doc_type='rbcapp1',id=1,body=content)

if __name__ == "__main__":
    content=app.run(host='myservice.rbc.com',debug=True, port=8000)
