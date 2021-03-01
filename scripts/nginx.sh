#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF

sudo rm -rf kick-off

git clone https://github.com/WaledSalem/kick-off.git

cd kick-off/loadbalancer/

docker-compose down --rmi all 

docker-compose up -d

EOF