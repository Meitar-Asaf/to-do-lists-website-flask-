from src.models.all_models import Base, User, TodoList, Task
from src.config import engine, Session

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
    
    session = Session()
    Base.metadata.create_all(engine)

    user1 = User(first_name="John", last_name="Doe", email="admin@example.com", password="$2b$12$J.V0tU2ZkDs5iRs3OMq/gep4I3s5cBB/I6p86YoWiuBg19GnrI.eC", is_staff=True)
    session.add(user1) 
    session.commit()
    todo_list = TodoList(title="Sample Todo List", user_id=1)
    session.add(todo_list)
    session.commit()
    task1 = Task(title="Sample Task 1", description="This is a sample task 1", todo_list_id=1)
    task2 = Task(title="Sample Task 2", description="This is a sample task 2", todo_list_id=1)
    session.add(task1)
    session.add(task2)
    session.commit()