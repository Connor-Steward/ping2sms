# ping2sms
Alert System for PingPlotter Pro

# What is ping2sms?
ping2sms is a program I created to ensure our team was alerted 24/7 on any outages on our network. When using Pingplotter Pro,
if a network device or sensor goes offline emails are sent to preconfigured addresses. 

The issue? What if nobody is in the office or checking their emails? That's why I created ping2sms! When critical devices stop responding to pings, ping2sms sends a text message SMS alert to everyone on the team. 

Our internal IT team used ping2sms for ~6 months until we moved to another monitoring system with more built-in functionality.

# How does it work?
ping2sms runs as a cronjob/scheduled task on a server everyone 1 minute (can be run more frequently if need be). It scans the mailbox of a service account for an alert email from Pingplotter, if found the info is scraped and sent via SMS (using the Twilio API) to all team members mobile phones. 
