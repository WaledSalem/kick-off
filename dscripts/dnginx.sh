#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF

docker system prune --all --force
sudo rm -rf kick-off

EOF