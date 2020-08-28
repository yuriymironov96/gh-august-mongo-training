from models.user import User

def create_user():
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
