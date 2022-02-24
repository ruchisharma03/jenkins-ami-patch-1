#!/bin/python3 
import sys 
sys.path.append('.')
from jira.jira import JiraAPI

jira = JiraAPI('https://<domain>.atlassian.net',
               '<username>', '<api_token>',"config/jira.config.yaml")

jira.create_issue()