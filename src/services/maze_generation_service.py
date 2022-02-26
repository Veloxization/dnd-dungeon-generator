import random
from collections import deque
from entities.map import Status

class MazeGenerationService:
    """The service for generating the maze used as the hallways of the dungeon.

    Attributes:
        map: The map object on which to draw the maze
        maze_cells: A two-dimensional list containing the status of the cells.
        (u)nvisited, (r)oom, (w)all and (p)assage.
        Initially all cells are unvisited.
        walls: A list containing the locations of the walls generated so far
    """

    def __init__(self, map_object):
        """Create a new MazeGenerationService object

        Args:
            map_object: The map object on which to draw the maze.
            Rooms should be added to the map before generating the maze.
        """

        self._map = map_object
        self._maze_cells = [['u' for x_coord in range(map_object.map_width)]
                             for y_coord in range(map_object.map_height)]
        self._walls = []

    def init_maze(self):
        """Initialize the maze by looking at which cells already have rooms
        and add wall and room cells respectively."""

        for y_coord in range(self._map.map_height):
            for x_coord in range(self._map.map_width):
                if (x_coord, y_coord) in self._map.cells:
                    if self._map.cells[(x_coord, y_coord)] == Status.ADJACENT_OCCUPIED:
                        self._maze_cells[x_coord][y_coord] = 'w'
                    elif self._map.cells[(x_coord, y_coord)] == Status.OCCUPIED:
                        self._maze_cells[x_coord][y_coord] = 'r'

    def generate_perfect_maze(self):
        """Fill the remaining available cells with perfect mazes
        utilizing a slightly modified randomized Prim's algorithm.
        A maze is perfect if it does not have any loops."""

        starting_point = self._find_starting_point()
        while starting_point is not None:
            self._add_passage((starting_point[0], starting_point[1]))

            while self._walls:
                rand_wall = random.choice(self._walls)
                if rand_wall[1] + 1 < self._map.map_height:
                    if (self._maze_cells[rand_wall[0]][rand_wall[1] + 1] in ('u', 'w')
                    and self._maze_cells[rand_wall[0]][rand_wall[1] - 1] == 'p'):
                        if self._count_adjacent_passages(rand_wall) < 2:
                            self._add_passage(rand_wall)
                            continue
                if rand_wall[0] + 1 < self._map.map_width:
                    if (self._maze_cells[rand_wall[0] + 1][rand_wall[1]] in ('u', 'w')
                    and self._maze_cells[rand_wall[0] - 1][rand_wall[1]] == 'p'):
                        if self._count_adjacent_passages(rand_wall) < 2:
                            self._add_passage(rand_wall)
                            continue
                if rand_wall[1] - 1 >= 0:
                    if (self._maze_cells[rand_wall[0]][rand_wall[1] - 1] in ('u', 'w')
                    and self._maze_cells[rand_wall[0]][rand_wall[1] + 1] == 'p'):
                        if self._count_adjacent_passages(rand_wall) < 2:
                            self._add_passage(rand_wall)
                            continue
                if rand_wall[0] - 1 >= 0:
                    if (self._maze_cells[rand_wall[0] - 1][rand_wall[1]] in ('u', 'w')
                    and self._maze_cells[rand_wall[0] + 1][rand_wall[1]] == 'p'):
                        if self._count_adjacent_passages(rand_wall) < 2:
                            self._add_passage(rand_wall)
                            continue
                self._walls.remove(rand_wall)

            starting_point = self._find_starting_point()

    def connect_maze_to_rooms(self, odds_of_loops=0.5):
        """Connect passage cells to room cells, or rooms to other rooms

        Args:
            odds_of_loops: The odds of the dungeon having loops, between 0 and 1
        """

        if odds_of_loops < 0: # pragma: no cover
            odds_of_loops = 0
        elif odds_of_loops > 1: # pragma: no cover
            odds_of_loops = 1
        connections = self._get_connections()
        if connections:
            rand_connection = random.choice(list(connections.keys()))
            added_regions = {connections[rand_connection][0], connections[rand_connection][1]}
            self._map.occupy(rand_connection[0], rand_connection[1])
            self._maze_cells[rand_connection[0]][rand_connection[1]] = 'p'
            connections.pop(rand_connection)
            while connections:
                rand_connection = random.choice(list(connections.keys()))
                if (connections[rand_connection][0] in added_regions
                and connections[rand_connection][1] in added_regions):
                    if random.random() < odds_of_loops:
                        self._map.occupy(rand_connection[0], rand_connection[1])
                        self._maze_cells[rand_connection[0]][rand_connection[1]] = 'p'
                else:
                    added_regions.add(connections[rand_connection][0])
                    added_regions.add(connections[rand_connection][1])
                    self._map.occupy(rand_connection[0], rand_connection[1])
                    self._maze_cells[rand_connection[0]][rand_connection[1]] = 'p'
                connections.pop(rand_connection)
            # Brute force solution to remaining unconnected regions
            connections = self._get_connections()
            for connection in list(connections.keys()):
                if connections[connection][0] != connections[connection][1]:
                    self._map.occupy(rand_connection[0], rand_connection[1])
                    self._maze_cells[rand_connection[0]][rand_connection[1]] = 'p'

    def _get_connections(self):
        """Find all room-to-room or passage-to-room connections.

        Returns: A dictionary object where the keys are (x, y) tuples of the coordinates of
        the connections and the values are tuples with IDs of the two regions the connection
        connects
        """

        connections = {}
        for y_coord in range(self._map.map_height):
            for x_coord in range(self._map.map_width):
                if (self._maze_cells[x_coord][y_coord] == 'w'
                and self._count_adjacent_passages((x_coord, y_coord)) == 2):
                    connection = self._get_connection((x_coord, y_coord))
                    if connection:
                        connections[(x_coord, y_coord)] = connection
        return connections

    def _add_wall(self, coordinates):
        """Adds a wall to the specified coordinates

        Args:
            coordinates: (int, int) Tuple containing the coordinates of the wall to be added
        """

        if self._maze_cells[coordinates[0]][coordinates[1]] != 'p':
            self._walls.append(coordinates)
            self._maze_cells[coordinates[0]][coordinates[1]] = 'w'

    def _add_passage(self, coordinates):
        """Adds a passage to the specified coordinates and surround it with walls

        Args:
            coordinates: (int, int) Tuple containing the coordinates of the passage to be added
        """

        self._maze_cells[coordinates[0]][coordinates[1]] = 'p'
        self._map.occupy(coordinates[0], coordinates[1])
        if (coordinates[0], coordinates[1]) in self._walls:
            self._walls.remove((coordinates[0], coordinates[1]))
        self._add_wall((coordinates[0], coordinates[1] + 1))
        self._add_wall((coordinates[0], coordinates[1] - 1))
        self._add_wall((coordinates[0] + 1, coordinates[1]))
        self._add_wall((coordinates[0] - 1, coordinates[1]))

    def _count_adjacent_passages(self, coordinates):
        """Counts the undiagonally adjacent passage and room cells to the given coordinates

        Args:
            coordinates: (int, int) Tuple containing the coordinates of the cell to check

        Returns: Integer of the number of adjacent passages
        """

        passage_num = 0
        if coordinates[1] + 1 < self._map.map_height and coordinates[1] - 1 >= 0:
            if self._maze_cells[coordinates[0]][coordinates[1]+1] in ('p', 'r'):
                passage_num += 1
            if self._maze_cells[coordinates[0]][coordinates[1]-1] in ('p', 'r'):
                passage_num += 1
        if coordinates[0] + 1 < self._map.map_width and coordinates[0] - 1 >= 0:
            if self._maze_cells[coordinates[0]+1][coordinates[1]] in ('p', 'r'):
                passage_num += 1
            if self._maze_cells[coordinates[0]-1][coordinates[1]] in ('p', 'r'):
                passage_num += 1

        return passage_num

    def _get_connection(self, coordinates):
        """Checks whether the given cell is a connection between a room and a corridor or two rooms.

        Args:
            coordinates: (int, int) Tuple containing the coordinates of the cell to check

        Returns: (int, int) Tuple containing the identifiers of the two regions
        the connection connects, or None if the cell is not a connection
        """

        if self._maze_cells[coordinates[0]][coordinates[1]] == 'w':
            if coordinates[1] + 1 < self._map.map_height and coordinates[1] - 1 > 0:
                if (self._maze_cells[coordinates[0]][coordinates[1] + 1] in ('r', 'p')
                and self._maze_cells[coordinates[0]][coordinates[1] - 1] == 'r'):
                    return (self._map.cell_regions[(coordinates[0], coordinates[1] + 1)],
                    self._map.cell_regions[(coordinates[0], coordinates[1] - 1)])
                if (self._maze_cells[coordinates[0]][coordinates[1] - 1] in ('r', 'p')
                and self._maze_cells[coordinates[0]][coordinates[1] + 1] == 'r'):
                    return (self._map.cell_regions[(coordinates[0], coordinates[1] - 1)],
                    self._map.cell_regions[(coordinates[0], coordinates[1] + 1)])
            if coordinates[0] + 1 < self._map.map_width and coordinates[0] - 1 > 0:
                if (self._maze_cells[coordinates[0] + 1][coordinates[1]] in ('r', 'p')
                and self._maze_cells[coordinates[0] - 1][coordinates[1]] == 'r'):
                    return (self._map.cell_regions[(coordinates[0] + 1, coordinates[1])],
                    self._map.cell_regions[(coordinates[0] - 1, coordinates[1])])
                if (self._maze_cells[coordinates[0] - 1][coordinates[1]] in ('r', 'p')
                and self._maze_cells[coordinates[0] + 1][coordinates[1]] == 'r'):
                    return (self._map.cell_regions[(coordinates[0] - 1, coordinates[1])],
                    self._map.cell_regions[(coordinates[0] + 1, coordinates[1])])
        return None

    def _find_starting_point(self):
        """Attempts to find a starting cell for a maze.
        A cell is a valid starting point only if it is unvisited
        and is not on the edge.

        Returns: (int, int) Tuple containing the coordinates of the starting cell.
        None if no available starting points remain."""

        for y_coord in range(1, self._map.map_height - 1):
            for x_coord in range(1, self._map.map_width - 1):
                if self._maze_cells[x_coord][y_coord] == 'u':
                    return (x_coord, y_coord)

        return None

    def prune_dead_ends(self):
        """Remove dead ends, i.e. cells that have only one neighbouring passage,
        leaving only winding paths between rooms. Utilises depth-first search."""
        for y_coord in range(self._map.map_height):
            for x_coord in range(self._map.map_width):
                if self._maze_cells[x_coord][y_coord] == 'p':
                    stack = deque()
                    visited = [[False for x_coord in range(self._map.map_width)]
                               for y_coord in range(self._map.map_height)]
                    stack.append((x_coord, y_coord))
                    while stack:
                        source = stack.popleft()
                        if self._map.is_cell_dead_end(source[0], source[1]):
                            self._maze_cells[source[0]][source[1]] = 'w'
                            self._map.unoccupy(source[0], source[1])
                        if not visited[source[0]][source[1]]:
                            visited[source[0]][source[1]] = True
                            for adjacent in self._map.get_adjacent_cells(source[0], source[1]):
                                if self._map.is_cell_occupied(adjacent[0], adjacent[1]):
                                    stack.appendleft(adjacent)
