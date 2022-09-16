# Parking Decision 
### _ParkingDecision Service_

This repository contains backend code, using FastAPI framework.

- CI with github action
- CD with AWS (not yet)
- FastAPI + postgers + docker
- Best practices

## Tech

This repository uses number of open source projects to work properly:

- [Github Actions] - Uses workflows to run linters, releasing, and deployments
- [FastAPI] - backend framework for building web applications
- [Python] - ''Strongly'' typed code with Python
- [Pre-commit] - Git hooks
- [Docker] - Deliver repository code ready to use without manually installing softwares
- [Flake8] - Linting the code and prevents bad code (checks if your code complies with the PEP8 style)
- [Black] - Formatting the code and prevents bad code
- [Git] - Version manager for the repository
- [pyproject.toml] - Styling your code (A new configuration file defined in PEP 518, expanded in PEP 621 and PEP 660)
- [Pytest] - Unit-tests for code
- [PIP] - Package manager
- [isort] Importing sorting to organize all the imports in our codes
- [PEP8] Line length is 79, which is the PEP8 standard used by Flake8
- [Pylint] Checks for bugs, helps enforce a coding standard
- [mypy] Checks for Static typing 
- [Dependabot] Keeping the dependencies updated automatically, Keeps on Productivity
- [requirements.txt] Using Dependabot to make sure we always have the latest version
- 
## Installation

Parking decider requires [Python]("https://www.python.org/downloads/") to run.

## Setup

To manually create a virtualenv on MacOS and Linux:

```sh
$ python3 -m venv venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```sh
$ source venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```sh
$ pip install -r requirements.txt
```

Start the server

```sh
$ docker compose up -d
```

Start the database, run

```sh
setup_db_schema() function inside db/migrations/setup_db_schema.py
```

## API

Parking decision uses the following APIs.
Instructions on how to use them in your own application are linked below.

| API              | Documentation |
|------------------| ------ |
| OCRapi           | https://ocr.space/ocrapi |


## Help

```sh
$ docker ps, kill, down
```

## Format

```sh
$ pre-commit run --all-files
```

## Tests

```sh
$ python -m pytest
```

## Maintain

```sh
$ pip3 freeze >> requirement.txt
```

## Docker 
1. build-an-image 
2. verify-image 
3. tag-image  
4. remove-tag 
5. start-container

```sh
#1 
$ docker build --tag my-python-docker-image-app
```
```sh
#2
$ docker images
```
```sh
#3
$ docker tag my-python-docker-image-app:latest python-docker:v1.0.0
```
```sh
#4
$ docker rmi python-docker:v1.0.0
```
```sh
#5
$ docker run -d --name mycontainer -p 80:80 my-python-docker-image-app
```
