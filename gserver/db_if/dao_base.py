''' This module is really assuming there will be more than one DB type to use. Assumed here mainly for learning purpose.'''
import abc
from gserver.db_if.db_models import *


class RoomDaoBase(abc.ABC):
    def __init__(self, db_client):
        self.dbc = db_client
        print(f'Ops Redis client: {self.dbc}')

    @abc.abstractmethod
    def insert_room(self, room: Room, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def get_room(self, room_id: int) -> dict:
        pass


    @abc.abstractmethod
    def get_room_board(self, room_dict: dict) -> dict:
        pass


    @abc.abstractmethod
    def get_room_status(self, room_id: int) -> int:  # Needed for avoiding getting the whole game
        print(f' DEBUG *** HERE ***')
        return 0

    @abc.abstractmethod
    def del_room(self, room_id: int):
        pass

    @abc.abstractmethod
    def get_all_room_ids(self) -> list:
        pass

    #@abc.abstractmethod
    #def insert_board(self, board: BoardG4inRow) -> None:
    #    pass

    #@abc.abstractmethod
    #def get_board(self, id: int) -> dict:
    #    pass
