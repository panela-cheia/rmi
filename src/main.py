import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

import Pyro5.socketutil
import Pyro5.server

Pyro5.config.SERVERTYPE = "thread"

# adapters
from adapters.users.login_user_adapter import LoginUserAdapter
from adapters.users.login_user_with_username_adapter import LoginUserWithUsernameAdapter
from adapters.users.create_user_adapter import CreateUserAdapter
from adapters.users.follow_user_adapter import FollowUserAdapter
from adapters.users.list_all_users_adapters import ListAllUsersAdapter
from adapters.users.list_others_users_adapter import ListOthersUsersAdapter
from adapters.users.search_in_users_barn_adapter import SearchInUsersBarnAdapter

from adapters.barn.save_recipe_adapter import SaveRecipeAdapter
from adapters.barn.search_recipe_adapter import SearchRecipeAdapter
from adapters.barn.remove_recipe_adapter import RemoveRecipeAdapter

from adapters.dive.create_dive_adapter import CreateDiveAdapter
from adapters.dive.enter_dive_adapter import EnterDiveAdapter
from adapters.dive.exit_dive_adapter import ExitDiveAdapter
from adapters.dive.list_dive_recipes_adapter import ListDiveRecipeAdapter
from adapters.dive.list_users_adapter import ListUsersAdapter
from adapters.dive.search_dive_adapter import SearchDiveAdapter
from adapters.dive.update_dive_adapter import UpdateDiveAdapter

from adapters.files.create_file_adapter import CreateFileAdapter
from adapters.files.delete_file_adapter import DeleteFileAdapter

from adapters.recipes.create_recipe_adapter import CreateRecipeAdapter
from adapters.recipes.list_recipe_adapter import ListRecipeAdapter
from adapters.recipes.reaction_recipe_adapter import ReactionRecipeAdapter
from adapters.recipes.search_recipe_adapter import SearchRecipeAdapter

if __name__ == "__main__":
    Pyro5.server.serve({
        CreateUserAdapter:"adapters.create_user_adapter",
        LoginUserAdapter: "adapters.user_login_login_adapter",
        LoginUserWithUsernameAdapter:"adapters.login_user_with_username_adapter",
        FollowUserAdapter: "adapters.follow_user_adapter",
        ListAllUsersAdapter:"adapters.list_all_users_adapters",
        ListOthersUsersAdapter:"adapters.list_others_users_adapter",
        SaveRecipeAdapter:"adapters.save_recipe_adapter",
        SearchRecipeAdapter:"adapters.search_recipe_adapter",
        RemoveRecipeAdapter:"adapters.remove_recipe_adapter",
        SearchInUsersBarnAdapter:"adapters.search_in_users_barn_adapter",
        CreateFileAdapter:"adapters.create_file_adapter",
        DeleteFileAdapter:"adapters.delete_file_adapter",
        CreateRecipeAdapter:"adapters.create_recipe_adapter",
        ListRecipeAdapter:"adapters.list_recipe_adapter",
        ReactionRecipeAdapter:"adapters.reaction_recipe_adapter",
        SearchRecipeAdapter:"adapters.search_recipe_adapter",
        CreateDiveAdapter:"adapters.create_dive_adapter",
        EnterDiveAdapter:"adapters.enter_dive_adapter",
        ExitDiveAdapter:"adapters.exit_dive_adapter",
        ListDiveRecipeAdapter:"adapters.list_dive_recipes_adapter",
        ListUsersAdapter:"adapters.list_users_adapter",
        SearchDiveAdapter:"adapters.search_dive_adapter",
        UpdateDiveAdapter:"adapters.update_dive_adapter"
    }, use_ns=True)