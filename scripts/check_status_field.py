#!/bin/python3
import os
import sys
sys.path.append('.')

from jira.jira import JiraAPI


USERNAME = os.getenv('JIRA_USERNAME')
API_TOKEN = os.getenv("JIRA_API_TOKEN")

TICKET_NUMBER = os.getenv('JIRA_TICKET_NUMBER')
FIELD_PATH = os.getenv('FIELD_PATH').split(',')

jira = JiraAPI(USERNAME, API_TOKEN, "config/jira.config.yaml")


field =jira.get_field_value_from_issue(FIELD_PATH, TICKET_NUMBER)
field_name,field_value = field.strip("{").strip("}").split(",")[0].split(":")
print(field_value.lstrip('"').rstrip('"').strip())