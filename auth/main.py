from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, users
from database import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Lab System"}
