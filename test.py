from fastapi import FastAPI,Depends,HTTPException,Header
from fastapi.security.api_key import APIKeyHeader
import joblib
from scipy.stats import linregress
from fastapi.middleware.cors import CORSMiddleware
API_KEY='Hello-World'
API_KEY_NAME='Authorization'
api_key_header=APIKeyHeader(name=API_KEY_NAME,auto_error=False)
app=FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5000",
    "http://127.0.0.1:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


loaded_model = joblib.load('RandomForest.pkl')

# def verify_api_key(x_api_key:str=Depends(api_key_header)):
#     if x_api_key ==API_KEY:
#         return api_key_header
#     else:
#         raise HTTPException(status_code=403,detail="Invalid API_KEY")
@app.post('/predict')
async def predict(honeypot , mouse_movement,api_key):
   
    if api_key !='Hello-World':
        return {"Error" : "Envalid API Key"}
    
    
    honeypot = 1 if honeypot == "Yes" else 0
    
    
    mouse_movement=1 if mouse_movement=='non linear' else 0
    
    
    prediction = loaded_model.predict([[honeypot, mouse_movement]]) 
    
    
    return {"prediction":prediction[0]}
    
    
  