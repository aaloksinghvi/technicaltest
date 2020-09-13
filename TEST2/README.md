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

```
In order execute the check_status action we need to bring up the rest api that is running on aaloksinghvi2.mylabserver.com

[root@aaloksinghvi2c api]# python test1_b.py 
 * Serving Flask app "test1_b" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://myservice.rbc.com:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 787-355-081

[ansible@aaloksinghvi1c project]$ ansible-playbook -i inv assignment.yaml -e "action=check_status"
[WARNING]: Found variable using reserved name: action

PLAY [all] ******************************************************************************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************************************************************
ok: [aaloksinghvi3c.mylabserver.com]
ok: [aaloksinghvi4c.mylabserver.com]
ok: [aaloksinghvi2c.mylabserver.com]

TASK [set_fact] *************************************************************************************************************************************************************************************
ok: [aaloksinghvi2c.mylabserver.com]
ok: [aaloksinghvi4c.mylabserver.com]
ok: [aaloksinghvi3c.mylabserver.com]

TASK [verify_install] *******************************************************************************************************************************************************************************
skipping: [aaloksinghvi2c.mylabserver.com]
skipping: [aaloksinghvi3c.mylabserver.com]
skipping: [aaloksinghvi4c.mylabserver.com]

TASK [check disk] ***********************************************************************************************************************************************************************************
skipping: [aaloksinghvi2c.mylabserver.com]
skipping: [aaloksinghvi3c.mylabserver.com]
skipping: [aaloksinghvi4c.mylabserver.com]

TASK [check_status] *********************************************************************************************************************************************************************************

TASK [check_status] *********************************************************************************************************************************************************************************
skipping: [aaloksinghvi3c.mylabserver.com]
skipping: [aaloksinghvi4c.mylabserver.com]
ok: [aaloksinghvi2c.mylabserver.com]

TASK [check_status : debug] *************************************************************************************************************************************************************************
ok: [aaloksinghvi2c.mylabserver.com] => {
    "health_check": {
        "changed": false, 
        "content_length": "4", 
        "content_type": "text/html; charset=utf-8", 
        "cookies": {}, 
        "cookies_string": "", 
        "date": "Sun, 13 Sep 2020 23:00:28 GMT", 
        "elapsed": 0, 
        "failed": false, 
        "msg": "OK (4 bytes)", 
        "redirected": false, 
        "server": "Werkzeug/1.0.1 Python/2.7.5", 
        "status": 200, 
        "url": "http://myservice.rbc.com:8000/healthcheck"
    }
}
skipping: [aaloksinghvi3c.mylabserver.com]
skipping: [aaloksinghvi4c.mylabserver.com]

PLAY RECAP ******************************************************************************************************************************************************************************************
aaloksinghvi2c.mylabserver.com : ok=4    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
aaloksinghvi3c.mylabserver.com : ok=2    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
aaloksinghvi4c.mylabserver.com : ok=2    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   

[ansible@aaloksinghvi1c project]$ 


```
```
3. action=check_disk
[ansible@aaloksinghvi1c project]$ ansible-playbook -i inv assignment.yaml -e
"action=check_disk"
[WARNING]: Found variable using reserved name: action
PLAY [all] *********************************************************************
TASK [Gathering Facts] *********************************************************
ok: [aaloksinghvi4c.mylabserver.com]
ok: [aaloksinghvi2c.mylabserver.com]
ok: [aaloksinghvi3c.mylabserver.com]
TASK [set_fact] ****************************************************************
ok: [aaloksinghvi4c.mylabserver.com]
ok: [aaloksinghvi3c.mylabserver.com]
ok: [aaloksinghvi2c.mylabserver.com]
TASK [verify_install] **********************************************************
skipping: [aaloksinghvi2c.mylabserver.com]
skipping: [aaloksinghvi3c.mylabserver.com]
skipping: [aaloksinghvi4c.mylabserver.com]
TASK [check disk] **************************************************************
[WARNING]: While constructing a mapping from
/home/ansible/project/roles/check_disk/tasks/main.yaml, line 2, column 6, found
a duplicate dict key (when). Using last defined value only.
TASK [check_disk1] *************************************************************
skipping: [aaloksinghvi4c.mylabserver.com] => (item={u'block_used': 1888839, u'uuid':
u'0f790447-ebef-4ca0-b229-d0aa1985d57f', u'size_total': 21463281664, u'block_total':
5240059, u'inode_available': 20823887, u'block_available': 3351220, u'size_available':
13726597120, u'fstype': u'xfs', u'inode_total': 20970432, u'mount': u'/', u'device':
u'/dev/nvme0n1p1', u'inode_used': 146545, u'block_size': 4096, u'options':
u'rw,seclabel,relatime,attr2,inode64,noquota'})
failed: [aaloksinghvi2c.mylabserver.com] (item={u'block_used': 2128528, u'uuid':
u'0f790447-ebef-4ca0-b229-d0aa1985d57f', u'size_total': 21463281664, u'block_total':
5240059, u'inode_available': 20805971, u'block_available': 3111531, u'size_available':
12744830976, u'fstype': u'xfs', u'inode_total': 20970432, u'mount': u'/', u'device':
u'/dev/nvme0n1p1', u'inode_used': 164461, u'block_size': 4096, u'options':
u'rw,seclabel,relatime,attr2,inode64,noquota'}) => {
    "ansible_loop_var": "item",
"assertion": "item.size_available > item.size_total|float * 0.8",
    "changed": false,
    "evaluated_to": false,
    "item": {
        "block_available": 3111531,
        "block_size": 4096,
        "block_total": 5240059,
        "block_used": 2128528,
        "device": "/dev/nvme0n1p1",
        "fstype": "xfs",
        "inode_available": 20805971,
        "inode_total": 20970432,
        "inode_used": 164461,
        "mount": "/",
        "options": "rw,seclabel,relatime,attr2,inode64,noquota",
        "size_available": 12744830976,
        "size_total": 21463281664,
        "uuid": "0f790447-ebef-4ca0-b229-d0aa1985d57f"
},
    "msg": "disk space has reached 80% threshold"
}
skipping: [aaloksinghvi3c.mylabserver.com] => (item={u'block_used': 1864174, u'uuid':
u'0f790447-ebef-4ca0-b229-d0aa1985d57f', u'size_total': 21463281664, u'block_total':
5240059, u'inode_available': 20820538, u'block_available': 3375885, u'size_available':
13827624960, u'fstype': u'xfs', u'inode_total': 20970432, u'mount': u'/', u'device':
u'/dev/nvme0n1p1', u'inode_used': 149894, u'block_size': 4096, u'options':
u'rw,seclabel,relatime,attr2,inode64,noquota'})
TASK [check_disk : send mail] **************************************************
fatal: [aaloksinghvi3c.mylabserver.com]: FAILED! => {"changed": false, "msg":
"Unsupported parameters for (mail) module: when Supported parameters include: attach,
bcc, body, cc, charset, headers, host, password, port, secure, sender, subject,
subtype, timeout, to, username"}
fatal: [aaloksinghvi4c.mylabserver.com]: FAILED! => {"changed": false, "msg":
"Unsupported parameters for (mail) module: when Supported parameters include: attach,
bcc, body, cc, charset, headers, host, password, port, secure, sender, subject,
subtype, timeout, to, username"}
PLAY RECAP *********************************************************************
aaloksinghvi2c.mylabserver.com : ok=2
skipped=1    rescued=0    ignored=0
aaloksinghvi3c.mylabserver.com : ok=2
skipped=2    rescued=0    ignored=0
aaloksinghvi4c.mylabserver.com : ok=2
skipped=2    rescued=0    ignored=0
[ansible@aaloksinghvi1c project]$
changed=0
changed=0
changed=0
```
NOTE : I am having issues in sending emails from the server and configuring a free
smtp.
