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
[root@aaloksinghvi2c api]# yum install elasticsearch
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: d36uatko69830t.cloudfront.net
 * epel: mirror.steadfastnet.com
 * extras: d36uatko69830t.cloudfront.net
 * nux-dextop: mirror.li.nux.ro
 * updates: d36uatko69830t.cloudfront.net
Nothing to do
[root@aaloksinghvi2c api]# curl -v localhost:9200/_cat/health
* About to connect() to localhost port 9200 (#0)
*   Trying ::1...
* Connected to localhost (::1) port 9200 (#0)
> GET /_cat/health HTTP/1.1
> User-Agent: curl/7.29.0
> Host: localhost:9200
> Accept: */*
> 
< HTTP/1.1 200 OK
< content-type: text/plain; charset=UTF-8
< content-length: 65
< 
1600038752 23:12:32 elasticsearch yellow 1 1 3 3 0 0 3 0 - 50.0%
* Connection #0 to host localhost left intact
[root@aaloksinghvi2c api]# 
```
