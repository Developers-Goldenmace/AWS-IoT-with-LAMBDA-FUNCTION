from __future__ import print_function  
import json
import boto3
print('Loading function')
def lambda_handler(event, context):
    # Parse the JSON message 
    eventText = json.dumps(event)
  
    # Print the parsed JSON message to the console; you can view this text in the Monitoring tab in the Lambda console or in the CloudWatch Logs console
    print('Received event: ', eventText)
      # Create an SNS client
    sns = boto3.client('sns') 
    # Publish a message to the specified topic
    response = sns.publish (
      TopicArn = 'arn:aws:sns:topic_for_sns',
      Message = eventText
    )
    client = boto3.client('iot-data')
    #Change topic, qos and payload
    response = client.publish(
      topic='sample_topic21',
   #note: 
      qos=0,
      payload=eventText
)
    print(response)  
