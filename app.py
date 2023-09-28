# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/9/28 14:36
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

URI = "mysql+pymysql://root:123456@127.0.0.1:3306/flas_demo?charset=utf8mb4"

engine = create_engine(URI, echo=False)
session = scoped_session(sessionmaker(engine))


class MySqlManager:

    def __init__(self, database):
        self.database = database
        session.execute(text(f"USE {database}"))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close()

    def __enter__(self):
        return self

    @staticmethod
    def __close():
        session.remove()

    @staticmethod
    def query(sql):
        result = session.execute(text(sql)).fetchall()
        for n in result:
            print(n)


if __name__ == '__main__':
    with MySqlManager("edr") as manager:
        manager.query("select * from alembic_version")

    with MySqlManager("flas_demo") as manager:
        manager.query("select * from user")
