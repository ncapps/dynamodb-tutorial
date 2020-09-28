class Ingredient:

    def __init__(self, item):
        self.name = item.get('name').get('S')
        self.type = item.get('type').get('S')
        self.category = item.get('category', "").get('S')
        self.style = item.get('style', "").get('S')

    def __repr__(self):
        
        return f"Ingredient<{self.name} -- {self.type}>"


class Recipe:

    def __init__(self, item):
        self.name = item.get('name').get('S')
        self.base = item.get('base').get('S')
        self.mix_method = item.get('mix_method').get('S')
        self.glassware = item.get('glassware').get('S')
        self.directions = item.get('directions', {}).get('S')

    def __repr__(self):
        return f"Recipe<{self.name} -- {self.base} -- {self.mix_method}>"


class RecipeIngredientMapping:

    def __init__(self, item):
        self.name = item.get('name').get('S')
        self.amount = item.get('amount', "").get('S')
        self.unit = item.get('unit', "").get('S')

    def __repr__(self):
        return f"RecipeIngredientMapping<{self.name} -- {self.amount} {self.unit}>"