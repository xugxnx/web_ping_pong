# WEB ping-pong on Python using Ansible and Docker

### Prerequisites:

Play with Docker service (PWD) or local machine with Python, Ansible and Docker installed

If using PWD instanse, run: "apk update && apk add ansible"

### HowTo:

git clone https://github.com/xugxnx/web_ping_pong.git

cd web_ping_pong

ansible-playbook ansible/playbook.yml

---
For output results use "docker logs containername" or "docker attach containername"
