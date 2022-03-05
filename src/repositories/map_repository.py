class MapRepository:
    """Handles the file management of the generated image.

    Attributes:
        img: The Image object to be handled as a file
    """

    def __init__(self, img):
        """Create a new MapRepository object

        Args:
            img: The Image object to be handled as a file
        """
        self._img = img

    def save(self, name):
        """Save the image to a new file

        Args:
            name: The desired file name
        """

        self._img.save(f"{name}.png", "PNG")
