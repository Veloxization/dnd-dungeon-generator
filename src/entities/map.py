from enum import Enum

class Status(Enum):
    """Cell status enumerator
    UNOCCUPIED: The cell is empty
    ADJACENT_OCCUPIED: An adjacent non-diagonal cell is occupied
    OCCUPIED: The cell itself is occupied"""

    UNOCCUPIED = 0
    ADJACENT_OCCUPIED = 1
    OCCUPIED = 2

class Map:
    """Keeps track of which cells are occupied by rooms or corridors

    Attributes:
        cells: A dictionary which keeps track of the status of individual cells.
        A coordinate tuple (x, y) acts as the key.
        The status enumerator acts as the value.
        regions: A dictionary which keeps track of the regions of the map.
        All cells that can be reached without passing through unoccupied cells
        belong in the same region.
        An integer starting from 0 acts as a key.
        A list of coordinate tuples (x, y) acts as the value.
        cell_regions: A dictionary which shows which region a certain cell belongs to.
        A coordinate tuple (x, y) acts as the key.
        A region identifier integer acts as the value.
        map_width: The width of the dungeon in cells
        map_height: The height of the dungeon in cells
    """

    def __init__(self, map_width=50, map_height=50):
        """Create a new Map object

        Args:
            map_width: The width of the map in cells
            map_height: The height of the map in cells
        """
        self.cells = {}
        self.regions = {}
        self.cell_regions = {}
        self.map_width = map_width
        self.map_height = map_height

    def occupy(self, cell_x, cell_y):
        """Occupy a cell, called when a room or a corridor is added.
        Also handles assigning cells to their regions.

        Args:
            cell_x: The x coordinate of the cell to occupy
            cell_y: The y coordinate of the cell to occupy
        """

        self.cells[(cell_x, cell_y)] = Status.OCCUPIED
        for cell in self._get_adjacent_cells(cell_x, cell_y):
            if cell not in self.cells:
                self.cells[cell] = Status.ADJACENT_OCCUPIED
            elif self.cells[cell] == Status.UNOCCUPIED:
                self.cells[cell] = Status.ADJACENT_OCCUPIED
            elif self.cells[cell] == Status.OCCUPIED:
                if (cell_x, cell_y) in self.cell_regions and cell in self.cell_regions:
                    if self.cell_regions[(cell_x, cell_y)] != self.cell_regions[cell]:
                        new_region = min(self.cell_regions[(cell_x, cell_y)],
                                         self.cell_regions[cell])
                        old_region = max(self.cell_regions[(cell_x, cell_y)],
                                         self.cell_regions[cell])
                        self.cell_regions[(cell_x, cell_y)] = new_region
                        self.cell_regions[cell] = new_region
                        for value in self.regions[old_region]:
                            self.cell_regions[value] = new_region
                        self.regions[new_region].extend(self.regions[old_region])
                else:
                    self.regions[self.cell_regions[cell]].append((cell_x, cell_y))
                    self.cell_regions[(cell_x, cell_y)] = self.cell_regions[cell]
        if (cell_x, cell_y) not in self.cell_regions:
            new_region_id = len(self.regions)
            self.regions[new_region_id] = []
            self.regions[new_region_id].append((cell_x, cell_y))
            self.cell_regions[(cell_x, cell_y)] = new_region_id

    def unoccupy(self, cell_x, cell_y):
        """Unoccupy a cell and adjacent cells if applicable.
        Also removes the cell from its region.

        Args:
            cell_x: The x coordinate of the cell to occupy
            cell_y: The y coordinate of the cell to occupy
        """

        self.cells[(cell_x, cell_y)] = Status.UNOCCUPIED
        for cell in self._get_adjacent_cells(cell_x, cell_y):
            marked_for_removal = True
            for sub_cell in self._get_adjacent_cells(cell[0], cell[1]):
                if sub_cell in self.cells:
                    if self.cells[sub_cell] == Status.OCCUPIED:
                        marked_for_removal = False
                        break
            if marked_for_removal:
                self.cells[cell] = Status.UNOCCUPIED
        if (cell_x, cell_y) in self.cell_regions:
            self.regions[self.cell_regions[(cell_x, cell_y)]].remove((cell_x, cell_y))
            self.cell_regions.pop((cell_x, cell_y))

    def is_cell_dead_end(self, cell_x, cell_y):
        """Check if the specified cell is a dead end,
        i.e. if it has less than two occupied neighbors.

        Args:
            cell_x: The x coordinate of the cell to check
            cell_y: The y coordinate of the cell to check

        Returns: True if the cell is a dead end, false otherwise.
        """

        number_of_cells = 0
        if self.is_cell_occupied(cell_x - 1, cell_y):
            number_of_cells += 1
        if self.is_cell_occupied(cell_x + 1, cell_y):
            number_of_cells += 1
        if self.is_cell_occupied(cell_x, cell_y - 1):
            number_of_cells += 1
        if self.is_cell_occupied(cell_x, cell_y + 1):
            number_of_cells += 1

        return number_of_cells < 2

    def _get_adjacent_cells(self, cell_x, cell_y):
        """Get the non-diagonally adjacent cells of a given cell

        Args:
            cell_x: The x coordinate of the cell whose adjacent cells to get
            cell_y: The y coordinate of the cell whose adjacent cells to get

        Returns: A list of adjacent cells
        """

        adjacent_cells = []
        if cell_x > 0:
            adjacent_cells.append((cell_x-1, cell_y))
        if cell_x < self.map_width:
            adjacent_cells.append((cell_x+1, cell_y))
        if cell_y > 0:
            adjacent_cells.append((cell_x, cell_y-1))
        if cell_y < self.map_height:
            adjacent_cells.append((cell_x, cell_y+1))

        return adjacent_cells

    def is_cell_occupied(self, cell_x, cell_y):
        """Checks whether the specified cell is occupied

        Args:
            cell_x: The x coordinate of the cell to check
            cell_y: The y coordinate of the cell to check

        Returns: True if the cell is occupied, False otherwise
        """

        if (cell_x, cell_y) in self.cells:
            if self.cells[(cell_x, cell_y)] == Status.OCCUPIED:
                return True

        return False
