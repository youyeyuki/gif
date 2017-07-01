from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode


class mysqlconnect:
    def __init__(self, config):
        # database 初始化
        try:
            self.cnx = mysql.connector.connect(**config)  # 尝试连接
            self.cursor = self.cnx.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

    def create_database(self, database):
        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
            print("Create database {}  successful".format(database))
            self.cnx.database = database  # 建立完成后选择数据库
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print("{} already exist!".format(database))
                self.cnx.database = database  # 存在时候也要选择数据库
                pass
            else:
                print("Failed creating database: {}".format(err))
                exit(1)

    def create_tables(self, tables):
        for name, ddl in tables.items():
            try:
                print("Creating table {}: ".format(name), end='')
                self.cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def insert_data(self, add_sql, data_dict):
        try:
            self.cursor.execute(add_sql, data_dict)
        except mysql.connector.Error as err:
            print(err)

    def query(self, query_sql):
        try:
            self.cursor.execute(query_sql)
        except mysql.connector.Error as err:
            print(err)

    def close(self):
        try:
            self.cursor.close()
            self.cnx.close()
        except mysql.connector.Error as err:
            print(err)


########################