import os
import time
import subprocess
from datetime import datetime
import json


def is_service_running(name):
    with open(os.devnull, 'wb') as hide_output:
        exit_code = subprocess.Popen(['service', name, 'status'], stdout=hide_output, stderr=hide_output).wait()
        return exit_code == 0



def checkProcessStatus(serviceList):
     List=[]
     for services in serviceList:
        print("######Checking status for "+ services + " serivce##### ")
        if not is_service_running(services):
           service_status="DOWN"
           List.append("DOWN")
        else :
           service_status="UP"
           List.append("UP")
        dictionary = {
            "service_name":services,
            "service_status":service_status,
            "host":"aaloksinghvi2c.mylabserver.com:HOST1"
        }
        timestampstr = time.strftime("%Y%m%d-%H%M%S")
        filename = services+"-status-"+timestampstr
        try:
            with open(filename,"w") as outfile:
                  json.dump(dictionary,outfile)
        except Exception as e:
            print("Error occured while writing to file :" +e)

        print("Status for "+services+" is uploaded to " + filename)
     downCount = List.count("DOWN")
     if downCount > 0 :
        dictionary = {
            "service_name":"rbcapp1",
            "service_status":"DOWN",
            "host":"aaloksinghvi2c.mylabserver.com:HOST1"
        }
        timestampstr = time.strftime("%Y%m%d-%H%M%S")
        filenamerbc = "rbcapp1"+"-status-"+timestampstr
        try:
            with open(filenamerbc,"w") as outfile:
                  json.dump(dictionary,outfile)
        except Exception as e:
            print("Error occured while writing to file :" +e)

     


if __name__ == "__main__":
    serviceList=["httpd","postgres","rabbitmq"]
    checkProcessStatus(serviceList)
