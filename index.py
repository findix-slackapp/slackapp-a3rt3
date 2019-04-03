import json
import datetime


def handler(event, context):

    # SlackのEvent APIの認証
    if "challenge" in event:
        return event["challenge"]

    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
