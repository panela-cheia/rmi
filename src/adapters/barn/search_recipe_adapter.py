import json
import Pyro5.server
from constants.topics import Topics
from loguru import logger

# repository
from modules.barn.repositories.barn_repository import BarnRepository

# useCase
from modules.barn.useCases.search_recipe import SearhRecipeUseCase, SearchRecipeInBarnDTO

@Pyro5.server.expose
class SearchRecipeAdapter(object):
    def __init__(self) -> None:
        self.useCase = SearhRecipeUseCase(repository=BarnRepository())

    def execute(self, barnId: str, recipeName: str):
        dto = SearchRecipeInBarnDTO(
            barnId=barnId,
            recipeName=recipeName
        )
        
        user = self.useCase.execute(data=dto)
        
        if "error" in user:
            logger.error("{topic} - {user}", topic=Topics.BARN_SEARCH_RECIPE.value, user=json.dumps(user, indent=4, ensure_ascii=False))
        else:
            logger.info("{topic} - {user}", topic=Topics.BARN_SEARCH_RECIPE.value, user=json.dumps(user, indent=4, ensure_ascii=False))
            
        return user