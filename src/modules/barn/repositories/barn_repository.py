from schema import Barn, Recipe
from orm import ORM

from modules.barn.dtos.save_recipe_dto import BarnSaveRecipeDTO
from modules.barn.dtos.remove_recipe_dto import RemoveRecipeDTO



class BarnRepository:

    def save(self, session: ORM, data: BarnSaveRecipeDTO):
        barn = session.get_session.query(Barn).filter_by(id=data.barnId).first()
        recipe = session.get_session.query(Recipe).filter_by(id=data.recipeId).first()

        barn.recipes.append(recipe)
        session.commit()

        return barn

    def findAll(self, session: ORM, barnId: str):
        barn = session.get_session.query(Barn).filter_by(id=barnId).first()
        return barn

    def removeRecipe(self, session: ORM, data: RemoveRecipeDTO):
        barn = session.get_session.query(Barn).filter_by(id=data.barnId).first()
        recipe = session.get_session.query(Recipe).filter_by(id=data.recipeId).first()

        barn.recipes.remove(recipe)
        session.commit()

        return barn