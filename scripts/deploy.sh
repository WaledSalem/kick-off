#!/bin/bash
ssh -i ~/.ssh/jenkins_agent_key swarmanager

sudo rm -rf kick-off

git clone https://github.com/WaledSalem/kick-off.git

cd kick-off

sudo docker stack rm kick-stack

sudo docker stack deploy --compose-file docker-compose.yaml kick-stack