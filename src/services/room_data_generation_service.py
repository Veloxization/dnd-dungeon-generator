from collections import namedtuple

class RoomDataGenerationService:
    """Service for generating data for the rooms, like their descriptions

    Attributes:
        placed_rooms: A list containing the rooms that have been placed on the map
        data_object: Initialising the namedtuple in which the room information is saved
        data: A list containing namedtuples that store information about each room
    """

    def __init__(self, room_generation_service):
        """Create a new RoomDataGenerationService object

        Args:
            room_generation_service: The room generation service object which contains
            the information on the rooms"""
        self._placed_rooms = []
        self._data_object = namedtuple("Room", ["number"])
        self._data = []
        for room in room_generation_service.rooms:
            if room.is_generated:
                self._placed_rooms.append(room)

    def init_data(self):
        """Initialize the data for each room"""

        for index, room in enumerate(self._placed_rooms):
            data = self._data_object(index+1)
            self._data.append(data)

    def print_data(self, name):
        """Convert the data to string form

        Args:
            name: The desired name to act as the title of the data

        Returns: The data in string form, separated room by room
        """

        data_string = f"{name} - GM Document\n\n"

        for data in self._data:
            data_string += f"Room {data[0]}\n\n"

        return data_string
