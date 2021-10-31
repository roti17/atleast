from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
  __tablename__ = 'movies'
  id = Column(Integer, primary_key = True)
  pic_link = Column(String)
  director = Column(String)
  movie_name = Column(String)
  release_year = Column(String)
  price = Column(Float)
  description=Column(String)
