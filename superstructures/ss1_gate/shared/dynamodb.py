
import boto3
from boto3.dynamodb.conditions import Key
import os

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('LandTena')

def write_user_profile(email, persona):
    table.put_item(Item={
        "email": email,
        "persona": persona
    })
