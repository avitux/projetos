import json
import boto3

def lambda_handler(event, context):
    try:
        comprehend = boto3.client('comprehend')
        
        body = json.loads(event['body'])
        text = body['Texto']
        response = comprehend.classify_document(
            Text=text,
            EndpointArn='arn:aws:comprehend:eu-west-1:014498643574:document-classifier-endpoint/ClassificarTexto'
        )
    except Exception as error:
        return {'statusCode': 500, 'body': { 'error': str(error), 'text': text } }

    return {'statusCode': 200, 'body': response}