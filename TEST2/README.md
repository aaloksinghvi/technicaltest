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

-> In order demonstrate the above challenger I spun 4 servers on playground using linux academy portal namely

```
aaloksinghvi1c.mylabserver.com (Ansible Controller Server)
aaloksinghvi2c.mylabserver.com (HOST1 - HTTPD Services and RBCAPP1 Application)
aaloksinghvi3c.mylabserver.com (HOST2 - RabbitMq Service)
aaloksinghvi4c.mylabserver.com (HOST3 - Postgresql Service)
```
-> Created a rbcapp1 systemd service which will run as service on aaloksinghvi2c.mylabserver.com. Details and code for rbcapp1 service demonstrated in TEST1.

```
[root@aaloksinghvi2c api]# service rbcapp1 status
Redirecting to /bin/systemctl status rbcapp1.service
● rbcapp1.service - RBCAPP1 Service
   Loaded: loaded (/usr/lib/systemd/system/rbcapp1.service; enabled; vendor preset:
disabled)
   Active: inactive (dead) since Sat 2020-09-12 03:46:59 UTC; 3h 0min ago
 Main PID: 1516 (code=killed, signal=HUP)
Sep 12 03:46:59 aaloksinghvi2c.mylabserver.com systemd[1]: Started RBCAPP1 Service.
[root@aaloksinghvi2c api]#
```

-> Created ansible users on all agents/hosts and making sure passwordless logins works using ansible user from
```
sources: aaloksinghvi1c.mylabserver.com -> desitnation: aaloksinghvi2c.mylabserver.com
sources: aaloksinghvi1c.mylabserver.com -> desitnation: aaloksinghvi3c.mylabserver.com
sources: aaloksinghvi1c.mylabserver.com -> desitnation: aaloksinghvi4c.mylabserver.com
```
-> Structure of Playbook -  For each action mentioned in the problem statement a role is defined
```
[root@aaloksinghvi1c project]# tree
.
├── assignment.yaml
├── inv
├── roles
│   ├── check_disk
│ │ └── tasks
│   │       └── main.yaml
│   ├── check_status
│ │ └── tasks
│   │       └── main.yml
│   └── verify_install
│ └── tasks
8 directories, 6 files
```
Sample output when ansible playbook is executed for each action :

```
1. action=verify_task

[ansible@aaloksinghvi1c project]$ ansible-playbook -i inv assignment.yaml -e
"action=verify_install"
[WARNING]: Found variable using reserved name: action
PLAY [all]
***************************************************************************************
TASK [Gathering Facts]
***************************************************************************************
ok: [aaloksinghvi4c.mylabserver.com]
ok: [aaloksinghvi3c.mylabserver.com]
ok: [aaloksinghvi2c.mylabserver.com]
TASK [set_fact]
***************************************************************************************
ok: [aaloksinghvi2c.mylabserver.com]
ok: [aaloksinghvi3c.mylabserver.com]
ok: [aaloksinghvi4c.mylabserver.com]
TASK [verify_install]
***************************************************************************************
TASK [verify_install : INSTALL HTTPD SERVICE ON HOST1]
***************************************************************************************
skipping: [aaloksinghvi3c.mylabserver.com] => (item=httpd)
*
*
*
*
*
skipping: [aaloksinghvi4c.mylabserver.com] => (item=httpd)
ok: [aaloksinghvi2c.mylabserver.com] => (item=httpd)
TASK [verify_install]
***************************************************************************************
skipping: [aaloksinghvi4c.mylabserver.com] => (item=httpd)
skipping: [aaloksinghvi3c.mylabserver.com] => (item=httpd)
ok: [aaloksinghvi2c.mylabserver.com] => (item=httpd)
TASK [verify_install : INSTALL RABBITMQ SERVICE ON HOST2]
***************************************************************************************
skipping: [aaloksinghvi2c.mylabserver.com] => (item=rabbitmq-server)
skipping: [aaloksinghvi4c.mylabserver.com] => (item=rabbitmq
```
NOTE : Worked on installing all the required services on respective host mentioned in
Pre-requisite section but ran into issues in install rabittmq and postgres. HTTPD is
working fine and output is shown above.
