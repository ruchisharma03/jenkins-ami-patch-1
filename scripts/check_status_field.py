#!/bin/python3 
import sys 
sys.path.append('.')
from jira.jira import JiraAPI

jira = JiraAPI('https://<domain>.atlassian.net',
               '<username>', '<api_token>',"config/jira.config.yaml")

print(jira.get_field_value_from_issue(["<fields>"],"<TICKET-NUMBER>"))