import json
import Pyro5.server
from constants.topics import Topics
from loguru import logger

# repository
from modules.barn.repositories.barn_repository import BarnRepository

# useCase
from modules.barn.useCases.remove_recipe import RemoveRecipeUseCase, RemoveRecipeDTO

@Pyro5.server.expose
class RemoveRecipeAdapter(object):
    def __init__(self) -> None:
        self.useCase = RemoveRecipeUseCase(repository=BarnRepository())
    
    def execute(self, barnId: str, recipeId: str):
        dto = RemoveRecipeDTO(
            barnId=barnId,
            recipeId=recipeId
        )
        
        user = self.useCase.execute(data=dto)
        
        if "error" in user:
            logger.error("{topic} - {user}", topic=Topics.BARN_REMOVE_RECIPE.value, user=json.dumps(user, indent=4, ensure_ascii=False))
        else:
            logger.info("{topic} - {user}", topic=Topics.BARN_REMOVE_RECIPE.value, user=json.dumps(user, indent=4, ensure_ascii=False))
            
        return user