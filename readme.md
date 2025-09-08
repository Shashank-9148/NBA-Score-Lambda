# NBA Game Day Real-Time Alert System

This project sends **live NBA game scores** to subscribed users via **SMS or Email** using AWS services.  
It works like your own **sports notification bot in the cloud** .

---

## Features
- Fetches live NBA scores from [SportsData.io](https://sportsdata.io/) API  
- AWS Lambda processes and formats the scores  
- Notifications sent via **Amazon SNS** (SMS/Email)  
- Automated scheduling using **Amazon EventBridge**  
- Secure handling of API keys using **Lambda Environment Variables**  
- Code stored in GitHub for version control  

---

##  Architecture

```mermaid
flowchart TD
    A[NBA API (sportsdata.io)] --> B[AWS Lambda]
    B --> C[Amazon SNS]
    C --> D[Subscribers (SMS/Email)]
    E[Amazon EventBridge] --> B
