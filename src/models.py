import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey, Integer
from eralchemy2 import render_er
from typing import List
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=False)
    password: Mapped[str] = mapped_column(String(30),nullable=False)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(nullable=True)
    character_race: Mapped[str] = mapped_column(nullable=True)
    character_age: Mapped[str] = mapped_column(nullable=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(nullable=True)
    planet_climate: Mapped[str]
    planet_url: Mapped[str] = mapped_column(nullable=False)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    vehicle_name: Mapped[str]
    vehicle_url: Mapped[str]


class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(nullable=True)
    character_race: Mapped[str] = mapped_column(nullable=True)
    character_age: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'), nullable=False)
    parent: Mapped["Characters"] = relationship(back_populates="users")


class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(nullable=True)
    planet_climate: Mapped[str] = mapped_column(nullable=True)
    planet_url: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'), nullable=False)
    parent: Mapped["Planets"] = relationship(back_populates="users")


class FavoriteVehicles(Base):
    __tablename__ = 'favorite_vehicle'
    id: Mapped[int] = mapped_column(primary_key=True)
    vehicle_name: Mapped[str] = mapped_column(nullable=True)
    vehicle_url: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicle.id'), nullable=False)
    parent: Mapped["Vehicle"] = relationship(back_populates="users")
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')