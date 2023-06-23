from save.orm import ORM
from modules.dive.dtos.create_dive_dto import CreateDiveDTO
from modules.dive.dtos.update_dive_dto import UpdateDiveDTO
from save.schema import Dive, User, UsersDive


class DiveRepository:
    def __init__(self):
        self.orm = ORM()

    def create(self, data: CreateDiveDTO):
        session = self.orm.get_session()
        
        dive = Dive(
            name=data.name,
            description=data.description,
            fileId=data.fileId,
            ownerId=data.userId
        )

        session.add(dive)
        session.commit()

        return dive

    def findById(self, id):
        session = self.orm.get_session()
        user = session.query(User).filter_by(id=id).first()

        return user

    def findDiveById(self, dive_id):
        session = self.orm.get_session()
        dive = session.query(Dive).filter_by(id=dive_id).first()

        return dive

    def findDiveByName(self, name):
        session = self.orm.get_session()
        dive = session.query(Dive).filter_by(name=name).first()

        return dive

    def verifyEntry(self, user: str, dive: str) -> bool:
        session = self.orm.get_session()
        values = session.query(UsersDive).filter_by(userId=user, diveId=dive).first()

        return values is not None

    def enterDive(self, user_id: str, dive_id: str):
        session = self.orm.get_session()
        user_dive = UsersDive(userId=user_id, diveId=dive_id)

        session.add(user_dive)
        session.commit()

        return user_dive

    def exitDive(self, user_id: str, dive_id: str):
        session = self.orm.get_session()
        session.query(UsersDive).filter_by(userId=user_id, diveId=dive_id).delete()
        session.commit()

    def update(self, updateDiveDTO: UpdateDiveDTO):
        session = self.orm.get_session()
        dive = session.query(Dive).filter_by(id=updateDiveDTO.id).first()
        dive.description = updateDiveDTO.description
        dive.fileId = updateDiveDTO.fileId
        dive.name = updateDiveDTO.name

        session.commit()

        return dive

    def findAll(self, name: str):
        session = self.orm.get_session()
        dives = session.query(Dive).filter(Dive.name.contains(name)).all()

        return dives

    def updateDiveOwner(self, dive_id: str, new_owner: str):
        session = self.orm.get_session()
        dive = session.query(Dive).filter_by(id=dive_id).first()
        dive.ownersDive = new_owner

        session.commit()

        return dive

    def findUserDive(self, user_id):
        session = self.orm.get_session()
        dives = session.query(UsersDive).filter_by(userId=user_id).all()

        return dives
