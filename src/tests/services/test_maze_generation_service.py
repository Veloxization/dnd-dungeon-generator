import unittest
from services.maze_generation_service import MazeGenerationService
from entities.map import Map

class TestMazeGenerationService(unittest.TestCase):
    def setUp(self):
        self.map = Map()
        self.maze_generation_service = MazeGenerationService(self.map)
        self.filled_maze_generation_service = MazeGenerationService(self.map)
        for y in range(len(self.filled_maze_generation_service._maze_cells[0])):
            for x in range(len(self.filled_maze_generation_service._maze_cells)):
                self.filled_maze_generation_service._add_wall((x,y))

    def test_the_maze_is_initialized_correctly(self):
        self.map.occupy(1,1)
        self.maze_generation_service.init_maze()
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'r')
        self.assertEqual(self.maze_generation_service._maze_cells[0][1], 'w')
        self.assertEqual(self.maze_generation_service._maze_cells[2][1], 'w')
        self.assertEqual(self.maze_generation_service._maze_cells[1][0], 'w')
        self.assertEqual(self.maze_generation_service._maze_cells[1][2], 'w')

    def test_walls_are_added_correctly(self):
        self.assertEqual(len(self.maze_generation_service._walls), 0)
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'u')
        self.maze_generation_service._add_wall((1,1))
        self.assertEqual(len(self.maze_generation_service._walls), 1)
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'w')

    def test_passages_are_added_correctly(self):
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'u')
        self.assertEqual(self.maze_generation_service._maze_cells[0][1], 'u')
        self.assertEqual(self.maze_generation_service._maze_cells[2][1], 'u')
        self.assertEqual(self.maze_generation_service._maze_cells[1][0], 'u')
        self.assertEqual(self.maze_generation_service._maze_cells[1][2], 'u')
        self.maze_generation_service._add_passage((1,1))
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'p')
        self.assertEqual(self.maze_generation_service._maze_cells[0][1], 'w')
        self.assertEqual(self.maze_generation_service._maze_cells[2][1], 'w')
        self.assertEqual(self.maze_generation_service._maze_cells[1][0], 'w')
        self.assertEqual(self.maze_generation_service._maze_cells[1][2], 'w')

    def test_passages_cannot_be_replaced_by_walls(self):
        self.maze_generation_service._add_passage((1,1))
        self.maze_generation_service._add_wall((1,1))
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'p')

    def test_wall_replaced_by_passage_is_removed(self):
        self.maze_generation_service._add_wall((1,1))
        self.assertEqual(len(self.maze_generation_service._walls), 1)
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'w')
        self.maze_generation_service._add_passage((1,1))
        self.assertNotEqual(len(self.maze_generation_service._walls), 1)
        self.assertEqual(self.maze_generation_service._maze_cells[1][1], 'p')

    def test_adjacent_passages_are_correctly_counted(self):
        self.assertEqual(self.maze_generation_service._count_adjacent_passages((1,1)), 0)
        self.maze_generation_service._add_passage((0,1))
        self.assertEqual(self.maze_generation_service._count_adjacent_passages((1,1)), 1)
        self.maze_generation_service._add_passage((2,1))
        self.assertEqual(self.maze_generation_service._count_adjacent_passages((1,1)), 2)
        self.maze_generation_service._add_passage((1,0))
        self.assertEqual(self.maze_generation_service._count_adjacent_passages((1,1)), 3)
        self.maze_generation_service._add_passage((1,2))
        self.assertEqual(self.maze_generation_service._count_adjacent_passages((1,1)), 4)

    def test_first_available_unvisited_cell_is_found(self):
        self.filled_maze_generation_service._maze_cells[5][5] = 'u'
        self.assertEqual(self.filled_maze_generation_service._find_starting_point(), (5,5))

    def test_find_starting_point_returns_none_with_no_starting_points(self):
        self.assertIsNone(self.filled_maze_generation_service._find_starting_point())

    def test_maze_does_not_override_rooms(self):
        self.map.occupy(2,2)
        self.maze_generation_service.init_maze()
        self.maze_generation_service.generate_perfect_maze()
        self.assertNotEqual(self.maze_generation_service._maze_cells[2][2], 'p')
