from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://bidur:e68eXWEeLZk98tZCTT50dezmMgENL7p1@dpg-crsh5cm8ii6s73edf1j0-a.oregon-postgres.render.com/musicdb_ul5w'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
