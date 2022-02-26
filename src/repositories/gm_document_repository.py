class GMDocumentRepository:
    """Handles the file management of the Game Master's text document

    Attributes:
        document: The document in which to write
    """

    def __init__(self, file_name):
        """Create a new GMDocumentRepository object

        Args:
            file_name: The file name of the Game Master's document
        """
        self._document = open(f"demo/{file_name}.txt", 'w')

    def write_data(self, data):
        """Write the contents of the text file

        Args:
            data: The data to be included in the text file
        """
        self._document.write(data)
        self._document.close()
