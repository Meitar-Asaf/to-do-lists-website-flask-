from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.all_models import Base, User, TodoList, Task
from src.config import DATABASE_URL

def run_seed():

    """
    Populates the database with a single admin user.

    This function creates a PostgreSQL engine using the DATABASE_URL
    environment variable, creates a session, and then creates all
    tables in the database using the Base.metadata.create_all
    method. Finally, it adds a single admin user to the database
    and commits the changes.

    :return: None
    """
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    user1 = User(first_name="John", last_name="Doe", email="admin@example.com", password="$2b$12$J.V0tU2ZkDs5iRs3OMq/gep4I3s5cBB/I6p86YoWiuBg19GnrI.eC", is_staff=True)
    session.add(user1)  
    session.commit()