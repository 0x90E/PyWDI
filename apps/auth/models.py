from apps.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType


class User(Base):
    __tablename__ = 'user'
    privilege_level_choices=(
        (0, 'admin'),
        (1, 'developer'),
        (2, 'analyst'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    # TODO: need email checker
    email = Column(String(120), unique=True)
    password = Column(String(50))
    privilege = (ChoiceType(privilege_level_choices, Integer()))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
