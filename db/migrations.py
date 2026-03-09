from db.config import engine
from models.users import Base

# importa os models para registrar no metadata
import models

def create_database():
    Base.metadata.create_all(bind=engine)
    print("Database tables created!")

if __name__ == "__main__":
    create_database()