import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import cx_Oracle

# 오라클 접속정보
host = 'pythonTest'
port = '1521'
sid = 'xe'
user = 'pythonTest'
password = '1234'
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user = user
    , password = password
    , sid = sid
)
# 두부 연결을 위한 engine 생성
engine = create_engine(
    cstr
    , convert_unicode=False
    , pool_recycle = 10
    , pool_size = 50
    , echo = True
)

Base = declarative_base()

class Person(Base):
    # 테이블명을 지정한다
    __tablename__ = 'person'

    # 컬럼정의, 기본키 지정
    id = Column(Integer, primary_keyu= True)

    # 일반적인 컬럼 정의
    name = Column(String(250), nullable=False)

metadata = MetaData()
address = Table('address', metadata,
    Column('street_name', String(250)),
    Column('street_member' String(250)),
    Column('post_code', String(250), nullable = False))
# class Address(Base):
#     # 테이블명을 지정한다
#     __tablename__ = 'address'
#
#     # 컬럼을 정의, 기본키 지정
#     id = Column(Integer, primary_key=True)
#
#     # 그외 일반적인 컬럼 정의
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable+False)
#
#     # 외래키를 지정한다
#     person_id = Column(Integer, ForeignKey('person.id'))
#
#     # 외래키로 참조하는 테이블과의 관계를 기술
#     person = relationship(Person)
#
#     # engine 생성<-- 데이터를 저장함
#     engine = create_engine('oracle://localhost:1521/xe')