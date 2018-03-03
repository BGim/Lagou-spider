#! /usr/bin/env python
# -*-coding:utf-8-*-

import pymysql


def connect():
    try:
        db = pymysql.connect("localhost", 'mg', '123', 'datas')
    except pymysql.Error as e:
        raise e

    return db

def create_table(arg,*args):
    cursor = arg.cursor()
    sql="""
          CREATE TABLE `occupation` (
              `id` int(11) DEFAULT NULL,
              `city` varchar(10) DEFAULT NULL,
              `PositionName` varchar(20) DEFAULT NULL,
              `positionId` INT (20) DEFAULT NULL ,
              `isSchoolJob` INT (2) DEFAULT NULL , 
              `FirstType` VARCHAR (20) DEFAULT NULL ,
              `SecondType` VARCHAR (20) DEFAULT NULL ,
              `workYear` varchar(10) DEFAULT NULL,
              `companyFullName` varchar(20) DEFAULT NULL,
              `companyShortName` VARCHAR (10) DEFAULT NULL ,
              `companyId` INT (10) DEFAULT NULL ,
              `industryField` varchar(30) DEFAULT NULL,
              `education` varchar(10) DEFAULT NULL,
              `salary` varchar(10) DEFAULT NULL,
              `jonNature` varchar(10) DEFAULT NULL,
              `financeStage` varchar(10) DEFAULT NULL,
              `positionLables` varchar(30) DEFAULT NULL,
              `companySize` varchar(10) DEFAULT NULL,
              `positionAdvantage` varchar(100) DEFAULT NULL,
              `Longitude` varchar(30) DEFAULT NULL ,
              `latitude` VARCHAR (30) DEFAULT NULL ,
              `Keyword` varchar(10) DEFAULT NULL,
              `createTime` VARCHAR (20) DEFAULT NULL 
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            """
    try:
        cursor.execute(sql)
        arg.commit()
    except pymysql.Error as e:
        raise e


if __name__ == '__main__':
    create_table(connect())
    
