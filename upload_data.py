from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#uniform resource identifier
uri = "mongodb+srv://Syedzaid0911:syedzaid0911@cluster0.28po1ro.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

##create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"


# read the data as a dataframe
df=pd.read_csv("E:\MLProject\sensor-fault-detection\notebooks\wafer_23012020_041211 (1).csv")
df=df.drop("Unnamed: 0",axis=1)

# convert the data as a json
json_records=list(json.loads(df.T.to_json()).values())

# now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)
