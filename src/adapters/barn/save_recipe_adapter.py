import json
import Pyro5.server
from constants.topics import Topics
from loguru import logger

# repository
from modules.barn.repositories.barn_repository import BarnRepository

# useCase
from modules.barn.useCases.save_recipe import SaveRecipeUseCase, BarnSaveRecipeDTO

@Pyro5.server.expose
class SaveRecipeAdapter(object):
    def __init__(self) -> None:
        self.useCase = SaveRecipeUseCase(repository=BarnRepository())
    
    def execute(self, barnId: str, recipeId: str):
        dto = BarnSaveRecipeDTO(
            barnId=barnId,
            recipeId=recipeId
        )
        
        user = self.useCase.execute(data=dto)
        
        if "error" in user:
            logger.error("{topic} - {user}", topic=Topics.BARN_SAVE_RECIPE.value, user=json.dumps(user, indent=4, ensure_ascii=False))
        else:
            logger.info("{topic} - {user}", topic=Topics.BARN_SAVE_RECIPE.value, user=json.dumps(user, indent=4, ensure_ascii=False))
            
        return user