#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swarmanager << EOF

docker stack rm kick-stack

sudo rm -rf kick-off
EOF