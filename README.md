## Fall2023_IDS706 Individual Project 4: Auto Scaling Flask App Using Any Platform As a Service
### by Jiayi Zhou [![CI](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject4_JiayiZhou/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject4_JiayiZhou/actions/workflows/cicd.yml)
### Purpose
This is for class data engineering individual project 4: build a publicly accessible auto-scaling container using Azure App Services and Flask. This is an easy way to build and deploy a scaleable web-hosted.

### Video
[YouTube]([https://youtu.be/C-rZvuf1OUQ](https://youtu.be/46Ns00ozexE))

### Overview
The app is a food recommendation application based on the input of nutrients. It is a Flask web application integrated with OpenAI's LLM model, utilizing Docker for effective containerization. Here is a brief workflow overview of the Flask web application:
* User Input: Users input nutrients into the application.
* Search: The application processes the inputted nutrients and searches for foods abundant in those nutrients.
* Output: The top two foods are listed for the user.
<img width="591" alt="Screenshot 2023-12-09 at 10 07 49 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject4_JiayiZhou/assets/143651921/0fbc7458-5bb9-49df-9ecc-a5a112d5d00e">
<img width="703" alt="Screenshot 2023-12-09 at 10 07 56 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject4_JiayiZhou/assets/143651921/147355a1-b468-4b09-9ba6-b599d2a97e77">

### Key Components
1. Flask Web Application:
* Functionality: The web app allows users to input prompts, which are then processed by the GPT-3.5 model to generate responses. The responses are displayed on a results page.
  * The web app (main.py) incorporates routes for the index page and the result page. User can input nutrients.
  * HTML Templates: The project contains HTML templates (index.html and result.html) providing a user-friendly interface.
2. Open AI LLM Model Integration:
* API Interaction: The application interfaces with the Open AI LLM Model via API calls. It sends a the user input of nutrients to get predictions.
3. Docker Containerization:
*Dockerfile:* This Dockerfile containerizes a Flask app, setting up a Docker container with Python and Gunicorn to run the web application. It encapsulates the app's code and dependencies, simplifying deployment across different environments.

### Azure Container Apps Deployment
* Azure Container Registry:
<img width="1332" alt="Screenshot 2023-12-09 at 10 33 54 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject4_JiayiZhou/assets/143651921/e9324b46-95e9-4286-8ff5-11df379c07f1">
* Azure Container Apps Deployment:
<img width="1333" alt="Screenshot 2023-12-09 at 10 33 31 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject4_JiayiZhou/assets/143651921/88b9463f-a6d0-4c26-bca2-d935f6448763">

### Docker
<img width="1505" alt="Screenshot 2023-12-09 at 10 37 34 PM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject4_JiayiZhou/assets/143651921/c75e10ec-eaa5-44c9-beab-d47e8a749a8d">

### Preparation: 
1. git clone the repo
2. install: `make install`
3. get access to user token via GPT
4. create an env file and add user token
5. run: `python main.py` and navigate to the locally hosted website
6. upload image or use default image
7. build docker image: `docker build --tag <insert image name> .`
8. login to azure cli: `az login`
9. deploy azuer web app: `az containerapp up --resource-group <insert resource group> --name <insert app name> --ingress external --target-port 50505 --source .`
10. view app via `conatiner apps` and docker image via `container regsitry` in azure web portal 

### Check Format and Test Errors: 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`
