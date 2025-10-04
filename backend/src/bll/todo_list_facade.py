from ..models.all_models import TodoList, Task
class TodoListFacade:
    def __init__(self, session):
        self.session = session

    def create_todo_list(self, name: str, user_id: int) -> TodoList:
        """
        Creates a new todo list in the database.

        Args:
            name (str): The name of the todo list.
            user_id (int): The ID of the user to whom the todo list belongs.

        Returns:
            TodoList: The newly created TodoList object.

        Raises:
            ValueError: If the name is missing or empty.
        """
        if not user_id:
            raise ValueError("User ID is required")
        if not name or len(name.strip()) == 0:
            raise ValueError("Name is required")
        
        new_todo_list = TodoList(name=name, user_id=user_id)
        self.session.add(new_todo_list)
        self.session.commit()
        return new_todo_list
    
    def get_todo_list_by_name(self, name: str) -> TodoList | None:
        """
        Retrieves a todo list by its name.

        Args:
            name (str): The name of the todo list.

        Returns:
            TodoList | None: The TodoList object if found, otherwise None.
        """
        return self.session.query(TodoList).filter_by(name=name).first()
    
    def get_all_todo_lists_by_user(self, user_id: int) -> list[TodoList]:
        """
        Retrieves all todo lists associated with a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list[TodoList]: A list of TodoList objects associated with the specified user.
        """
        return self.session.query(TodoList).filter_by(user_id=user_id).all()
    
    def delete_todo_list(self, todo_list_id: int) -> bool:
        """
        Deletes a todo list from the database.

        Args:
            todo_list_id (int): The ID of the todo list to delete.

        Returns:
            bool: True if the todo list was deleted, False otherwise.
        """
        todo_list = self.session.query(TodoList).get(todo_list_id)
        if todo_list:
            self.session.delete(todo_list)
            self.session.commit()
            return True
        return False

    def get_tasks_by_todo_list(self, todo_list_id: int) -> list[Task] | None:
        """
        Retrieves all tasks associated with a specific todo list.

        Args:
            todo_list_id (int): The ID of the todo list.

        Returns:
            list: A list of Task objects associated with the specified todo list.
        """
        tasks = self.session.query(Task).filter_by(todo_list_id=todo_list_id).all()
        if tasks:
            return tasks
