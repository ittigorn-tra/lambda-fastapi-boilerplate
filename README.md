# Lambda FastAPI Boilerplate Project
This is a boilerpalte for FastAPI on AWS Lambda.

# Requirements
1. Python 3.9
2. Node 12.20.1 or higher (for serverless deployment)
3. Serverless framework 3 (for deployment)
4. Pipenv

## Create pipenv environment
### Install Python packages with development dependencies (for debugging and testing on local machine)
```
pipenv install --dev
```
### Install Python packages without development dependencies (for production environment)
```
pipenv install
```
### Activating the pipenv environment
```
pipenv shell
```

# Local Testing & Debugging
## Run server directly
```
uvicorn main:app --reload
```

## Run server with serverless-offline
### Install serverless
```
npm install -g serverless
```

### Install plugins
```
sls plugin install -n serverless-dotenv-plugin
sls plugin install -n serverless-python-requirements
sls plugin install -n serverless-prune-plugin
sls plugin install -n serverless-offline
```

### Run local server
```
serverless offline --stage local
```
