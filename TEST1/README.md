# TECHNICAL TEST 1

<b> PROBLEM STATEMET </b>

Assume all 3 services are running on the same server as Linux services.
a) Write a Python script that monitors these services and creates a JSON object with application_name, application_status and host_name.
Sample JSON Payload
{
“service_name”:“httpd”,
“service_status”:“UP”,
“host_name”:“host1”
}
Please write this JSON object to a file named {serviceName}-status-{@timestamp}.json
b) Write a simple Python REST webservice that:
Accepts the above created JSON file and writes it to Elasticsearch
Provide a second endpoint where the data can be retrieved, i.e
-> POST /add -> Insert payload into Elasticsearch
-> GET /health_check -> Return the Application status (“UP” or “DOWN”)

Sample calls

https://myservice.rbc.com/add
https://myservice.rbc.com/health_check
