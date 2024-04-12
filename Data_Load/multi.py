from pyathena import connect
import csv

import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


env_src = "..//..//open-data-webapp//"
if load_dotenv(env_src+"loc.env"):
  print("Loaded the Environment Variables")
else:
  SystemExit


def conn_athena():
  engine = connect(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION"),
    schema_name=os.getenv("SCHEMA_NAME"),
    s3_staging_dir=os.getenv("S3_STAGING_DIR"))
  
  cursor = engine.cursor()

  return cursor

def exec_qry(dt_param):
  qry = f"""SELECT * FROM {os.getenv('DATABASE_NAME')}.{os.getenv('TABLE_NAME')} 
                     WHERE date(date_parse("O_Created Date & Time", 
                     '%%Y-%%m-%%dT%%H:%%i:%%s')) = DATE %("{dt_param}")s"""
  print(qry)

def process_dates():
  args = ['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-06','2024-01-07']
  with Pool() as pool:
    results = pool.map(exec_qry,args)

# print(exec_qry("2024-01-01"))
    
process_dates()

  