<h1><b>Introduction</h1></b>
<br>
Auto Ci-cd generator is a Python-based application that utilizes the OpenAI feature to generate the Docker file, basic deployment, and service manifest file for Kubernetes. Additionally, it generates a pipeline file depending on the provider in which the user provides. This application helps beginner users to deploy applications in Kubernetes and set up pipelines without requiring much expertise.
<br>


<h1><b>Requirements</h1></b>
1.An openapi token has to be generated for using auto-cicd. The steps for activating an openai token is in the link below
<br>
https://platform.openai.com/account/api-keys
<br>
2.You need to clone your application directory to the machine to detect the codebase of the application.
3. User needs to generate the token for repository access for github/gitlab and also mention this token in the script.
<h2><b2>Architecture of the Application</h2></b2>
The Auto Ci-cd generator consists of a YAML file for user input. In this file, the user inputs the details of their image registry and their password. An example format of how the file looks like:
<br>

#YAML
<br>
`ymlcodebase: nodejs`
<br>
`kubeconfig-file: /home/avinash/.kubeconfig`
<br>
`registry:`
<br>
  `password: c2ltcGxlcGFzcw==`
  <br>
  `username: avinash2632`
  <br>
`repo: gitlab`
<br>


The codebase is automatically generated by the application with the built-in code detector function.
<br>


<h3><b3>How to Install and Use the Application</h3></b3>
To install and use the Auto Ci-cd generator, follow these steps:
<br></br>


<b4>Step 1</b4>: Clone the repository using the command:
`git clone https://github.com/Auto-ci-cd/ci-cd-generator.git`

<b5>Step 2</b5>: Use the command below:

`echo 'python3  /home/autocicd.py "$@"' | sudo tee /usr/local/bin/autocicd >/dev/null && sudo chmod +x /usr/local/bin/autocicd`
<br></br>
This command exports the autocicd file. Replace the </home/autocicd.py> file with the cloned file location.

<b6>Step 3</b6>: Run the command:

`autocicd --code <your-code-location>`
This command generates the necessary deployment manifest files, Docker file, and pipeline file required for deployment.
<br>

<h4><b4>Conclusion</h4></b4>
The Auto Ci-cd generator is an application that simplifies the process of deploying applications in Kubernetes and setting up pipelines. With just a few inputs, users can generate the necessary files required for deployment. Follow the installation steps to start using the Auto Ci-cd generator today!
