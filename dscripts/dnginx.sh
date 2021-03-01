#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF

sudo rm -rf kick-off

docker-compose down --rmi all 

EOF