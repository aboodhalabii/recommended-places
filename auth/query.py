from src.database.execute import DBClient
from src.database.model import users, places, favorites
class recommendedQueries:
    def __init__(self):
        self.db_client = DBClient()
    
    def get_places(self):
        query = places.select()
        rows = self.db_client.executeAll(query)
        return rows
    
    def insert_places(self, places_data):
        query = places.insert().values(dict(places_data)).returning(places)
        rows = self.db_client.executeOne(query)
        return rows
    
    def update_places(self, places_data):
        query = places.update().values(dict(places_data)).returning(places)
        rows = self.db_client.executeOne(query)
        return rows

    def get_favorites(self):
        query = favorites.select()
        rows = self.db_client.executeAll(query)
        return rows

    def insert_favorites(self, favorites_data):
        query = favorites.insert().values(dict(favorites_data)).returning(favorites)
        rows = self.db_client.executeOne(query)
        return rows

    def update_favorites(self, favorites_data):
        query = favorites.update().values(dict(favorites_data)).returning(favorites)
        rows = self.db_client.executeOne(query)
        return rows

    def get_users(self):
        query = users.select()
        rows = self.db_client.executeOne(query)
        return rows

    def insert_users(self, user_data):
        query = users.insert().values(dict(users_data)).returning(users)
        rows = self.db_client.executeOne(query)
        return rows

    


    
