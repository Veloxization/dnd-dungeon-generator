import unittest
from entities.map import Map, Status

class TestMap(unittest.TestCase):
    def setUp(self) -> None:
        self.test_map1 = Map(10, 20)

    def test_the_map_objects_width_and_height_are_assigned_correctly(self):
        self.assertAlmostEqual(self.test_map1.map_width, 10)
        self.assertAlmostEqual(self.test_map1.map_height, 20)

    def test_the_top_left_corner_only_has_two_neighbours(self):
        self.assertEqual(len(self.test_map1._get_adjacent_cells(0, 0)), 2)

    def test_an_edge_cell_has_three_neighbours(self):
        self.assertEqual(len(self.test_map1._get_adjacent_cells(0,1)), 3)

    def test_a_middle_cell_has_four_neighbours(self):
        self.assertEqual(len(self.test_map1._get_adjacent_cells(1, 1)), 4)

    def test_an_occupied_cells_status_changes_correctly(self):
        self.assertNotIn((0,0), self.test_map1.cells)
        self.test_map1.occupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,0)], Status.OCCUPIED)

    def test_an_adjacent_occupied_cells_status_changes_correctly(self):
        self.assertNotIn((0,1), self.test_map1.cells)
        self.test_map1.occupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,1)], Status.ADJACENT_OCCUPIED)
