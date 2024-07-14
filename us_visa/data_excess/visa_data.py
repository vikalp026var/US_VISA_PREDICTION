from us_visa.configuration.mongodb_conn import MongoDBClient
from us_visa.constant import DB_NAME
from us_visa.exception import USvisaException
import pandas as pd 
import sys 
from typing import Optional
import numpy as np 


class USvisaData:
    def __init__(self):
        try:
            self.mongo_client=MongoDBClient(database_name=DB_NAME)
        except Exception as e:
            raise USvisaException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None):
        try:
            if database_name is None:
                collection=self.mongo_client.database[collection_name]
            else:
                collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=['_id'],axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df 
        except Exception as e:
            raise USvisaException(e,sys) 
