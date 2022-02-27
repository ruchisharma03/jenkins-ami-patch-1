#!/bin/python3
import os
from jira.jira import JiraAPI
import sys
sys.path.append('.')

USERNAME = os.getenv('JIRA_USERNAME')
API_TOKEN = os.getenv("JIRA_API_TOKEN")


jira = JiraAPI(USERNAME, API_TOKEN, "config/jira.config.yaml")


print(jira.get_field_value_from_issue(["<fields>"], "<TICKET-NUMBER>"))
