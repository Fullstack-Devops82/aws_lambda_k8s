from __future__ import print_function

import os
import json
import urllib
import requests
import boto3
from botocore.exceptions import ClientError

    
def executeStepFunction(event, context):

    ### Launch three Pods ###

    #url = 'http://127.0.0.1:8080/api/v1/namespaces/default/pods'
    #payloadCalTwoNum = open("calculatetwonumber.json")
    #payloadDyFirstMsg = open("displayfirstmessage.json")
    #payloadDySecondMsg = open("displaysecondmessage.json")
    #headers = {'content-type': 'application/json', 'Accept': 'application/json'}

    #requests.post(url, data=payloadCalTwoNum, headers=headers)
    #requests.post(url, data=payloadDyFirstMsg, headers=headers)
    #requests.post(url, data=payloadDySecondMsg, headers=headers)


    ### Get all events from K8S ###

    #url = 'http://127.0.0.1:8080/api/v1/events'
    #response = requests.post(url, headers=headers)


    ### Call State Machines ###
    numberOne = event['queryStringParameters']['numberOne']
    numberTwo = event['queryStringParameters']['numberTwo']
    
    stateMachineName = 'SequenceNumActivityMachine'
    stepFunction = boto3.client('stepfunctions')
    state_machines = stepFunction.list_state_machines()
    message = 'Step function not is executing'
    
    try:
        if state_machines.get('stateMachines'):
            for sm in state_machines.get('stateMachines'):
                if sm['name'] == stateMachineName:
                    stepFunction.start_execution(stateMachineArn=sm['stateMachineArn'], input=json.dumps({ numberOne: numberOne, numberTwo: numberTwo }))
                    message = 'Step function is executing'
            
        body = {
            "message": message,
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except ClientError as e:
        body = {
            "message": e.response['Error']['Code'],
            "input": event
        }

        response = {
            "statusCode": 400,
            "body": json.dumps(body)
        }

    return response
    

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def ExecuteErrorInExecution(event, context):

    logger.info("Starting ExecuteErrorInExecution ...")
    logger.info(event)

    # activity = "arn:aws:states:us-east-2:912778368198:activity:calculateTwoNumber"
    # stepFunction = boto3.client('stepfunctions')
    # task = stepFunction.get_activity_task(activityArn=activity, workerName="CalculateTwoNumberNext")
    # taskToken=task['taskToken']

    # response = stepFunction.send_task_failure(
    #     taskToken=taskToken,
    #     error='task token fail ...',
    #     cause='dont know the reason'
    # )

    err_resp = {
        "statusCode": 'event error',
        "body": 'event cause'
    }
    return err_resp
