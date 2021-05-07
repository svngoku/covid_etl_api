from typing import Optional
from fastapi import FastAPI, UploadFile, File
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
import asyncio

## MODELS
from models.africa_covid import africa_covid_data_helper
from models.vaccine_covid import vaccine_covid_helper
from models.variant_covid import variant_covid_helper
from models.male_female_deaths_covid import male_female_deaths_covid_helper

# INIT FASTAPI SERVER
app = FastAPI()

#MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = "mongodb+srv://sysbot:sysbot#2021@cluster0.w11b8.mongodb.net/"

# ENABLE FRONT END REQUESTS
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
vaccine_ue_covid_collection = database.get_collection("vacin_test")
variant_covid_collection = database.get_collection("variant_covid")
male_female_deaths_covid_collection = database.get_collection("male_female_deaths_covid")



async def retrieve_africa_data():
    africa_covid_data = []
    async for data in africa_covid_collection.find({}):
        africa_covid_data.append(africa_covid_data_helper(data))
    return africa_covid_data

async def retrieve_vaccine_ue():
    vaccine_ue_datas = []
    async for data in vaccine_ue_covid_collection.find({}):
        vaccine_ue_datas.append(vaccine_covid_helper(data))
    return vaccine_ue_datas

async def retrieve_variant_covid():
    variant_covid_data = []
    async for data in variant_covid_collection.find({}):
        variant_covid_data.append(variant_covid_helper(data))
    return variant_covid_data

async def retrieve_male_female_deaths_covid():
    male_female_deaths_data = []
    async for data in male_female_deaths_covid_collection.find({}):
        male_female_deaths_data.append(male_female_deaths_covid_helper(data))
    return male_female_deaths_data 


@app.get("/")
def read_root():
    return {"message": "Welcome to the covid ETL project!"}

@app.get('/afrique_central')
async def afrique_central():
    africa_datas = await retrieve_africa_data()
    if africa_datas:
        return {"datas": africa_datas}
    return (africa_datas, "Empty list returned")

@app.get('/vaccine_ue')
async def vaccine_ue():
    vaccine_ue_datas = await retrieve_vaccine_ue()
    if vaccine_ue_datas:
        return {"datas": vaccine_ue_datas}
    return (vaccine_ue_datas, "Empty list returned")

@app.get('/variant')
async def get_variants():
    variant_covid_data = await retrieve_variant_covid()
    if variant_covid_data:
        return {"datas": variant_covid_data}
    return (variant_covid_data, "Empty list returned")

@app.get('/male_female_deaths')
async def get_male_female_deaths():
    male_female_deaths_data = await retrieve_male_female_deaths_covid()
    if male_female_deaths_data:
        return {"datas": male_female_deaths_data}
    return (male_female_deaths_data, "Empty list returned")


# @app.post("/upload")
# async def uploadfile(file: UploadFile = File(...)):
#     return { "filename": file.filename }


if __name__ == '__main__':
    uvicorn.run(
        "main:app"
    )

