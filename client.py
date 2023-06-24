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
test = Proxy("PYRONAME:adapters.login_user_with_username_adapter")
result = test.execute(username="@moviepapa",password="12345678")
print(result)
'''

test = Proxy("PYRONAME:adapters.search_in_users_barn_adapter")
result = test.execute(user_id="6809d450-68e0-479f-91e1-7d2d5c52ad90",value="a")
print(result)