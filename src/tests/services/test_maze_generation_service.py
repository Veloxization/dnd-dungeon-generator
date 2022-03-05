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

    def test_a_passage_on_the_left_is_connected_to_a_room_on_the_right(self):
        self.map.occupy(3,3)
        self.maze_generation_service.init_maze()
        self.maze_generation_service._add_passage((1,3))
        self.assertEqual(self.maze_generation_service._get_connection((2,3)), (1,0))

    def test_a_passage_on_the_right_is_connected_to_a_room_on_the_left(self):
        self.map.occupy(1,3)
        self.maze_generation_service.init_maze()
        self.maze_generation_service._add_passage((3,3))
        self.assertEqual(self.maze_generation_service._get_connection((2,3)), (1,0))

    def test_a_passage_above_is_connected_to_a_room_below(self):
        self.map.occupy(3,3)
        self.maze_generation_service.init_maze()
        self.maze_generation_service._add_passage((3,1))
        self.assertEqual(self.maze_generation_service._get_connection((3,2)), (1,0))

    def test_a_passage_below_is_connected_to_a_room_above(self):
        self.map.occupy(3,1)
        self.maze_generation_service.init_maze()
        self.maze_generation_service._add_passage((3,3))
        self.assertEqual(self.maze_generation_service._get_connection((3,2)), (1,0))

    def test_non_walls_are_not_considered_connections(self):
        self.maze_generation_service.init_maze()
        self.maze_generation_service._maze_cells[1][1] = 'p'
        self.maze_generation_service._maze_cells[1][3] = 'r'
        self.assertIsNone(self.maze_generation_service._get_connection((1,2)))

    def test_if_the_map_is_empty_there_are_no_connections(self):
        self.maze_generation_service.init_maze()
        self.assertEqual(len(self.maze_generation_service._get_connections()), 0)

    def test_the_correct_number_of_connections_is_established(self):
        self.map.occupy(1,1)
        self.map.occupy(1,3)
        self.map.occupy(3,1)
        self.maze_generation_service.init_maze()
        self.assertEqual(len(self.maze_generation_service._get_connections()), 2)

    def test_initial_connection_is_correctly_drawn(self):
        self.map.occupy(1,1)
        self.map.occupy(1,3)
        self.maze_generation_service.init_maze()
        self.assertEqual(self.maze_generation_service._maze_cells[1][2], 'w')
        self.maze_generation_service.connect_maze_to_rooms()
        self.assertEqual(self.maze_generation_service._maze_cells[1][2], 'p')

    def test_only_one_connection_is_made_if_odds_of_loops_is_zero(self):
        map_test = Map(6,6)
        map_test.occupy(2,3)
        maze_gen = MazeGenerationService(map_test)
        maze_gen.init_maze()
        maze_gen._add_passage((2,1))
        maze_gen._add_passage((3,1))
        maze_gen._add_passage((4,1))
        maze_gen._add_passage((4,2))
        maze_gen._add_passage((4,3))
        # Map reference:
        # [['u','u','u','u','u','u'],
        #  ['u','w','u','w','u','u'],
        #  ['w','p','w','r','w','u'],
        #  ['w','p','w','w','u','u'],
        #  ['w','p','p','p','w','u'],
        #  ['u','w','w','w','u','u']]
        self.assertEqual(maze_gen._maze_cells[2][2], maze_gen._maze_cells[3][3])
        maze_gen.connect_maze_to_rooms(0)
        self.assertNotEqual(maze_gen._maze_cells[2][2], maze_gen._maze_cells[3][3])

    def test_all_possible_connections_are_made_if_odds_of_loops_is_one(self):
        map_test = Map(6,6)
        map_test.occupy(2,3)
        maze_gen = MazeGenerationService(map_test)
        maze_gen.init_maze()
        maze_gen._add_passage((2,1))
        maze_gen._add_passage((3,1))
        maze_gen._add_passage((4,1))
        maze_gen._add_passage((4,2))
        maze_gen._add_passage((4,3))
        self.assertEqual(maze_gen._maze_cells[2][2], maze_gen._maze_cells[3][3])
        maze_gen.connect_maze_to_rooms(1)
        self.assertEqual(maze_gen._maze_cells[2][2], maze_gen._maze_cells[3][3])

    def test_dead_ends_are_pruned_correctly(self):
        self.map.occupy(1,1)
        self.map.occupy(5,1)
        self.maze_generation_service.init_maze()
        self.maze_generation_service._add_passage((2,1))
        self.maze_generation_service._add_passage((3,1))
        self.maze_generation_service._add_passage((3,2))
        self.maze_generation_service._add_passage((4,1))
        self.assertEqual(self.maze_generation_service._maze_cells[3][2], 'p')
        self.maze_generation_service.prune_dead_ends()
        self.assertEqual(self.maze_generation_service._maze_cells[3][2], 'w')
