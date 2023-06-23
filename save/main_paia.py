from save.orm import ORM
from src.modules.recipes.repositories.recipe_repository import RecipeRepository

orm = ORM()

session = orm.get_session()

# Crie uma instância do RecipeRepository
repository = RecipeRepository()

# Chame a função findAll e imprima os resultados
recipes = repository.create(session=session)

for recipe in recipes:
    print(recipe.name)

# Feche a sessão
session.close()
