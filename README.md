# parking-decision-service

Steps to perform:

1. Turn on Docker hub app
2. Clone project
3. Open Terminal
4. Run: docker compose up -d
5. Run: setup_db_schema() inside db/migrations
6. help commands: docker ps, kill, down

Design: 

1. BP= gets BC, DAL and API
execute function makes request, check payload, and loading to DB and there's a construct method  
2. BC= execute function that analyzer the number-plate if valid one
3. DAL= using postgres, ORM
4. IaC= docker compose
