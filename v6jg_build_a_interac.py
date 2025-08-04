# Configuration file for Interactive Automation Script Notifier

# Notification Settings
NOTIFICATION_TITLE = "Automation Script Alert"
NOTIFICATION_MESSAGE = "New script execution completed successfully!"

# Email Settings
EMAIL_SUBJECT = "Automation Script Notification"
EMAIL_BODY = "A new automation script has been executed successfully. Please find details below:\n\nScript Name: {}\nExecution Time: {}\nStatus: {}"
EMAIL_RECIPIENTS = ["admin@example.com", "dev@example.com"]
EMAIL_SERVER = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "username"
EMAIL_PASSWORD = "password"

# Automation Script Settings
SCRIPT_NAME = "My Automation Script"
SCRIPT_EXECUTION_INTERVAL = 30  # minutes
SCRIPT_EXECUTION_LOG_FILE = "script_execution_log.txt"

# Interactive Settings
INTERACTIVE_PROMPT = "Do you want to execute the automation script now? (yes/no)"
INTERACTIVE_YES_RESPONSE = "yes"
INTERACTIVE_NO_RESPONSE = "no"

# Logging Settings
LOG_FILE = "automation_script_notifier.log"
LOG_LEVEL = "INFO"

# Import Modules
import os
import time
import smtplib
from email.mime.text import MIMEText
import logging