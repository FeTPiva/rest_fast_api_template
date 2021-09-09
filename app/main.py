
# http://127.0.0.1:8000/docs
#uvicorn credit_score.main:app --reload

import json
from fastapi import FastAPI, Depends, Body
from fastapi import responses

from fastapi.responses import JSONResponse
from credit_score.apps.entities.user_entity_schema import ResponseScore, UserEntitySchemaPydantic
from credit_score.apps.entities.user_entity_schema import whatever
#import joblib


app = FastAPI(title="Credit Score API",
    description="Api que retorna o score de pessoas para a mesa de crédito",
    version="0.3")


@app.post("/score", tags=["Cálculo Score"], response_model= ResponseScore)
async def retorna_score(score_data: UserEntitySchemaPydantic):
    
    #faz qqlr coisa
    response_api = ResponseScore()
    response_api.categoria = 'Hello'
    response_api.score = 8000.1

    return response_api


@app.post("/predict")
async def pred( ):
    #modelo_dt = joblib.load('clf_dt')
   # result = 

    return 0