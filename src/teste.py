import sys
import os

# Obtenha o caminho absoluto do diretório que contém o arquivo main.py
current_dir = os.path.dirname(os.path.abspath(__file__))
#Adicione o diretório acima ao sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from modules.users.repositories.user_repository import UserRepository
from modules.files.repositories.files_repository import FilesRepository

userRepository = UserRepository()
filesRepository = FilesRepository()

'''
1) create

userRepository.create(
    name="João da Silva",
    username="@joaodasilva",
    email="joao.da.silva@gmail.com",
    password="12345678"
)

2) findall
users = userRepository.findAll()

for user in users:
    for barn in user.barn:
        barn_id = barn.id
        print(barn_id)

users = userRepository.findAll()


for user in users:
    if user.photo:
        print(f"User: {user.name}")
        print(f"Photo ID: {user.photo.id}")
        print(f"Photo Filename: {user.photo.name}")
        print(f"Photo Path: {user.photo.path}")
        print()
    else:
        print(f"User {user.name} has no photo.")
        


3) findByEmail

user = userRepository.findByEmail('joao.da.silva@gmail.com')
if user:
    for barn in user.barn:
        barn_id = barn.id
        print(barn_id)
else:
    print('Usuário não encontrado')


4) findByUsername

user = userRepository.findByUsername("@joaodasilva")

if user:
    print(user.__dict__)
else:
    print('Usuário não encontrado')

    
5) findById

user = userRepository.findById("38982c9e-c4bd-4396-8a38-e15a6390ad69")

if user:
    print(user.__dict__)
else:
    print('Usuário não encontrado')

6) update

update = userRepository.update(
        id="38982c9e-c4bd-4396-8a38-e15a6390ad69",
        name="João da Silva",
        username="@joaodasilva",
        bio="macarrão é bão dmais!"
    )

print(update.__dict__)

7) delete
delete = userRepository.delete(id="38982c9e-c4bd-4396-8a38-e15a6390ad69")
print(delete)


8) followUser

follow =  userRepository.followUser(
    user_id="5ea14993-ec3b-4ec3-8e7f-5c8e2f77b04b",
    follow_id="59ef9f90-f7fe-4f8e-ad65-2a85af97aa2d")

print(follow)


9) deleteFollow = unfollow

unfollow =  userRepository.deleteFollow(
    user_id="5ea14993-ec3b-4ec3-8e7f-5c8e2f77b04b",
    unfollow_id="59ef9f90-f7fe-4f8e-ad65-2a85af97aa2d")

print(unfollow)

10) verifyFollowing

verifyFollowing = userRepository.verifyFollowing(
    follower="5ea14993-ec3b-4ec3-8e7f-5c8e2f77b04b",
    following="59ef9f90-f7fe-4f8e-ad65-2a85af97aa2d")
print(verifyFollowing)


11) findOther

users = userRepository.findOther(id="5ea14993-ec3b-4ec3-8e7f-5c8e2f77b04b")

for user in users:
    print(user.id)

12) searchUser

searchUser = userRepository.searchUser(user_id="5ea14993-ec3b-4ec3-8e7f-5c8e2f77b04b",value="M")

for user in searchUser:
    print(user['user'].name)


13) updatePhoto

updateUserPhoto = userRepository.updatePhoto(
    id="7e43f882-b014-43a6-8d9d-54500c3b4fc6",photo_id="52ab7b64-2c87-406d-bff7-ec336bd2b538"
)

print(updateUserPhoto)

'''

'''
File

1) create
create = filesRepository.create(name="a",path="a")
print(create)'''