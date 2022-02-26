from PIL import Image, ImageDraw

class ImageGenerationService:
    """A class responsible for generating the actual image of the dungeon

    Attributes:
        _map_width: The width of the generated image in pixels
        _map_height: The height of the generated image in pixels
        image: The image object upon which the image is generated
        _image_draw: The object used to draw the graphical elements
    """

    def __init__(self, map_width=1000, map_height=1000):
        """Create a new ImageGenerationService object

        Args:
            map_width: The width of the generated image in pixels
            map_height: The height of the generated image in pixels
        """

        self._map_width = map_width
        self._map_height = map_height
        self.image = Image.new("RGBA", (map_width, map_height), color=(0,0,0,255))
        self.room_image = Image.new("RGBA", (self._map_width, self._map_height), color=(0,0,0,0))
        self.grid_image = Image.new("RGBA", (self._map_width, self._map_height), color=(0,0,0,0))

    def draw_room(self, room_position_x=0, room_position_y=0, room_width=100, room_height=100):
        """Draws a room of specified dimensions and position

        Args:
            room_position_x: The x coordinate of the room.
            The coordinate matches the x coordinate of the top left corner.
            room_position_y: The y coordinate of the room.
            The coordinate matches the y coordinate of the top left corner.
            room_width: The width of the room in pixels
            room_height: The height of the room in pixels
        """

        image_draw = ImageDraw.Draw(self.room_image)
        lower_right_x = room_position_x + room_width
        lower_right_y = room_position_y + room_height
        image_draw.rectangle((room_position_x, room_position_y, lower_right_x, lower_right_y),
                                    fill=(255,255,255,128))

    def draw_grid(self, cell_width=20, cell_height=20, line_thickness=1):
        """Draws the movement grid for the map. Should be used last as this one is on top.

        Args:
            cell_width: The width of an individual grid cell in pixels
            cell_height: The height of an individual grid cell in pixels
            line_thickness: The thickness of the grid lines in pixels
        """

        image_draw = ImageDraw.Draw(self.grid_image)
        line_color = (128,128,128,64)
        current_coordinate = 0
        while current_coordinate < self._map_width:
            image_draw.line((current_coordinate, 0, current_coordinate, self._map_height),
                             fill=line_color,
                             width=line_thickness)
            current_coordinate += cell_width

        current_coordinate = 0
        while current_coordinate < self._map_height:
            image_draw.line((0, current_coordinate, self._map_width, current_coordinate),
                             fill=line_color,
                             width=line_thickness)
            current_coordinate += cell_height
        self.image.alpha_composite(self.grid_image)

    def get_generated_image(self):
        """Get the generated image

        Returns:
            The generated Image object in whatever form it is in
        """

        self.image.alpha_composite(self.room_image)
        self.image.alpha_composite(self.grid_image)
        return self.image
