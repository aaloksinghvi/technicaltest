# TECHNICAL TEST 1

<b> PROBLEM STATEMENT </b>

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

https://myservice.rbc.com/add<n>
https://myservice.rbc.com/health_check

<b>Pre-requisites , Installation and setup </b>
-> Assuming we have rbcapp1, httpd , postgres and rabbitmq running as a service on same linux servers.
For test purpose we are running on aaloksinghvi2c.mylabserver.com
Created following service files under /usr/lib/systemd/system ( Code attached )
```
rbcapp1.service
postgres.service
rabbitmq.service
```
Created following python files under /usr/bin/ ( Code Attached )
```
rbcapp1.service
postgres.service
rabbitmq.service
```
->In order to upload the payload installed Elasticsearch on aaloksinghvi2c.mylabserver.com
Updated /etc/yum.repos.d with new elastic search repo to install the rpm package for elastic search
```
[root@aaloksinghvi2c api]# cat /etc/yum.repos.d/elasticsearch.repo 
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
[root@aaloksinghvi2c api]# 
```
