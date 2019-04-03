import json
import datetime


def handler(event, context):

    # SlackのEvent APIの認証
    if "challenge" in event:
        return event["challenge"]
    
    return "OK"