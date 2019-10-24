import requests
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import json


response = requests.get("http://localhost/deviceStatus")

mydb = mysql.connector.connect(
  host="localhost",
  database='ri_db',
  user="test",
  passwd=""
)


db_connection_str = 'mysql+pymysql://test:@localhost/ri_db'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM rules', con=db_connection)

input = json.loads(response.content)


df = df[(df.deviceName == input["deviceName"]) & (df.deviceStatus == input["deviceStatus"])]

if df.action.count() > 1:
  print("ambiguous")
elif df.action.count() != 1:
  print("unknown")
else:
  print(df['action'].iloc[0])