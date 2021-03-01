#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF

docker rm -f $(docker ps -qa)
sudo rm -rf kick-off

EOF