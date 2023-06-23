from modules.barn.dtos.search_recipe_in_barn_dto import SearchRecipeInBarnDTO
from modules.barn.repositories.barn_repository import BarnRepository

from utils.serializator.recipe_without_reactions import recipeWithoutReactionsSerializator

class SearhRecipeUseCase:
    def __init__(self, repository: BarnRepository):
        self.repository = repository

    def execute(self, data: SearchRecipeInBarnDTO):
        barns =  self.repository.findAll(barnId=data.barnId)
        # print(barns)
        if barns is None:
            return []
        
        recipes = []

        for recipe in barns.recipes:
            recipes.append(recipeWithoutReactionsSerializator(recipe=recipe))

        return recipes