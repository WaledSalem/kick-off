#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swanginx << EOF

docker system prune --all
sudo rm -rf kick-off

EOF