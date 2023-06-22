import Pyro5.server
import Pyro5.socketutil

Pyro5.config.SERVERTYPE = "thread"

# adapters
from adapters.users.user_login_login_adapter import UserLoginAdapter

if __name__ == "__main__":
    Pyro5.server.serve({
        UserLoginAdapter:"adapters.user_login_login_adapter"
    },use_ns=True)