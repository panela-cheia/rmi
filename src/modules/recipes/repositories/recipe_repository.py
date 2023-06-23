from schema import Barn, Recipe, Ingredients, Reaction
from orm import ORM
from src.modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO

from sqlalchemy.orm import joinedload

class RecipeRepository:
    def create(self, session: ORM, data: CreateRecipeDTO):
        recipe = Recipe(
            name=data.name,
            description=data.description,
            userId=data.userId,
            diveId=data.diveId,
            fileId=data.fileId
        )

        ingredients = [
            Ingredients(name=ingredient.name, amount=ingredient.amount, unit=ingredient.unit)
            for ingredient in data.ingredients
        ]
        recipe.ingredients = ingredients

        session.add(recipe)
        session.commit()
        session.refresh(recipe)

        return recipe

    def findAll(self, session: ORM):
        recipes = session.query(Recipe).\
            options(joinedload(Recipe.barn), joinedload(Recipe.dive),
                    joinedload(Recipe.ingredients), joinedload(Recipe.photo),
                    joinedload(Recipe.reactions), joinedload(Recipe.user)).\
            order_by(Recipe.created_at.desc()).all()

        return recipes

    def search(self, session: ORM, name: str):
        recipes = session.query(Recipe).\
            options(joinedload(Recipe.barn), joinedload(Recipe.dive),
                    joinedload(Recipe.ingredients), joinedload(Recipe.photo),
                    joinedload(Recipe.reactions), joinedload(Recipe.user)).\
            filter(Recipe.name.ilike(f'%{name}%')).all()

        return recipes

    def verify_existing_reaction(self, session: ORM, recipe_id: str, user_id: str):
        existing_reaction = session.query(Reaction).\
            filter(Reaction.recipeId == recipe_id, Reaction.userId == user_id).first()

        return existing_reaction

    def reaction(self, session: ORM, recipe_id: str, type: str, user_id: str):
        reaction = Reaction(type=type, recipeId=recipe_id, userId=user_id)

        session.add(reaction)
        session.commit()
        session.refresh(reaction)

        return reaction

    def updateReaction(self, session: ORM, id: str, type: str):
        reaction = session.query(Reaction).get(id)
        reaction.type = type

        session.commit()

        return reaction

    def getReactionQuantities(self, session: ORM, recipe_id: str):
        reaction_quantities = {
            "bão": 0,
            "mió de bão": 0,
            "água na boca": 0
        }

        try:
            recipe_reactions = session.query(Reaction).filter(Reaction.recipeId == recipe_id).all()

            for reaction in recipe_reactions:
                if reaction.type in reaction_quantities:
                    reaction_quantities[reaction.type] += 1
        except Exception as e:
            # Lidar com exceção de consulta
            print(e)

        return reaction_quantities
