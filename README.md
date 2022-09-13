# parking-decision-service

Steps to perform:

1. Turn on Docker hub app
2. Clone project
3. Run: pip install -r requirements.txt
4. Run: docker compose up -d
5. Run: setup_db_schema() inside db/migrations

6. Helps commands: docker ps, kill, down
7. Run format: pre-commit run --all-files
8. Run tests: python -m pytest

9. After download package run: pip3 freeze >> requirement.txt

10. Build image: docker build --tag my-python-docker-image-app
11. Verify: docker images
12. Tagging: docker tag my-python-docker-image-app:latest python-docker:v1.0.0
13. Remove-Tag: docker rmi python-docker:v1.0.0
14. Start the Docker Container: docker run -d --name mycontainer -p 80:80 my-python-docker-image-app
