# TECHNICAL TEST 2

Write ansible playbook which perform following task on HOST1, HOST2 and
HOST3 a) Create an Ansible inventory file for the above hosts that meets the
monitoring needs explained above
b) Write an Ansible playbook that will action based on a provided variable named
"action": (clarify the action variable)
1. "action=verify_install": verifies the services are installed on their allocated hosts and if not, the playbook should install it. (for the install, please pick just one service to illustrate)
2. "action=check-disk" : with this action it should check the disk space on all servers and report any disk usage > 80%. Send an alert email to a selected email address (Pick your own).
3. "action=check-status": with this action it should return the status of the application “rbcapp1” and a list of services that are down. (you can use the REST endpoint created in TEST1).

Below is a sample command to run the playbook 
 Ansible-playbook assignment.yml -I inventory -e action=verify_install ---- This is for verify install as an example

<b>Pre-requisites , Installation and setup</b>

In order demonstrate the above challenger I spun 4 servers on playground using linux academy portal namely

```
aaloksinghvi1c.mylabserver.com (Ansible Controller Server)
aaloksinghvi2c.mylabserver.com (HOST1 - HTTPD Services and RBCAPP1 Application)
aaloksinghvi3c.mylabserver.com (HOST2 - RabbitMq Service)
aaloksinghvi4c.mylabserver.com (HOST3 - Postgresql Service)
```
Created a rbcapp1 systemd service which will run as service on aaloksinghvi2c.mylabserver.com. Details and code for rbcapp1 service demonstrated in TEST1.
