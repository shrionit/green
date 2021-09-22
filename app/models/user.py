from sqlalchemy import Column, String, Integer, Date

from app.utils.dbbase import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
    
    def __str__(self):
        return f'User(name={self.name}, email={self.email})'