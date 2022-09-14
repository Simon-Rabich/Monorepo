# Parking Decision 
### _Service_

This repository contains backend code, using FastAPI framework.

- CI with github action
- CD with AWS
- FastAPI + postgers + docker
- Best practices

## Tech

This repository uses number of open source projects to work properly:

- [Github Actions] - Uses workflows to run linters, releasing, and deployments
- [FastAPI] - backend framework for building web applications
- [Python] - Strongly typed code with Python
- [Pre-commit] - Git hooks
- [Docker] - Deliver repository code ready to use without manually installing softwares
- [Flake8] - Linting the code and prevents bad code
- [Git] - Version manager for the repository
- [Toml] - Styling your code
- [Pytest] - Unit-tests for code
- [PIP] - Package manager

## Installation

Landing page requires [Node.js](https://nodejs.org/) v12+ to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install -r requirements.txt
```

For production environments...

```sh
docker compose up -d
Run: setup_db_schema() inside db/migrations
```

## APIs

Landing page uses the following APIs.
Instructions on how to use them in your own application are linked below.

| API              | Documentation |
|------------------| ------ |
| OCRapi           | https://ocr.space/ocrapi |


## Help

```sh
docker ps, kill, down
```

## Format

```sh
pre-commit run --all-files
```

## Tests

```sh
python -m pytest
```

## Maintain

```sh
pip3 freeze >> requirement.txt
```

## Docker 
build-image / verify-img / tag-img / rm-tag / start-container

```sh
docker build --tag my-python-docker-image-app
```
```sh
docker images
```
```sh
docker tag my-python-docker-image-app:latest python-docker:v1.0.0
```
```sh
docker rmi python-docker:v1.0.0
```
```sh
docker run -d --name mycontainer -p 80:80 my-python-docker-image-app
```