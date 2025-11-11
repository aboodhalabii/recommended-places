
from src.database.model import users, places, favorites
from src.auth.query import recommendedQueries
class recommendedQueries:
    def __init__(self):
        self.todo_query = TodoQueries()

    def get_places(self):
        rows = self.places_query.get_places()
        if not rows:
            raise
        return rows

    def insert_places(self):
        rows = self.places_query.insert_places(sub_data)
        if not rows:
            raise
        return rows

    def update_places(self):
        rows = self.places_query.update_places(sub_data)
        if not rows:
            raise
        return rows

    def get_favorites(self):
        rows = self.favorites_query.get_favorites()
        if not rows:
            raise
        return rows

    def insert_favorites(self, sub_data):
        rows = self.favorites_query.insert_favorites(sub_data)
        if not rows:
            raise
        return rows

    def update_favorites(self):
        rows = self.favorites_query.update_favorites(sub_data)
        if not rows:
            raise
        return rows

     def get_users(self):
        rows = self.users_query.get_users()
        if not rows:
            raise
        return rows

    def insert_users(self):
        rows = self.users_query.insert_users(sub_data)
        if not rows:
            raise
        return rows
