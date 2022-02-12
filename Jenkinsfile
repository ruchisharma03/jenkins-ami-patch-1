pipeline{
agent any

stages{

stage('build a job'){
    
    steps{
        withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding',
            credentialsId: "aws-creds",
            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
            ]]) {
            // AWS Code
            sh script:'''#!/bin/python3
            
            import boto3 
from os import getenv 

REGIONS = getenv('REGIONS') # list of regions separated by commas
SERVICE_NAME = getenv('SERVICE_NAME') # service name 
FILTERS = getenv('FILTERS') # 
 
boto3_clients = [] #list of boto3 clients

output = {} # store the output 


def get_latest_ami_version(client):
    print(client.describe_images())


def check_ami_version_from_lc(client):
    print(client.describe_launch_configurations())

            
def compare_ami_versions(first_ami,second_ami):
    return first_ami == second_ami 



if REGIONS:
        for each_region in REGIONS.split(','):
            boto3_clients.append(boto3.client('ec2',region_name=each_region))

# for each client , execute the follow sequence of code
for each_client in boto3_clients:
    latest_ami_version = get_latest_ami_version(each_client)
    service_ami_version  = check_ami_version_from_lc(each_client)
    if service_ami_version:
        print(compare_ami_versions(service_ami_version,latest_ami_version))




            
            
            '''
        
        
        }
    }
}
}

}