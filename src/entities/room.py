class Room:
    """An object storing the information about a room

    Attributes:
        coordinates: Room x and y coordinates respectively.
        The coordinate of the cell at the top left corner of the room.
        width: Room width in cells
        height: Room heigh in cells
        is_generated: Whether the room has been successfully placed on the map
    """

    def __init__(self, coordinates=(0,0), width=2, height=2):
        """The constructor used for generating a new Room object

        Args:
            coordinates: Tuple (x, y), the coordinates of the top left cell of the room
            width: The width of the room in cells
            height: The height of the room in cells
        """

        self.coordinates = coordinates
        self.width = width
        self.height = height
        self.is_generated = False

    def toggle_generated(self):
        """Changes the room's status between generated and ungenerated"""

        self.is_generated = not self.is_generated

    def __eq__(self, other):
        return (self.coordinates == other.coordinates and
                self.width == other.width and
                self.height == other.height and
                self.is_generated == other.is_generated)
