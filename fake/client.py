from Pyro5.api import Proxy
import asyncio

test = Proxy("PYRONAME:adapters.user_login_login_adapter")
result = test.execute(email="teste@gmail.com", password="12345678")
print(result)
