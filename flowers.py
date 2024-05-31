from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel , Field
from uuid import UUID

app = FastAPI(title='Flowers API' , description='API for flowers' , version='1.0')

class Flowers(BaseModel):
    id : UUID
    title: str = Field(min_length=2 , max_length=222)
    price: float = Field(gt=5, lt=100)
    color: str = Field(min_length=10, max_length=100)
    type: str or None = Field(min_length=10, max_length=100)
    data: datetime = Field(default_factory=datetime.now)

database = []

@app.get('/')
async def root():
    return {'message': 'Here you can find API for flowers!'}

@app.post('/flowers')
async def create_flower(flower: Flowers):
    database.append(flower)
    return { 'data':flower,'message': 'You have created a flower'}

@app.get('/flowers/')
async def get_flowers():
    return database

@app.put('/flowers/{id}')
async def update_flower(flower_id:UUID, flower: Flowers):
    a = 0
    for i in database:
        a+=1
        if i.id == flower_id:
            database[a-1] = flower
            return {'data':database[a-1],'message': 'flowers updated successfully'}

    raise HTTPException(status_code=404, detail=f'ID{a-1} does not exist')

@app.delete('/flowers/{id}')
async def delete_flower(flower_id:UUID):
    a = 0
    for i in database:
        a+=1
        if i.id == flower_id:
            del database[a-1]
            return { 'data':database[a-1],'message': 'flowers deleted successfully'}
    raise HTTPException(status_code=404, detail=f'ID{a-1} does not exist')