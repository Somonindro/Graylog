# Graylog: Log Management and SIEM Solution

## Overview: 
Graylog is a centralized Log Management System (LMS) to aggregate, organize, and make sense of data from various sources like devices, applications, and operating systems. It is on a mission to make Log Management and SIEM easier, faster, more affordable and more effective. Video demonstration of this project [here](https://youtu.be/ko7xcU1z02c)

## Mission: 
Graylog aims to simplify log management and SIEM, making it easier, faster, more affordable, and effective. The platform is purpose-built with a focus on providing efficient log management solutions.

## Security Solution: 
Graylog Security, built on the Graylog Enterprise Platform, promises traditional SIEM capabilities without complexity, alert fatigue, and high costs.

## Feature Demonstration:

###  1. Logging From Python

#### Step-1: Installing packages
You have to install logging gelf package by the command "pip install logging" in terminal.

####  Step-2: Setting up Input:
<p align="center">
    <img src="Images/Python_demo/setting_input.png?raw=true" width = "50%"/>
</p>

####  Step-3: Running the script:
python3 log_appdata.py

####  Step-4: Message Logged in Graylog:
You will see the following messages in Graylog:
<p align="center">
    <img src="Images/Python_demo/messages.png?raw=true" width = "50%"/>
</p>
The details of the message can also be shown. Details include name of the file, the line number , timestamp etc.
<p align="center">
    <img src="Images/Python_demo/message_detail.png?raw=true" width = "50%"/>
</p>

###  2. Raw PlainText TCP

#### Step-1: Setting up input:
<p align="center">
    <img src="Images/Raw_plaintext/input_settingup.png?raw=true" width = "50%"/>
</p>

#### Step-2: Opening Server:
<p align="center">
    <img src="Images/Raw_plaintext/server_listening.png?raw=true" width = "50%"/>
</p>

#### Step-3: Message Details:
<p align="center">
    <img src="Images/Raw_plaintext/message_details.png?raw=true" width = "50%"/>
</p>

###  3. Alert and Events
Events are conditions from log messages that can be used to show alerts and send notification via an email or remote server.

#### Step-1: Creating an Event:
Here we are creating an event and alert system to detect brute force attacks. If an user fails to log in 10 times under a minute, an event will be created.

<p align="center">
    <img src="Images/Alerts/event_details.png?raw=true" width = "50%"/>
</p>

<p align="center">
    <img src="Images/Alerts/event_filter.png?raw=true" width = "25%"/>
    <img src="Images/Alerts/event_def.png?raw=true" width = "25%"/>
</p>

<p align="center">
    <img src="Images/Alerts/event_summary.png?raw=true" width = "50%"/>
</p>

#### Step-2: Simulating brute force attack:
Running the script: python3 bruteforce_attack.py

#### Step-3: Event Log:
<p align="center">
    <img src="Images/Alerts/alert.png?raw=true" width = "50%"/>
</p>