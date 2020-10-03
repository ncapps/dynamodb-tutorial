#! /usr/bin/env python

import boto3

dynamodb = boto3.client('dynamodb')

try:
    dynamodb.update_table(
        TableName='recipes',
        AttributeDefinitions=[
            {
                "AttributeName": "base",
                "AttributeType": "S"
            }
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "BaseSpiritIndex",
                    "KeySchema": [
                        {
                            "AttributeName": "base",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1
                    }
                }
            }
        ],
    )
    print("Table updated successfully.")
except Exception as e:
    print("Could not update table. Error:")
    print(e)
