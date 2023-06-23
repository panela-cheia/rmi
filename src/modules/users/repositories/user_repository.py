from save.orm import ORM
from save.schema import User, Barn, Follows, UsersDive

class UserRepository:
    def __init__(self):
        self.orm = ORM()
    
    def create(self, name, username, email, password):
        session = self.orm.get_session()

        user = User(name=name, username=username, email=email, password=password)
        session.add(user)
        session.commit()

        barn = Barn(user_id=user.id)
        session.add(barn)
        session.commit()

        session.close()

        return user

    def findAll(self):
        session = self.orm.get_session()

        users = session.query(User).all()

        session.close()

        return users

    def findByEmail(self, email):

        session = self.orm.get_session()

        user = session.query(User).filter(User.email == email).first()

        session.close()

        return user

    def findByUsername(self, username):

        session = self.orm.get_session()

        user = session.query(User).filter(User.username == username).first()

        session.close()

        return user

    def findById(self, id):

        session = self.orm.get_session()

        user = session.query(User).filter(User.id == id).first()

        session.close()

        return user

    def update(self, id, name, username, bio):

        session = self.orm.get_session()

        user = session.query(User).filter(User.id == id).first()
        user.name = name
        user.username = username
        user.bio = bio
        session.commit()

        session.close()

        return user

    def updatePhoto(self, id, photo):

        session = self.orm.get_session()

        user = session.query(User).filter(User.id == id).first()
        user.photo = photo
        session.commit()

        session.close()

        return user

    def delete(self, id):

        session = self.orm.get_session()

        user = session.query(User).filter(User.id == id).first()
        session.delete(user)
        session.commit()

        session.close()

        return user

    def verifyFollowing(self, follower, following):

        session = self.orm.get_session()

        follows = session.query(Follows).filter(Follows.followerId == follower, Follows.followingId == following).first()

        session.close()

        return follows is not None

    def followUser(self, user_id, follow_id):

        session = self.orm.get_session()

        follow = Follows(followerId=user_id, followingId=follow_id)
        session.add(follow)
        session.commit()

        session.close()

        return follow

    def deleteFollow(self, user_id, unfollow_id):

        session = self.orm.get_session()

        session.query(Follows).filter(Follows.followerId == user_id, Follows.followingId == unfollow_id).delete()
        session.commit()

        session.close()

    def findOther(self, id):

        session = self.orm.get_session()

        users = session.query(User).filter(User.id != id).all()

        session.close()

        return users

    def searchUser(self, user_id, value):

        session = self.orm.get_session()

        users = session.query(User).filter(
            (User.name.contains(value) | User.username.contains(value)) & (User.id != user_id)
        ).all()

        results = []

        for user in users:
            common_followers = session.query(Follows).filter(Follows.followingId == user_id, Follows.followerId == user.id).count()
            common_dives = session.query(UsersDive).filter(
                UsersDive.userId == user_id,
                UsersDive.diveId.in_([users_dive.diveId for users_dive in user.usersDive])
            ).count()

            result = {
                "user": user,
                "common_followers": common_followers,
                "common_dives": common_dives
            }

            results.append(result)

        session.close()

        return results