#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF

git clone https://github.com/WaledSalem/kick-off.git

cd kick-off/loadbalancer/

docker-compose up -d

EOF