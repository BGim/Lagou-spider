import pymysql
import time
import logging

class _Item(object):
    def __init__(self):
        super(_Item, self).__init__()
        self.host = 'localhost'
        self.usr = 'mg'
        self.passwd = '123'
        self.database = 'datas'
        # define the fields for your item here like:
        pass

    def connect_db(self):
        try:
            db = pymysql.connect(self.host, self.usr, self.passwd, self.database, charset='utf8')
        except Exception as e:
            logging.error(e)
            db.rollback()
        return db

    def insert_company(self, dbobject, *args):
        cursor = dbobject.cursor()
        sql = "INSERT INTO company VALUES ('%d','%s','%s','%s','%s','%s','%s','%s','%s')"\
              % (args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])
        # print('创建成功:%5s'%(sql))
        try:
            cursor.execute(sql)
        except Exception as e:
            sql = "INSERT INTO company VALUES ('%d','%s','%s','%s','%s','%s','%s','%s','%s')"\
              % (args[0],'None', 'None', 'None', 'None', 'None', 'None', 'None','None')
            cursor.execute(sql)
            logging.WARNING(e)
            logging.info('company插入空项目 companyid:%d'%(args[0]))
            dbobject.commit()
            dbobject.close()
        else:
            dbobject.commit()
            dbobject.close()
            #print("执行成功")

    def insert_work(self, dbobject, *args):
        cursor = dbobject.cursor()
        sql = "INSERT INTO work VALUES ( '%d','%s','%s','%s','%d','%s','%s','%s','%s','%s')"\
              % (args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9])
        # print('创建成功:%5s'%(sql))
        try:
            cursor.execute(sql)
        except Exception as e:
            sql = "INSERT INTO work VALUES ( '%d','%s','%s','%s','%d','%s','%s','%s','%s','%s')"\
              % (args[0],'None', 'None', 'None', args[4], 'None', 'None', 'None','None','None')
            cursor.execute(sql)
            logging.WARNING(e)
            logging.info('work插入空项目 positionid:%d'%(args[0]))
            dbobject.commit()
            dbobject.close()
        else:
            dbobject.commit()
            dbobject.close()
            #print("执行成功")

    def insert_employment(self, dbobject, *args):
        cursor = dbobject.cursor()
        sql = "INSERT INTO employment VALUES ( '%d','%d','%s')" % (args[0], args[1], args[2])
        # print('创建成功:%5s'%(sql))
        try:
            cursor.execute(sql)
        except Exception as e:
            sql = "INSERT INTO employment VALUES ( '%d','%d','%s')" % (args[0], args[1], 'None')
            cursor.execute(sql)
            logging.WARNING(e)
            logging.info('employment插入空项目 companyid:%d,positionid:%d'%(args[0],args[1]))
            dbobject.commit()
            dbobject.close()
        else:
            dbobject.commit()
            dbobject.close()
            #print("执行成功")
