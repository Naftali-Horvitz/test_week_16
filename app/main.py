import uvicorn
from fastapi import FastAPI
from routes import router
from contextlib import asynccontextmanager
import time
from dal import *



@asynccontextmanager
async def lifespan(app: FastAPI):
    for _ in range(1):
        try:
            mycol = get_col()
            with open("employee_data_advanced.json", 'r') as file:
                data = json.load(file)
                mycol.insert_many(data)
            break
        except Exception as e:
            time.sleep(3)
            raise e
    yield  

app = FastAPI(lifespan=lifespan)
app.include_router(router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
