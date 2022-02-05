from services.image_generation_service import ImageGenerationService
from entities.map import Status

class DrawingService:
    """A service that handles the calls to ImageGenerationService to generate the dungeon map.

    Attributes:
        image_generation_service: The service handling the generation of the image
        room_generation_service: The service handling the room generation. Needed for the room list.
        cell_size: A tuple containing the width and height of an individual cell in pixels
        map: A map object that contains the information about occupied cells
    """

    def __init__(self, room_generation_service, map_entity, cell_size=(20,20)):
        """Create a new DrawingService object

        Args:
            room_generation_service: The service handling the room generation.
            cell_size: Tuple (width, height), the size of an individual cell in pixels
            map_entity: A map object containing the information about occupied cells
        """

        self._image_generation_service = ImageGenerationService(map_entity.map_width*cell_size[0],
                                                                map_entity.map_height*cell_size[1])
        self._room_generation_service = room_generation_service
        self._cell_size = cell_size
        self._map = map_entity

    def draw_rooms(self): # Test with mock
        """Draw the generated rooms on the map, if possible"""

        for room in self._room_generation_service.rooms:
            if self._can_draw_room(room):
                room.toggle_generated()
                coordinates = self._get_coordinate_value(room.coordinates[0], room.coordinates[1])
                self._image_generation_service.draw_room(coordinates[0],
                                                         coordinates[1],
                                                         room.width*self._cell_size[0],
                                                         room.height*self._cell_size[1])
                for y_coord in range(room.coordinates[1], room.coordinates[1] + room.height):
                    for x_coord in range(room.coordinates[0], room.coordinates[0] + room.width):
                        self._map.occupy(x_coord, y_coord)

    def draw_grid(self, line_thickness=1): # Test with mock
        """Draw the movement grid for the map. Should be called last.

        Args:
            line_thickness: The desired thickness of the grid lines
        """

        self._image_generation_service.draw_grid(self._cell_size[0],
                                                 self._cell_size[1],
                                                 line_thickness)

    def get_image(self):
        """Get the image object from the ImageGenerationService
        
        Returns: The generated image object
        """

        return self._image_generation_service.get_generated_image()

    def _can_draw_room(self, room):
        """Checks if the room can be generated in the allotted space.
        The space must not go past the edge wall of the dungeon and
        there must be at least a cell-wide gap between rooms.

        Args:
            room: The room to be checked

        Returns: True if the room can be placed, False otherwise
        """

        if (room.coordinates[0] < 1
            or room.coordinates[0] > self._map.map_width - 1
            or room.coordinates[0] + room.width > self._map.map_width - 1):
            return False

        if (room.coordinates[1] < 1
            or room.coordinates[1] > self._map.map_height - 1
            or room.coordinates[1] + room.height > self._map.map_height - 1):
            return False

        for y_coord in range(room.coordinates[1], room.coordinates[1]+room.height):
            for x_coord in range(room.coordinates[0], room.coordinates[0]+room.width):
                if (x_coord, y_coord) in self._map.cells:
                    if self._map.cells[(x_coord, y_coord)] != Status.UNOCCUPIED:
                        return False

        return True

    def _get_coordinate_value(self, cell_x, cell_y):
        """Gives the pixel coordinates of a given cell's top left corner

        Args:
            cell_x: The x coordinate of the cell to convert
            cell_y: The y coordinate of the cell to convert

        Returns: Tuple (x, y) containing the coordinates of the top left corner of the cell in
        pixels
        """

        return cell_x * self._cell_size[0], cell_y * self._cell_size[1]
