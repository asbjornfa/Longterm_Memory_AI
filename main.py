from fastapi import FastAPI
import mainAI
app = FastAPI()


app.include_router(mainAI.router, prefix="/AI")
