from modules.recipes.repositories.recipe_repository import RecipeRepository
from utils.serializator.recipe import recipeSerializator


class ListRecipesUseCase:
    def __init__(self, repository: RecipeRepository) -> None:
        self.repository = repository

    def execute(self):
        recipes = self.repository.findAll()
        # for recipe in recipes:
        #     print(recipe.__dict__)

        all_recipes = []

        for recipe in recipes:
            reactions = self.repository.getReactionQuantities(recipe_id=recipe.id)
            # print(reactions)
            recipe_formatted =  recipeSerializator(recipe=recipe,reactions=reactions)

            # all_recipes.append(recipe_formatted)

        # return all_recipes