import json
import datetime
from urllib.parse import parse_qs

def handler(event, context):

    # json処理
    if 'body' in event:
        body = json.loads(event.get('body'))
    elif 'token' in event:
        body = event
    else:
        logger.error('unexpected event format')
        return {'statusCode': 500, 'body': 'error:unexpected event format'}

    # SlackのEvent APIの認証
    if 'challenge' in body:
        challenge = body.get('challenge')
        return {
            'isBase64Encoded': 'true',
            'statusCode': 200,
            'headers': {},
            'body': challenge
        }

    data = {
        'output': 'hellow',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
