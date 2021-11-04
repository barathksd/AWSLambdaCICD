import json
import boto3

def lambda_handler(event, context):

	deploymentId = event['DeploymentID']
	exID = event['LifecycleEventHookExecutionId']
	client = boto3.client('codedeploy')
	
	# Lambda function status confirmation
	# ...
	
	client.put_lifecycle_event_hook_execution_status(deploymentId=deploymentId,lifecycleEventHookExecutionId=exID,status='Succeeded')
    return {
        'statusCode': 200,
        'body': json.dumps('')
    }