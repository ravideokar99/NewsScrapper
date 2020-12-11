#!/usr/bin/env python
# coding: utf-8
import cx_Oracle as oracle
class ConnectToOracle():
    def __init__(self,conn_str="RAVI/9833504978@localhost/orcl"):
        self._conn_str=conn_str
        self._connect_oracle()
        self.cur=self._cursor
    def _connect_oracle(self):
        self._connection=oracle.connect(self._conn_str)
        self._cursor= self._connection.cursor()
    def insert_data(self,table_name,data_list):
        st=""
        l=[]
        for data in data_list:
            if isinstance(data,str)==True and "TO_DATE" not in data:
                l.append("'"+data+"'")
            elif isinstance(data,int)==True or isinstance(data,float)==True or "TO_DATE" in data:
                l.append(str(data))
            else:
                raise ValueError(f"Invalid data type {data}")
        st=",".join(l)
        query="""INSERT INTO {} VALUES({})""".format(table_name,st)
        #print(query)
        self._cursor.execute(query)
        self._connection.commit()
    def create_table(self,query):
        """Create's a table in database using query as input use " " at the beginning and end of the query

        SYNTAX: CREATE TABLE TABLE_NAME COLUMN_NAME COLUMN_DATA_TYPE"""
        query=query
        self._cursor.execute(query)
        self._connection.commit()
    def drop_table(self,table_name):
        """Drop The table form the DataBase
        
        table_name- The Table Name from the Database will be dropped """
        query="""DROP TABLE {}""".format(table_name)
        self._cursor.execute(query)
        self._connection.commit()
    def delete_value(self,table_name,condition_attribute,condition_value):
        """ Delete's a value from the Table
        
         table_name- The Table name from the Database from where you want to Delete the value
         condition_attribute- The column name from where you want to delete the value 
         condition_value- The value you want you to delete from the table
         SYNTAX: DELETE FROM TABLE_NAME WHERE CONDITIONAL_ATTRIBUTE=CONDITIONAL_VALUE"""
        query="""DELETE FROM {} WHERE {}={}""".format(table_name,condition_attribute,condition_value)
        self._cursor.execute(query)
        self._connection.commit()
    def delete_all(self,table_name):
        """ Deletes all the value from the table by adding table_name to parameter
        
        SYNTAX: DELETE FROM TABLE_NAME"""
        query=""" DELETE FROM {}""".format(table_name)
        self._cursor.execute(query)
          
    def update_table(self,query):
        """Update's the table from database using query as input use " " at the beginning and end of the query
        
        SYNTAX: UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition"""
        query=query
        self._cursor.execute(query)
        self._connection.commit()
    def select_all(self,table_name):
        """Select's all values from the table.

        SYNTAX: SELECT * FROM TABLE_NAME"""
        query = """SELECT * FROM {}""".format(table_name)
        self._cursor.execute(query)
        row = self._cursor.fetchall()
        for index,record in enumerate(row):
            print(index,record,'\n')
    def select_n_rows(self,table_name,number_of_rows):
        """Select's n number of values from the table.

        SYNTAX: SELECT * FROM TABLE_NAME"""
        query = """SELECT * FROM {}""".format(table_name)
        self._cursor.execute(query)
        row = self._cursor.fetchmany(number_of_rows)
        for index,record in enumerate(row):
            print(index,record,'\n')
    def select_conditional(self,query):
        """Select's values from the table with a condition in it .
           USE 3 QUOTES TO WRITE A QUERY.
        
        SYNTAX: SELECT * FROM TABLE_NAME WHERE CONDITION"""
        query = query
        self._cursor.execute(query)
        row = self._cursor.fetchall()
        for index,record in enumerate(row):
            print(index,record,'\n')
    def convert_to_date(self,datetime):
        st="TO_DATE('{}','DD-MM-YYYY HH24:MI:SS')".format(datetime)
        return st
    
        
    def close(self):
        self._connection.close()
     

       

    

conn=ConnectToOracle()






