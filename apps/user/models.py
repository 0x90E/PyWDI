from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType
from werkzeug.security import generate_password_hash, check_password_hash


from apps.database import database_manager, Base

class User(Base):
    __tablename__ = 'user'
    privilege_level_choices=(
        (0, 'admin'),
        (1, 'developer'),
        (2, 'analyst'),
    )

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    # TODO: need email checker
    email = Column(String(120), unique=True)
    password = Column(String(512))
    privilege = (ChoiceType(privilege_level_choices, Integer()))
    login_time = Column(Integer)

    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email
        super(User, self).__init__()

    def __repr__(self):
        return '<User %r>' % (self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add(self, User):
        db_session = database_manager.get_db_session()
        db_session.add(User)
        db_session.commit()

    def update(self):
        db_session = database_manager.get_db_session()
        db_session.commit()

    def get(self, id):
        return self.query.filter_by(id=id).first()
