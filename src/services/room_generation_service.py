from entities.room import Room

class RoomGenerationService:
    """A class handling the generation of dungeon rooms

    Attributes:
        cell_width: The width of a single cell in pixels.
        Used in converting room size in cells into room size in pixels.
        cell_height: The height of a single cell in pixels.
        Used in converting room size in cell into room size in pixels.
        rooms: A list containing the generated Room objects
    """

    def __init__(self, cell_width=20, cell_height=20):
        """Create a new RoomGenerationService object

        Args:
            cell_width: The width of a single cell in pixels
            cell_height: The height of a single cell in pixels
        """

        self._cell_width = cell_width
        self._cell_height = cell_height
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
