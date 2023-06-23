from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import uuid
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    bio = Column(String)

    photo_id = Column(String, ForeignKey('files.id'))
    photo = relationship("File")

    barn = relationship("Barn")

    followers = relationship("Follows", back_populates="follower", foreign_keys='Follows.follower_id')
    following = relationship("Follows", back_populates="following", foreign_keys='Follows.following_id')

    recipes = relationship("Recipe")
    users_dive = relationship("UsersDive")
    owners_dive = relationship("Dive", back_populates="owner")
    reactions = relationship("Reaction")

class Follows(Base):
    __tablename__ = 'follows'

    follower_id = Column(String, ForeignKey('users.id'), primary_key=True)
    follower = relationship("User", foreign_keys='Follows.follower_id', back_populates="followers")
    following_id = Column(String, ForeignKey('users.id'), primary_key=True)
    following = relationship("User", foreign_keys='Follows.following_id', back_populates="following")

class Dive(Base):
    __tablename__ = 'dives'

    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True)
    description = Column(String)

    owner_id = Column(String, ForeignKey('users.id'))
    owner = relationship("User", back_populates="owners_dive")

    members = relationship("UsersDive")
    recipe = relationship("Recipe")

    photo_id = Column(String, ForeignKey('files.id'))
    photo = relationship("File")

class UsersDive(Base):
    __tablename__ = 'users_dive'

    id = Column(String, primary_key=True, default=uuid.uuid4)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship("User")
    dive_id = Column(String, ForeignKey('dives.id'))
    dive = relationship("Dive")

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    description = Column(String)

    user_id = Column(String, ForeignKey('users.id'))
    user = relationship("User")

    barn_id = Column(String, ForeignKey('barns.id'))
    barn = relationship("Barn")

    dive_id = Column(String, ForeignKey('dives.id'))
    dive = relationship("Dive")

    photo_id = Column(String, ForeignKey('files.id'))
    photo = relationship("File")

    reactions = relationship("Reaction")
    ingredients = relationship("Ingredients")

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

class Ingredients(Base):
    __tablename__ = 'ingredients'

    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    amount = Column(Integer)
    unit = Column(String)

    recipe_id = Column(String, ForeignKey('recipes.id'))
    recipe = relationship("Recipe")

class Reaction(Base):
    __tablename__ = 'reactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)

    recipe_id = Column(String, ForeignKey('recipes.id'))
    recipe = relationship("Recipe")

    user_id = Column(String, ForeignKey('users.id'))
    user = relationship("User")

class Barn(Base):
    __tablename__ = 'barns'

    id = Column(String, primary_key=True, default=uuid.uuid4)

    user_id = Column(String, ForeignKey('users.id'), unique=True)
    user = relationship("User", back_populates="barn")

    recipes = relationship("Recipe")

class File(Base):
    __tablename__ = 'files'

    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    path = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    users = relationship("User")
    recipe = relationship("Recipe")
    dive = relationship("Dive")

class IngredientsUnit(Base):
    __tablename__ = 'ingredients_units'

    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True)
