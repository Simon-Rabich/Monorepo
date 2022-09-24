# Setup-Grafana-with-Prometheus-for-Python-projects-using-Docker

Service monitoring allows us to analyze specific events in our projects such as database calls, API interaction, tracking resource performance, etc. You can easily detect unusual behaviour or discover useful clues behind the issues.

requirements.txt

prometheus-client

Start running services

docker-compose up -d

Grafana: 

http://localhost:3000/

admin both for username and password.

select Data Sources from the page.
Next, select Prometheus as a data source:
put in url http://prometheus:9090
Click on Save and Test

navigate to http://localhost:3000/dashboards

 Click New Dashboard and then New Panel
 
run request_processing_seconds_count query

Don't forget to build the docker image again for all services, after updating stuff:

docker-compose up -d --build

use 'docker scan' for using Snyk
