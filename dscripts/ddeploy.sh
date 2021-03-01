#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swarmanager << EOF

sudo rm -rf kick-off

docker stack rm kick-stack
EOF