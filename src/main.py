import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

import Pyro5.socketutil
import Pyro5.server

Pyro5.config.SERVERTYPE = "thread"

# adapters
from adapters.users.user_login_login_adapter import UserLoginAdapter
from adapters.users.create_user_adapter import CreateUserAdapter
from adapters.users.follow_user_adapter import FollowUserAdapter
from adapters.users.list_all_users_adapters import ListAllUsersAdapter
from adapters.users.list_others_users_adapter import ListOthersUsersAdapter
from adapters.barn.save_recipe_adapter import SaveRecipeAdapter
from adapters.barn.search_recipe_adapter import SearchRecipeAdapter
from adapters.barn.remove_recipe_adapter import RemoveRecipeAdapter

if __name__ == "__main__":
    Pyro5.server.serve({
        CreateUserAdapter:"adapters.create_user_adapter",
        UserLoginAdapter: "adapters.user_login_login_adapter",
        FollowUserAdapter: "adapters.follow_user_adapter",
        ListAllUsersAdapter:"adapters.list_all_users_adapters",
        ListOthersUsersAdapter:"adapters.list_others_users_adapter",
        SaveRecipeAdapter:"adapters.save_recipe_adapter",
        SearchRecipeAdapter:"adapters.search_recipe_adapter",
        RemoveRecipeAdapter:"adapters.remove_recipe_adapter"
    }, use_ns=True)