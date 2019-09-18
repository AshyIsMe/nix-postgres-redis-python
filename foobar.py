#!/usr/bin/env python3

import sqlalchemy as db
import pandas as pd

def createdb():
  #engine = db.create_engine("postgres://localhost")
  #conn = engine.connect()
  #conn.execute("commit")
  #conn.execute("create database databaseaf")
  #conn.close()

  with db.create_engine('postgresql:///postgres', isolation_level='AUTOCOMMIT').connect() as connection:
	  connection.execute('CREATE DATABASE databaseaf')

def main():
  engine = db.create_engine("postgres://localhost/databaseaf")

  connection = engine.connect()
  metadata = db.MetaData()

  emp = db.Table('emp', metadata,
          db.Column('Id', db.Integer()),
          db.Column('name', db.String(255), nullable=False),
          db.Column('salary', db.Float(), default=100.0),
          db.Column('active', db.Boolean(), default=True)
          )

  metadata.create_all(engine) #Creates the table

  #Inserting many records at ones
  query = db.insert(emp)
  values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
           {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
  ResultProxy = connection.execute(query,values_list)

  results = connection.execute(db.select([emp])).fetchall()
  df = pd.DataFrame(results)
  df.columns = results[0].keys()
  print( df.head(4) )


if __name__ == "__main__":
    createdb()
    main()
