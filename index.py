import json
import logging
import urllib.request
import os
import pya3rt
import re

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    #getenv
    OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
    BOT_TOKEN = os.environ['BOT_TOKEN']
    HOOK_KEYWORD = os.environ['HOOK_KEYWORD']
    REPLY_WORD = os.environ['REPLY_WORD']
    BOT_NAME = os.environ['BOT_NAME']
    BOT_ID = os.environ['BOT_ID']
    A3RT_API_KEY = os.environ['A3RT_API_KEY']

    #受信したjsonをLogsに出力
    logging.info(json.dumps(event))

    print (type(event))
    # json処理
    if 'body' in event:
        body = json.loads(event.get('body'))
    elif 'token' in event:
        body = event
    else:
        logger.error('unexpected event format')
        return {'statusCode': 500, 'body': 'error:unexpected event format'}

    #url_verificationイベントに返す
    if 'challenge' in body:
        challenge = body.get('challenge')
        logging.info('return challenge key %s:', challenge)
        return {
            'isBase64Encoded': 'true',
            'statusCode': 200,
            'headers': {},
            'body': challenge
        }
    #SlackMessageに特定のキーワードが入っていたときの処理
    # if body.get('event').get('text') == HOOK_KEYWORD:
    m = re.match('<@%s>(.+)' % BOT_ID, body.get('event').get('text'))
    if m:
        logger.info('hit!: %s', HOOK_KEYWORD)
        url = 'https://slack.com/api/chat.postMessage'
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': 'Bearer {0}'.format(BOT_TOKEN)
        }
        data = {
            'token': OAUTH_TOKEN,
            'channel': body.get('event').get('channel'),
            'text': m.group(1),
            'username': BOT_NAME
        }
        # POST処理　
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), method='POST', headers=headers)
        res = urllib.request.urlopen(req)
        logger.info('post result: %s', res.msg)
        return {'statusCode': 200, 'body': 'ok'}
    return {'statusCode': 200, 'body': 'quit'}