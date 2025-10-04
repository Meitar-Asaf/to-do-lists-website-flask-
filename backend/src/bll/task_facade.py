from ..models.all_models import Task
class TaskFacade:
    def __init__(self, session):
        self.session = session

    def create_task(self, title: str, description: str, todo_list_id: int) -> Task:
        """
        Creates a new task in the database.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            todo_list_id (int): The ID of the todo list to which the task belongs.

        Returns:
            Task: The newly created Task object.

        Raises:
            ValueError: If the title is missing or empty.
        """
        if not todo_list_id:
            raise ValueError("Todo list ID is required")
        if not title or len(title.strip()) == 0:
            raise ValueError("Title is required")
        
        new_task = Task(title=title, description=description, todo_list_id=todo_list_id)
        self.session.add(new_task)
        self.session.commit()
        return new_task
    
    def get_task_by_title(self, title: str) -> Task | None:
        """
        Retrieves a task by its title.

        Args:
            title (str): The title of the task.

        Returns:
            Task | None: The Task object if found, otherwise None.
        """
        return self.session.query(Task).filter_by(title=title).first()
    
    def get_all_tasks_by_todo_list(self, todo_list_id: int) -> list[Task]:
        """
        Retrieves all tasks associated with a specific todo list.

        Args:
            todo_list_id (int): The ID of the todo list.

        Returns:
            list[Task]: A list of Task objects associated with the specified todo list.
        """
        return self.session.query(Task).filter_by(todo_list_id=todo_list_id).all()
    
    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task from the database.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            bool: True if the task was deleted, False otherwise.
        """
        task = self.session.query(Task).get(task_id)
        if task:
            self.session.delete(task)
            self.session.commit()
            return True
        return False
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> Task | None:
        """
        Updates an existing task in the database.

        Args:
            task_id (int): The ID of the task to update.
            title (str, optional): The new title of the task. Defaults to None.
            description (str, optional): The new description of the task. Defaults to None.

        Returns:
            Task | None: The updated Task object if found and updated, otherwise None.
        """
        task = self.session.query(Task).get(task_id)
        if not task:
            return None
        if title is not None:
            if not title or len(title.strip()) == 0:
                raise ValueError("Title cannot be empty")
            task.title = title
        if description is not None:
            task.description = description
        self.session.commit()
        return task
    
    def get_task_by_id(self, task_id: int) -> Task | None:
        """
        Retrieves a task by its ID.

        Args:
            task_id (int): The ID of the task.

        Returns:
            Task | None: The Task object if found, otherwise None.
        """
        return self.session.query(Task).get(task_id)