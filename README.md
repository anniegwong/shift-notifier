# HotSchedules Shift Notifier
Python script to check if there are any available shifts in HotSchedules (SaaS in hospitality and service industry) and send email to specified recipients.

## Setup
config.py requires 6 inputs:
- HSusername: employee's HotSchedules username
- HSpassword: employee's HotSchedules password
- sender: gmail to send notifications
- recipients: list of email notification recipients
- gmail_user: username of gmail to send notifications
- gmail_password: password of gmail to send notifications

### Notes
- Make sure sender email has "Less secure app access" on for the Google Account
- Designed to run with Windows Task Scheduler to check for new available shifts periodically.
