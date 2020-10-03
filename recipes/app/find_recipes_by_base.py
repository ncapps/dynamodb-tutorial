#! /usr/bin/env python

import boto3

from entities import Recipe

dynamodb = boto3.client('dynamodb')

BASE_SPIRIT = "Gin"

def find_recipes_by_base(base_spirit):
    resp = dynamodb.query(
        TableName='recipes',
        IndexName="BaseSpiritIndex",
        KeyConditionExpression="#base = :base",
        ExpressionAttributeNames={
            "#base": "base"
        },
        ExpressionAttributeValues={
            ":base": { "S": base_spirit },
        },
        ScanIndexForward=True
    )

    recipes = [Recipe(item) for item in resp['Items']]

    return recipes

recipes = find_recipes_by_base(BASE_SPIRIT)
print(f"Recipes that use {BASE_SPIRIT}")
for recipe in recipes:
    print(recipe)
