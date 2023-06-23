from modules.users.repositories.user_repository import UserRepository

from utils.serializator.users_all import serialize_user

class ListAllUsersUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    def execute(self):
        users = self.userRepository.findAll()

        serialized_users = [serialize_user(user) for user in users]

        return serialized_users