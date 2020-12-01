
# 1. 오라클 접속정보
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'pythonTest' #enter your username
PASSWORD = '1234' #enter your password
HOST = 'localhost' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
SERVICE = 'pythonTest' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

# 2. 두부 연결을 위한 engine 생성 - lazy connecting
from sqlalchemy import create_engine
engine = create_engine(ENGINE_PATH_WIN_AUTH)


# 3. Mapping Class
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import Table, MetaData

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" \
               % (self.name, self.fullname, self.nickname)

# print(User.__table__) 메타데이터 확인
# print(User.__mapper__) 매퍼 클래스 확인

Base.metadata.create_all(engine)

# # 인스턴스 생성
# ed_user = Userinfo(name='ed', fullname='Ed Jones', nickname='ednickname')
#
#
# # 세션생성, 2에서 생성한 engine
# from sqlalchemy.orm import sessionmaker
# # engine을 아직 생성하지 않은 경우 Session = sessionmaker()
# Session = sessionmaker(bind=engine)
#
# # 두부와 연결을 해야할 때 인스턴트화를 한다.
# session = Session()
#
# # Insert 또는 Update
# session.add(ed_user)