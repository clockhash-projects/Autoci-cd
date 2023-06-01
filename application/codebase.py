import os
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--code', help="Path to code directory")
parser.add_argument('--version', action='version', version='1.0')



        
args = parser.parse_args()



directory = args.code

def codecheck():
    # Check for Node.js code
    if any(f.endswith(('.js')) for f in os.listdir(directory)):
        with open(os.path.join(directory, 'package.json'), 'r') as f:
            package_json = json.load(f)
            if 'express' in package_json['dependencies']:
                code = 'nodejs'
                return code

    # Check for React code
    if any(f.endswith(('.js')) for f in os.listdir(directory)):
        with open(os.path.join(directory, 'package.json'), 'r') as f:
            package_json = json.load(f)
            if 'react' in package_json['dependencies']:
                code = 'react'
                return code

    # Check for Python code
    if any(f.endswith('.py') for f in os.listdir(directory)):
        code = 'python'
        return code

    # Check for Flask code
    if any(f.endswith('.py') for f in os.listdir(directory)):
        with open(os.path.join(directory, "requirements.txt"), "r") as f:
            requirements = f.read()
        if "Flask" in requirements:
            code = "flask"
            return code
        else:
            print("Error: Requirements file not found")
            return None

    # Check for Django code
    if any(f.endswith('.py') for f in os.listdir(directory)):
        with open(os.path.join(directory, "requirements.txt"), "r") as f:
            requirements = f.read()
        if "Django" in requirements:
            code = "django"
            return code
        else:
            print("Error: Requirements file not found")
            return None

    # Check for Angular code
    if any(f.endswith(('.ts', '.html')) for f in os.listdir(directory)):
        code = "angular"
        return code

    # Check for Java code
    if any(f.endswith('.java') for f in os.listdir(directory)):
        code = "java"
        return code

    # Check for Laravel code
    if any(f.endswith('.php') for f in os.listdir(directory)):
        with open(os.path.join(directory, "composer.json"), "r") as f:
            composer_json = f.read()
        if "laravel/framework" in composer_json:
            code = "laravel"
            return code

codecheck()

