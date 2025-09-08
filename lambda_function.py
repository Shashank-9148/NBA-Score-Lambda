import os
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    api_key = os.environ['API_KEY']
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']
    date = datetime.now().strftime("%Y-%m-%d")

    url = f"https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        games = response.json()

        messages = []
        for game in games:
            if game.get('Status') == 'Final':
                home = game.get('HomeTeam')
                away = game.get('AwayTeam')
                home_score = game.get('HomeTeamScore')
                away_score = game.get('AwayTeamScore')
                messages.append(f"{home} {home_score} - {away} {away_score}")

        if messages:
            sns = boto3.client('sns')
            sns.publish(
                TopicArn=sns_topic_arn,
                Message="\n".join(messages),
                Subject="NBA Final Scores"
            )
            return {"statusCode": 200, "body": "Scores sent successfully."}
        else:
            return {"statusCode": 200, "body": "No final scores yet."}
    
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
