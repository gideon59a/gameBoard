''' This module is really assuming there will be more than one DB type to use. Assumed here mainly for learning purpose.'''
import abc
from gserver.db_if.db_models import *


class RoomDaoBase(abc.ABC):
    @abc.abstractmethod
    def insert_room(self, room: Room, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def get_room(self, id: int) -> dict:
        pass

    @abc.abstractmethod
    def get_all_room_ids(self) -> list:
        pass

    @abc.abstractmethod
    def insert_board(self, board: Board ) -> None:
        pass

    @abc.abstractmethod
    def get_board(self, id: int ) -> dict:
        pass