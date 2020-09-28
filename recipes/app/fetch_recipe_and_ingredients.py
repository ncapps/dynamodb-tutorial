#! /usr/bin/env python

import boto3

from entities import Recipe, RecipeIngredientMapping

dynamodb = boto3.client('dynamodb')

RECIPE_ID = "1fb91e23-a7d8-4e38-9b5c-5010497beb67" # Aviation

def fetch_recipe_and_ingredients(recipe_id):
    resp = dynamodb.query(
        TableName='recipes',
        KeyConditionExpression="PK = :pk AND SK BETWEEN :metadata AND :ingredients",
        ExpressionAttributeValues={
            ":pk": { "S": "RECIPE#{}".format(recipe_id) },
            ":metadata": { "S": "#METADATA#{}".format(recipe_id) },
            ":ingredients": { "S": "INGREDIENT$" },
        },
        ScanIndexForward=True
    )

    recipe = Recipe(resp['Items'][0])
    recipe.ingredients = [RecipeIngredientMapping(item) for item in resp['Items'][1:]]
    return recipe


recipe = fetch_recipe_and_ingredients(RECIPE_ID)

print(recipe)
for ingredient in recipe.ingredients:
    print(ingredient)

