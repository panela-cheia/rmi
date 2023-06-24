from Pyro5.api import Proxy

'''
test = Proxy("PYRONAME:adapters.follow_user_adapter")
result = test.execute(user_id="b5764f89-c00b-4b2d-b45f-f0782e14a99f",follow_id="78e519bb-a541-4a6a-af5d-398fc9c9e00f")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.list_all_users_adapters")
result = test.execute()
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.list_others_users_adapter")
result = test.execute(id="b5764f89-c00b-4b2d-b45f-f0782e14a99f")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.save_recipe_adapter")
result = test.execute(barnId="fef1b59f-db5a-46b3-8ba2-d306447c4b00", recipeId="b523820d-0973-4bf7-b39f-03778713925b")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.search_recipe_adapter")
result = test.execute(barnId="fef1b59f-db5a-46b3-8ba2-d306447c4b00", recipeName="dive-2")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.remove_recipe_adapter")
result = test.execute(barnId="fef1b59f-db5a-46b3-8ba2-d306447c4b00", recipeId="b523820d-0973-4bf7-b39f-03778713925b")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.login_user_with_username_adapter")
result = test.execute(username="@moviepapa",password="12345678")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.search_in_users_barn_adapter")
result = test.execute(user_id="6809d450-68e0-479f-91e1-7d2d5c52ad90",value="a")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.create_file_adapter")
result = test.execute(name="file.png",path="path")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.delete_file_adapter")
result = test.execute(id="b35351d4-70cf-41d2-b836-947ffd643d2c")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.create_recipe_adapter")
result = test.execute(name="dive-3",description="testar dive",userId="64542159-4fff-40ed-a22c-a3d0d5eb9196",fileId="7db5df5e-3835-4f34-94d8-12478b4bea64", diveId="d2066594-3c31-4342-b51a-ae2f20ea4683",
            ingredients=[
            {"name": "Ingredient 1", "amount": 1, "unit": "cup"},
            {"name": "Ingredient 2", "amount": 2, "unit": "teaspoon"},
            {"name": "Ingredient 3", "amount": 3, "unit": "gram"},
        ])
print(result)
'''


'''
test = Proxy("PYRONAME:adapters.list_recipe_adapter")
result = test.execute()
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.reaction_recipe_adapter")
result = test.execute(type="bão",recipe_id="b523820d-0973-4bf7-b39f-03778713925b",user_id="64542159-4fff-40ed-a22c-a3d0d5eb9196")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.search_recipe_adapter")
result = test.execute(name="d")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.save_recipe_adapter")
result = test.execute(barnId="fef1b59f-db5a-46b3-8ba2-d306447c4b00", recipeId="b523820d-0973-4bf7-b39f-03778713925b")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.search_recipe_adapter")
result = test.execute(barnId="fef1b59f-db5a-46b3-8ba2-d306447c4b00", recipeName="dive-2")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.remove_recipe_adapter")
result = test.execute(barnId="fef1b59f-db5a-46b3-8ba2-d306447c4b00", recipeId="b523820d-0973-4bf7-b39f-03778713925b")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.create_dive_adapter")
result = test.execute(name="But dos cria", description="Resenha", fileId="7db5df5e-3835-4f34-94d8-12478b4bea64", userId="b5764f89-c00b-4b2d-b45f-f0782e14a99f")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.enter_dive_adapter")
result = test.execute(userId="6809d450-68e0-479f-91e1-7d2d5c52ad90", diveId="d2066594-3c31-4342-b51a-ae2f20ea4683")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.exit_dive_adapter")
result = test.execute(user="b5764f89-c00b-4b2d-b45f-f0782e14a99f", new_owner="6809d450-68e0-479f-91e1-7d2d5c52ad90", diveId="d2066594-3c31-4342-b51a-ae2f20ea4683")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.list_dive_recipes_adapter")
result = test.execute(diveId="d2066594-3c31-4342-b51a-ae2f20ea4683")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.list_users_adapter")
result = test.execute(userId="64542159-4fff-40ed-a22c-a3d0d5eb9196")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.search_dive_adapter")
result = test.execute(diveName="But dos cria")
print(result)
'''

'''
test = Proxy("PYRONAME:adapters.update_dive_adapter")
result = test.execute(id="d2066594-3c31-4342-b51a-ae2f20ea4683", name="teste", fileId="", description="")
print(result)
'''