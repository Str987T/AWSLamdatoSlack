import urllib3
import json

http = urllib3.PoolManager()

def lambda_handler(event, context):
    url = "https://hooks.slack.com/services/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"
    
    msgtype = event['Records'][0]['Sns']['Type']
    msgid = event['Records'][0]['Sns']['MessageId']
    msgsubject = event['Records'][0]['Sns']['Subject']
    msgtimestamp = event['Records'][0]['Sns']['Timestamp']
    msgbody = event['Records'][0]['Sns']['Message']
    
    _message = "============================\n" \
               "\nNotification Type: *{}*" \
               "\nMessage ID: *{}*" \
               "\nSubject: *{}*" \
               "\nTime: *{}*" \
               "\nNotification: *{}*" \
               "\n============================"
    
    message = _message.format(
        msgtype,
        msgid,
        msgsubject,
        msgtimestamp,
        msgbody
    )
    
    body = {'username': 'AWS Alerts', 'text': message}
    
    headers = {'Content-type': 'application/json'}
    
    resp = http.request('POST', url, body=json.dumps(body).encode('utf-8'), headers=headers)
    
    print({
        "message": event['Records'][0]['Sns']['Message'], 
        "status_code": resp.status, 
        "response": resp.data
    })
