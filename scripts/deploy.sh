#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swarmanager << EOF

git clone https://github.com/WaledSalem/kick-off.git

cd kick-off

docker stack deploy --compose-file docker-compose.yaml kick-stack
EOF