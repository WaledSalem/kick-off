# Project Kick-Off

This Flask application generates “Objects” upon a set of predefined rules, by simulating a football senario where a player is kicking a penalty.

## Description

By means of a service-orientated architecture, the application is composed of 4 services that work together.

### Service-1

The core service – renders the Jinja2 templates needed to interact with the application, it is also responsible for communicating with the other 3 services, and finally for persisting the data in an SQL database.

### Service-2

This service generates a random “Object” -the direction where the Penalty-taker kicks the ball to score (Left, Middle, or Right)

### Service-3

This service generates a random “Object” -the direction where the Goal-keeper dives to save the ball (Left, Middle, or Right)

### Service-4

This service calculates the chance of scoring, a probability based upon the results of service #2 & #3 using actual figures (Chiappori, 2002).

### Different Implementations

Two different implementations were created for services #2, #3 & #4 , to demonstrate swapping these implementations out for each other seamlessly, without disrupting the user experience. The changes were made by changing the variables used to calculate the chance of scoring with the first version for a right- handed shooter and the second for a left-handed.

## Features

* Trello board linked to the Github repository
* Full integration using the Feature-Branch model into Github as a Version Control System that is linked to jenkins by webhooks used so that Jenkins automatically recreates and redeploys the application, if a change is made to a code base
* Jenkins is the CI server that built the model and deploy GCP virtual machine.
* The environment that the application needs to run was provisioned using Ansible for configuration management
* Nginx was the web server that was used to make the application accessible to the user
* The micro-services were deployed using Docker for containerisation and Docker Swarm as an orchestration tool

### Dependencies

* Ubuntu
* MySQL
* Jenkins
* Ansible
* Python
* Github
* Docker/Swarm
* Nginx

### Infrastructure (GCP)

* 1 MySQL instance for presisting the database
* 1 VM instance (e2-standard-2) running Jenkins
* 1 VM instance (e2-medium) for the NGINX load-balancer
* 1 VM instance (e2-medium) for the swarm manager
* 1 VM instance (e2-medium) for the swarm worker

## Links

Waled Salem  
[@WaledSalem](https://www.linkedin.com/in/waled-salem-9894261ba)

Kanban Trello Board  
[@WaledSalem](https://trello.com/b/HJY4wsGj)

Github  
[@WaledSalem](https://github.com/WaledSalem)

## Version History

* 0.1
  * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
