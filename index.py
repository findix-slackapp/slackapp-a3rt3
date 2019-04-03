import json
import datetime
from urllib.parse import parse_qs

def handler(event, context):

    query = parse_qs(event.get('body') or '')

    # SlackのEvent APIの認証
    challenge = query.get('challenge', [''])[0]
    if challenge:
        return challenge

    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
