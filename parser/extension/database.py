import psycopg2
from config import config

connection = psycopg2.connect(user=config['postgresql']['user'],
                              password=config['postgresql']['password'],
                              host=config['postgresql']['host'],
                              port=config['postgresql']['port'],
                              database=config['postgresql']['database'])
cursor = connection.cursor()
