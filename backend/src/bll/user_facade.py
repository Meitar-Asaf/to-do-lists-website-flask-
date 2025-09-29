from ..models.all_models import User, Base, TodoList, Task
from passlib.hash import bcrypt
from email_validator import validate_email, EmailNotValidError
class UserFacade:
    def __init__(self, session):
        self.session = session

    def missing_fields(self, first_name: str, last_name: str, email: str, password: str, second_password: str) -> None:
        """
        Checks if any of the required fields are missing or empty.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email of the user.
            password (str): The password of the user.
            second_password (str): The second password of the user.

        Raises:
            ValueError: If any of the required fields are missing or empty.
        """
        missing_fields = []
        if not first_name or len(first_name.strip()) == 0:
            missing_fields.append("First name")
        if not last_name or len(last_name.strip()) == 0:
            missing_fields.append("Last name")
        if not email or len(email.strip()) == 0:
            missing_fields.append("Email")
        if not password or len(password.strip()) == 0:
            missing_fields.append("Password")
        if not second_password or len(second_password.strip()) == 0:
            missing_fields.append("Second password")
        if missing_fields:
            raise ValueError(
                f"Missing required fields: {', '.join(missing_fields)}")

    def create_user(self, first_name: str, last_name: str, email: str, password: str, second_password: str) -> User:
        
        
        """
        Creates a new user in the database.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email of the user.
            password (str): The password of the user.
            second_password (str): The second password of the user.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If any of the required fields are missing or empty, or if the passwords do not match.
            EmailNotValidError: If the email address is invalid.
        """
        self.missing_fields(first_name, last_name, email, password, second_password)
        try:
            validate_email(email)
        except EmailNotValidError:
            raise EmailNotValidError("Invalid email address.")
        if self.get_user_by_email(email):
            raise ValueError("A user with this email already exists.")
        if password != second_password:
            raise ValueError("Passwords do not match.")
        password = bcrypt.hash(password)
        new_user = User(first_name=first_name, last_name=last_name,
                        email=email, password=password)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieves a user from the database by their email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            User or None: The User object representing the user with the given email, or None if no such user exists.
        """
        return self.session.query(User).filter_by(email=email).first()

    def get_all_users(self) -> list[User]:
        """
        Retrieves all users from the database.

        Returns:
            list: A list of User objects representing all users in the database.
        """
        return self.session.query(User).all()

    def delete_user(self, user_id: int) -> bool:
        """
        Deletes a user from the database by their id.

        Args:
            user_id (int): The id of the user to delete.

        Returns:
            bool: True if the user was deleted, False otherwise.
        """
        user = self.session.query(User).get(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
