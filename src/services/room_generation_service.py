import random
from entities.room import Room

class RoomGenerationService:
    """A class handling the generation of dungeon rooms

    Attributes:
        cell_width: The width of a single cell in pixels.
        Used in converting room size in cells into room size in pixels.
        cell_height: The height of a single cell in pixels.
        Used in converting room size in cell into room size in pixels.
        map_width: The width of the map in which to generate the rooms.
        Used in creating the coordinate ranges where rooms can be placed.
        map_height: The width of the map in which to generate the rooms.
        Used in creating the coordinate ranges where rooms can be placed.
        rooms: A list containing the generated Room objects
    """

    def __init__(self, cell_width=20, cell_height=20, map_width=50, map_height=50):
        """Create a new RoomGenerationService object

        Args:
            cell_width: The width of a single cell in pixels
            cell_height: The height of a single cell in pixels
            map_width: The width of the map in which to place the room
            map_height: The height of the map in which to place the room
        """

        self._cell_width = cell_width
        self._cell_height = cell_height
        self._map_width = map_width
        self._map_height = map_height
        self.rooms = []

    def generate_room(self, coordinates=(0,0), room_width=2, room_height=2):
        """Generate a new room object

        Args:
            coordinates: The coordinates of the top left cell of the room
            room_width: The width of the room in cells
            room_height: The height of the room in cells
        """

        room = Room(coordinates, room_width, room_height)
        self.rooms.append(room)

    def generate_random_rooms(self, amount, min_width=2, max_width=2, min_height=2, max_height=2):
        """Generate multiple random rooms.

        Args:
            amount: How many rooms are generated, note that not all can be placed
            min_width: How small can the room's width be, recommended 2 or more
            max_width: How large can the room's width be, recommended 2 or more
            min_height: How small can the room's height be, recommended 2 or more
            max_height: How large can the room's height be, recommended 2 or more
        """

        for num in range(amount):
            width = random.randint(min_width, max_width)
            height = random.randint(min_height, max_height)
            x_coord = random.randint(1, self._map_width - width - 1)
            y_coord = random.randint(1, self._map_height - height - 1)
            self.generate_room((x_coord, y_coord), width, height)
