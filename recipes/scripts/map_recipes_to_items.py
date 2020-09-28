#! /usr/bin/env python
'''
**Primary Key Design**
Entity Hash | HASH | RANGE
--- | --- | ---
Ingredient | INGREDIENT#<INGREDIENT_ID> | #METADATA#<INGREDIENT_ID>
Recipe | RECIPE#<RECIPE_ID> | #METADATA#<RECIPE_ID>
RecipeIngredientMapping | RECIPE#<RECIPE_ID> | INGREDIENT#<INGREDIENT_ID>

example:
{"PK": "GAME#0ab37cf1-fc60-4d93-b72b-89335f759581", "SK": "USER#hshort", "username": "hshort", "game_id": "0ab37cf1-fc60-4d93-b72b-89335f759581"}
'''

import json
from uuid import uuid4


def format_recipe(recipe):
    recipe_item = recipe.copy()
    recipe_item.pop('ingredients', False)
    recipe_id = uuid4()
    recipe_item['PK'] = f'RECIPE#{recipe_id}'
    recipe_item['SK'] = f'#METADATA#{recipe_id}'
    return recipe_item


def format_ingredient(ingredient):
    an_ingredient = ingredient.copy()
    ingredient_id = uuid4()
    an_ingredient.pop('amount', False)
    an_ingredient.pop('unit', False)
    an_ingredient['PK'] = f'INGREDIENT#{ingredient_id}'
    an_ingredient['SK'] = f'#METADATA#{ingredient_id}'
    return an_ingredient


with open('scripts/recipes.json', 'rt') as in_fh, open('scripts/items.json', 'wt') as out_fh:
    recipes = json.load(in_fh)
    unique_ingredients = {}
    

    for recipe in recipes:
        recipe_item = format_recipe(recipe)
        out_fh.write(f'{json.dumps(recipe_item)}\n')
        for ingredient in recipe['ingredients']:
            ing_name = ingredient['name']
            if not unique_ingredients.get(ing_name, False):
                new_ingredient = format_ingredient(ingredient)
                unique_ingredients[ing_name] = new_ingredient

            recipe_ingredient_map = {
                'PK': recipe_item['PK'],
                'SK': unique_ingredients[ing_name]['PK'],
                'amount': ingredient.get('amount', 0),
                'unit': ingredient.get('unit', None)
            }
            out_fh.write(f'{json.dumps(recipe_ingredient_map)}\n')
        
            
    for ingredient_item in unique_ingredients.values():
        out_fh.write(f'{json.dumps(ingredient_item)}\n')
