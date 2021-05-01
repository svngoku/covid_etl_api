from typing import Optional
from fastapi import FastAPI, UploadFile, File
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# import pymongo

app = FastAPI()

#MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = "mongodb+srv://sysbot:sysbot#2021@cluster0.w11b8.mongodb.net/"

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = AsyncIOMotorClient(MONGO_DETAILS)

# Database
database = client.elt_dataviz

# Collections
africa_covid_collection = database.get_collection("central_africa_covid_data")

def africa_covid_data_helper(africa_covid_data):
    return {
        "id": str(africa_covid_data["_id"]),
        "Pays": africa_covid_data["Pays"],
        "Nombre de cas detectes": africa_covid_data["Nombre de cas detectes"],
        "Nombre de deces": africa_covid_data["Nombre de deces"]
    }

async def retrieve_africa_data():
    africa_covid_data = []
    async for data in africa_covid_collection.find():
        africa_covid_data.append(africa_covid_data_helper(data))
    return africa_covid_data


@app.get("/")
def read_root():
    return {"message": "Welcome to the covid ETL project!"}


@app.get('/afrique_central')
async def afrique_central():
    africa_datas = await retrieve_africa_data()
    print(africa_datas)
    if africa_datas:
        return {"datas": africa_datas}
    return (africa_datas, "Empty list returned")

# @app.post('/upload')
# async def uploadfile(file: UploadFile = File(...)):
#     return {"filename": file.filename}


if __name__ == '__main__':
    uvicorn.run(
        "main:app"
    )

