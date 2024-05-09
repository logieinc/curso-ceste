<br >![ Screenshot of the empty token dialog box ](../assets/images/logo-ceste.png)

### AWS Lambda & S3

  ```python
    import json
    import boto3
    
    s3 = boto3.client('s3')
    
    def lambda_handler(event, context):
        bucket ='mycestebucket'
    
        transactionToUpload = {}
        transactionToUpload['transactionId'] = '12345'
        transactionToUpload['type'] = 'PURCHASE'
        transactionToUpload['amount'] = 20
        transactionToUpload['customerId'] = 'CID-11111'
    
        fileName = 'CID-11111' + '.json'
    
        uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))
    
        s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)
    
        print('Write completado...')
   ```

### AWS Lambda & DynamoDB

  ```python
    import json
    import boto3
    
    def lambda_handler(event, context):
        
        client_dynamodb = boto3.client('dynamodb')
        
        # Inser
        client_dynamodb.put_item(
                        TableName='CesteDynamoDB',
                        Item={
                                'id' : { 'S': '5'},
                                'first_name' : { 'S' : 'Maria' },
                                'last_name' : { 'S' : 'Gonzalez' }
                        })
                        
                        
        # Find    
        response = client_dynamodb.get_item(
                        TableName='CesteDynamoDB', 
                        Key={
                            'id' : { 'S' : '5' }
                        }
                    )
        
        print(response)
                   
    
        # Update
        client_dynamodb.update_item(
                        TableName='CesteDynamoDB', 
                        Key={"id": { 'S' : '5' }},
                        UpdateExpression="set last_name=:ln",
                        ExpressionAttributeValues={":ln": { 'S' : "Garcia"}},
                        ReturnValues="UPDATED_NEW",
                    )  
        
        # Delete        
        client_dynamodb.delete_item(                       
                       TableName='CesteDynamoDB', 
                       Key={
                           'id' : { 'S' : '53333' }
                       }
                   )
    
        
        return {
            'statusCode': 200,
            'body': json.dumps('DynamoDB Ok!')
        }   
   ```

### Codigo AWS API Gateway WebSocket (Implementación chat)

   **IDE Test Web Socket :** https://piehost.com/websocket-tester

    { 
        "action: "sendMessage",
        "message" "Hola, hay alguien alli"
    }
    Route selection expresion -> request.body.action

   ```python
    # Connect & Disconnect

    import json
    
    def lambda_handler(event, context):
        print(event)
        print("-" * 80)
        print(context)
        return { "statusCode" : 200}
    
    
    # SendMessage - Needs AmazonAPIGatewayInvokeFullAccess IAM Policy
    import json
    import urllib3
    import boto3
    
    client = boto3.client('apigatewaymanagementapi', endpoint_url="xxxxxxxxxx.com/production")
    
    def lambda_handler(event, context):
        print(event)
        
        #Extract connectionId from incoming event
        connectionId = event["requestContext"]["connectionId"]
        
        #Do something interesting... 
        responseMessage = "responding..."
        
        #Form response and post back to connectionId
        response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(responseMessage).encode('utf-8'))
        return { "statusCode": 200  }
    
    
    # Broadcast - Needs AmazonAPIGatewayInvokeFullAccess IAM Policy
    import json
    import urllib3
    import boto3
    
    client = boto3.client('apigatewaymanagementapi', endpoint_url="xxxxxx.com/production")
    
    def lambda_handler(event, context):
        
        #Extract connectionId and desired message to send from input
        connectionId = event["connectionId"]
        message = event["message"]
        
        #Form response and post back to provided connectionId
        response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(message).encode('utf-8'))
        print(response)
        
    # Broadcast Lambda Input Event Example
    #{
    #  "connectionId": "FUVNdckkIAMCIZw=",
    #  "message": "Anyone out there?"
    #}
   ```