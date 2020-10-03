#! /usr/bin/env python
import re

import boto3

from entities import Ingredient, RecipeIngredientMapping

dynamodb = boto3.client('dynamodb')

INGREDIENT = {"name": "Brandied Cherry", "type": "Garnish", "PK": "INGREDIENT#1091362f-3a34-4979-9c44-790807d703d6", "SK": "#METADATA#1091362f-3a34-4979-9c44-790807d703d6"}
INGREDIENT_ID =  re.match('(INGREDIENT#)(.+)', INGREDIENT['PK']).group(2)


def find_recipes_for_ingredient(ingredient):
    try:
        resp = dynamodb.query(
            TableName='recipes',
            IndexName='InvertedIndex',
            KeyConditionExpression="SK = :sk",
            ExpressionAttributeValues={
                ":sk": { "S": f"INGREDIENT#{ingredient}" }
            },
            ScanIndexForward=True
        )
    except Exception as e:
        print('Index is still backfilling. Please try again in a moment.')
        return None
    
    recipes = [RecipeIngredientMapping(item) for item in resp['Items']]
    return recipes


recipes = find_recipes_for_ingredient(INGREDIENT_ID)
if recipes:
    print(f"Recipes with {INGREDIENT['name']}")
    for recipe in recipes:
        print(recipe)
