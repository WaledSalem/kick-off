#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF


cd kick-off/loadbalancer/

docker-compose down --rmi all 

sudo rm -rf kick-off

EOF