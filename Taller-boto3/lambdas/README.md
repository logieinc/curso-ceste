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

### Codigo AWS DynamoDB Streams to Lambda

    Crear tabla DynamDb GameEvents id, sort = date

    { 
        "playerId: "9c8eee7a",
        "date" "Aug 10 2024 19:20:05",
        "gameRoundId" : 125949494,
        "score" : 75
    }

   ```python
        import json
        
        print('Loading function')
        
        def lambda_handler(event, context):
            print('------------------------')
            print(event)
            #1. Iterate over each record
            try:
                for record in event['Records']:
                    #2. Handle event by type
                    if record['eventName'] == 'INSERT':
                        handle_insert(record)
                    elif record['eventName'] == 'MODIFY':
                        handle_modify(record)
                    elif record['eventName'] == 'REMOVE':
                        handle_remove(record)
                print('------------------------')
                return "Success!"
            except Exception as e: 
                print(e)
                print('------------------------')
                return "Error"
        
        
        def handle_insert(record):
            print("Handling INSERT Event")
            
            #3a. Get newImage content
            newImage = record['dynamodb']['NewImage']
            
            #3b. Parse values
            newPlayerId = newImage['playerId']['S']
        
            #3c. Print it
            print ('New row added with playerId=' + newPlayerId)
        
            print("Done handling INSERT Event")
        
        def handle_modify(record):
            print("Handling MODIFY Event")
        
            #3a. Parse oldImage and score
            oldImage = record['dynamodb']['OldImage']
            oldScore = oldImage['score']['N']
            
            #3b. Parse oldImage and score
            newImage = record['dynamodb']['NewImage']
            newScore = newImage['score']['N']
        
            #3c. Check for change
            if oldScore != newScore:
                print('Scores changed - oldScore=' + str(oldScore) + ', newScore=' + str(newScore))
        
            print("Done handling MODIFY Event")
        
        def handle_remove(record):
            print("Handling REMOVE Event")
        
            #3a. Parse oldImage
            oldImage = record['dynamodb']['OldImage']
            
            #3b. Parse values
            oldPlayerId = oldImage['playerId']['S']
        
            #3c. Print it
            print ('Row removed with playerId=' + oldPlayerId)
        
            print("Done handling REMOVE Event")
   ```

    INSERT 
   ```python
    {
       "Records":[
          {
             "eventID":"361a4b288c96554a1a793e8be931907f",
             "eventName":"INSERT",
             "eventVersion":"1.1",
             "eventSource":"aws:dynamodb",
             "awsRegion":"us-east-1",
             "dynamodb":{
                "ApproximateCreationDateTime":1715796571.0,
                "Keys":{
                   "date":{
                      "S":"Aug 10 2024 19:20:05"
                   },
                   "id":{
                      "S":"9c8eee7a"
                   }
                },
                "NewImage":{
                   "date":{
                      "S":"Aug 10 2024 19:20:05"
                   },
                   "id":{
                      "S":"9c8eee7a"
                   }
                },
                "SequenceNumber":"36100000000045250299058",
                "SizeBytes":68,
                "StreamViewType":"NEW_AND_OLD_IMAGES"
             },
             "eventSourceARN":"arn:aws:dynamodb:us-east-1:381492044272:table/GameEvents/stream/2024-05-15T17:37:26.310"
          }
       ]
    }
   ```

    MODIFY 
   ```python
    {
       "Records":[
          {
             "eventID":"bd21cb50328e6c03e87775a106cd1547",
             "eventName":"MODIFY",
             "eventVersion":"1.1",
             "eventSource":"aws:dynamodb",
             "awsRegion":"us-east-1",
             "dynamodb":{
                "ApproximateCreationDateTime":1715796757.0,
                "Keys":{
                   "date":{
                      "S":"Aug 10 2024 19:20:05"
                   },
                   "id":{
                      "S":"9c8eee7a"
                   }
                },
                "NewImage":{
                   "date":{
                      "S":"Aug 10 2024 19:20:05"
                   },
                   "score":{
                      "N":"75"
                   },
                   "gameRoundId":{
                      "N":"125949494"
                   },
                   "id":{
                      "S":"9c8eee7a"
                   }
                },
                "OldImage":{
                   "date":{
                      "S":"Aug 10 2024 19:20:05"
                   },
                   "id":{
                      "S":"9c8eee7a"
                   }
                },
                "SequenceNumber":"36200000000045250515902",
                "SizeBytes":126,
                "StreamViewType":"NEW_AND_OLD_IMAGES"
             },
             "eventSourceARN":"arn:aws:dynamodb:us-east-1:381492044272:table/GameEvents/stream/2024-05-15T17:37:26.310"
          }
       ]
    }
   ```

    DELETE 
   ```python
        {
           "Records":[
              {
                 "eventID":"e5f425af08b9fc2b50db2eda65e363ae",
                 "eventName":"REMOVE",
                 "eventVersion":"1.1",
                 "eventSource":"aws:dynamodb",
                 "awsRegion":"us-east-1",
                 "dynamodb":{
                    "ApproximateCreationDateTime":1715796892.0,
                    "Keys":{
                       "date":{
                          "S":"Aug 10 2024 19:20:05"
                       },
                       "id":{
                          "S":"9c8eee7a"
                       }
                    },
                    "OldImage":{
                       "date":{
                          "S":"Aug 10 2024 19:20:05"
                       },
                       "score":{
                          "N":"75"
                       },
                       "gameRoundId":{
                          "N":"125949494"
                       },
                       "id":{
                          "S":"9c8eee7a"
                       }
                    },
                    "SequenceNumber":"36300000000045250668648",
                    "SizeBytes":92,
                    "StreamViewType":"NEW_AND_OLD_IMAGES"
                 },
                 "eventSourceARN":"arn:aws:dynamodb:us-east-1:381492044272:table/GameEvents/stream/2024-05-15T17:37:26.310"
              }
           ]
        }
   ```

### Codigo AWS SNS:

   ```python
    import json
    
    print('Loading function')
    
    
    def lambda_handler(event, context):
        #print("Received event: " + json.dumps(event, indent=2))
        message = event['Records'][0]['Sns']['Message']
        print("From SNS: " + message)
        return message
   ```





