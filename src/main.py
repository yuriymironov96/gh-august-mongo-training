from mongoengine import connect
from playground.playground import create_user

if __name__ == "__main__":
    connect('playground')
    create_user()