import json
import openai
import boto3
import os
import yaml
import atexit
import argparse
from codebase import codecheck 
from github import Github
import gitlab
import base64

username = input("Enter your username for your registry: ")
password = input("Enter your password for your registry: ")


encoded_password = base64.b64encode(password.encode())

with open('clockhash.yml', 'r') as f:
    config = yaml.safe_load(f)

config['registry']['password'] = encoded_password.decode()
config['registry']['username'] = username

with open('clockhash.yml', 'w') as f:
    yaml.dump(config, f)




def parse():
    headers = {
        "Content-Type": "application/json"
    }

    with open('clockhash.yml', 'r') as f:

        data = yaml.safe_load(f)

        if data['repo'] == 'github':
             with open(data['kubeconfig-file'], 'r') as f:
                      kubeconfig = f.read()

             token = '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'
             g = Github(token)
             repo = g.get_repo('avinash2632/dockernginx')
             repo.create_secret('KUBECONFIG', kubeconfig)
             repo.create_secret('USERNAME',data['registry']['username'])
             repo.create_secret('PASSWORD',data['registry']['password'])


        if data['repo'] == 'gitlab':
             with open(data['kubeconfig-file'], 'r') as f:
                      kubeconfiggitlab = f.read()

             gl = gitlab.Gitlab('https://gitlab.com/', private_token='glpat-VKT4JY4B46hrxqYZoBbH')
             project_id = 26849616
             variable_key = 'KUBE'
             username_key = 'USERNAME'
             password_key = 'PASSWORD'
             usernamevalue = data['registry']['username']
             passwordvalue = data['registry']['password']
             variable_value = kubeconfiggitlab
             protected = True

             project = gl.projects.get(project_id)
             variable = project.variables.create({'key':variable_key, 'value':variable_value, 'protected':protected})
             passw = project.variables.create({'key':password_key, 'value':passwordvalue, 'protected':protected})
             userw = project.variables.create({'key':username_key, 'value':usernamevalue, 'protected':protected})

             

            
        if 'codebase' not in data:
            codebase = codecheck();
            data['codebase'] = codebase

            with open('clockhash.yml', 'w') as f:
                yaml.dump(data, f, default_flow_style=False)
        jsondata = json.dumps(data)
        return jsondata

def lambda_handler(event):

    model_to_use = "text-davinci-003"
    input_prompt1 = f"provide basic docker file for {event['codebase']}"
    openai.api_key = os.environ["OPENAI_API_KEY"]
    response1 = openai.Completion.create(
      model=model_to_use,
      prompt=input_prompt1,
      temperature=0,
      max_tokens=2200,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )




    output = response1['choices'][0]['text']
    
    with open('Dockerfile', 'w') as f:


         f.write(output)



    model_to_use2 = "text-davinci-003"
    input_prompt2 = f"generate full {event['repo']} ci/cd pipeline file  for {event['codebase']} application to deploy on kubernetes cluster and also assume that the docker image has to be build along with this pipeline with the dockerfile from the repo and while deploying to kubernetees cluster use the KUBE variable secret for storing cluster details"
    response2 = openai.Completion.create(
      model=model_to_use2,
      prompt=input_prompt2,
      temperature=0,
      max_tokens=3200,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )


    output2 = response2['choices'][0]['text']
    finaloutput2 = output2.replace("KUBE_SECRET", "KUBE").replace("gitlab-ci-token", "$USERNAME").replace("$CI_JOB_TOKEN", "$PASSWORD")
        
    with open('pipeline.yml', 'w') as f:


         f.write(finaloutput2)


    model_to_use3 = "text-davinci-003"
    input_prompt3 = f"provide kubernetes manifests file for deploying {event['codebase']} application to kubernetes cluster"
    response3 = openai.Completion.create(
      model=model_to_use3,
      prompt=input_prompt3,
      temperature=0,
      max_tokens=2200,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )


    output3 = response3['choices'][0]['text']

    with open('deployment.yml', 'w') as f:


         f.write(output3)


def prompt():
    print("Docker file, Deployment file and Pipeline file for your application  has been generated")


parsed_data = parse()
event = json.loads(parsed_data)
lambda_handler(event)
atexit.register(prompt)



def main():
    parser = argparse.ArgumentParser(description="Autocicd Command Line Utility")
    
    parser.add_argument('--code', help="Path to code directory")
    parser.add_argument('--generate', help="Generate the password;")
    args = parser.parse_args()



if __name__ == '__main__':
    main()


