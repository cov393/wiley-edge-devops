## Instructions
1. Push all code files to your GitHub account in a public repository.
2. Share the GitHub repository link 1-on-1 with Mandeep on Slack.
## Assignment
1. Build a Python application that, when run, launches a simple HTTP server. 
You may use any port number for the HTTP server. You may also choose to 
display whatever content on the landing page.
2. Containerise the application using a Dockerfile. You should be able to launch
the application with the ‘docker run’ command. You may choose to pass 
additional arguments to the ‘docker run’ command if required.
3. Create a Jenkins pipeline job to trigger the docker build & run operations. 
Create the trigger in a way that any code push to GitHub main branch 
triggers the Jenkins job. Ensure to code the pipeline in Jenkinsfile, not the 
Jenkins portal.
4. Extend the Jenkinsfile to include another stage to push the built docker 
image to your Docker Hub account.
5. Create a Kubernetes Deployment object using YAML that can deploy your 
docker image to a Kubernetes cluster. You may choose any number of 
replicas.
6. Create a Kubernetes Service object using YAML so that you can access the 
deployed application via a web browser.
### *Expected Deliverables (in GitHub):*
1. Python code (in .py files)
2. Dockerfile
3. Jenkinsfile
4. Kubernetes YAML files:
a. Deployment
b. Service