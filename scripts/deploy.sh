#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swarmanager << EOF

sudo rm -rf kick-off

git clone https://github.com/WaledSalem/kick-off.git

cd kick-off

docker stack rm kick-stack

docker stack deploy --compose-file docker-compose.yaml kick-stack
EOF

ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF

sudo rm -rf kick-off

git clone https://github.com/WaledSalem/kick-off.git

cd kick-off/loadbalancer/

docker-compose down --rmi all 

docker-compose up -d

EOF