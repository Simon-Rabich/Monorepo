# Parking Decision MicroService
### _Parking Decision Backend Service giving inspiration and sort of template to study from_
### _Level: easy-medium_
### _This repo will take you fast-forward to be beyond exceptional_

This repository contains backend code, using the FastAPI framework.

- CI with GitHub action
- CD with AWS (not yet)
- FastAPI + pg db + docker
- Best practices implementations
- USING:
- Construct, DAL, ORM, TDD full coverage, docker, swagger
- Workflows, git hooks, SDK, common, PEP8 helpers, PR templates
- TODO:
- make serverless, add env configs for dev, stg, uat, prd

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
- [unittest] - Unit-tests for code
- [PIP] - Package manager
- [isort] Importing sorting to organize all the imports in our codes
- [PEP8] Line length is 79, which is the PEP8 standard used by Flake8
- [Pylint] Checks for bugs, helps enforce a coding standard
- [mypy] Checks for Static typing
- [Dependabot] Keeping the dependencies updated automatically, Keeps on Productivity
- [requirements.txt] Using Dependabot to make sure we always have the latest version
-
## Installation

Parking decider requires [Python](https://www.python.org/downloads/) to run.

## Setup

To manually create a virtualenv on MacOS and Linux:

```sh
python3 -m venv venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```sh
source venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```sh
pip install -r requirements.txt
```

## StartDB

```sh
docker compose up -d
```

## Setdb-schema

```sh
setup_db_schema() function inside db/migrations/setup_db_schema.py
```

## 3rd Party API

Parking decision uses the following APIs.
This API is know how to get an image and extract the text from it.

| API              | Documentation |
|------------------| ------ |
| OCRapi           | https://ocr.space/ocrapi |


## Help

```sh
$ docker ps, kill, down
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
```sh
#build-an-image
$ docker build --tag my-python-docker-image-app
```
```sh
#verify-image
$ docker images
```
```sh
#tag-image
$ docker tag my-python-docker-image-app:latest python-docker:v1.0.0
```
```sh
#remove-tag
$ docker rmi python-docker:v1.0.0
```
```sh
#start-container
$ docker run -d --name mycontainer -p 80:80 my-python-docker-image-app
```
