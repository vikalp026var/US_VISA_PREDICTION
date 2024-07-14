import os 
from us_visa.constant import DB_NAME,CONNECTION_URL
import pymongo 
import certifi 
from us_visa.logger import logging
from us_visa.exception import USvisaException


ca=certifi.where()



class MongoDBClient:
    client=None

    def __init__(self,database_name=DB_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url=CONNECTION_URL
                if mongo_db_url is None:
                    raise Exception(f"Environment key :{CONNECTION_URL} is not set.")
                MongoDBClient.client=pymongo.MongoClient(CONNECTION_URL,tlsCAFile=ca)
            self.client=MongoDBClient.client
            self.database=self.client[database_name]
            self.database_name=database_name
            logging.info("MongoDB connection successfull")
        except Exception as e:
            raise USvisaException(e)