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

    def test_an_unoccupied_cells_status_changes_correctly(self):
        self.assertNotIn((0,0), self.test_map1.cells)
        self.test_map1.unoccupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,0)], Status.UNOCCUPIED)

    def test_an_unoccupied_cells_status_changes_correctly_when_status_is_unoccupied(self):
        self.test_map1.unoccupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,0)], Status.UNOCCUPIED)
        self.test_map1.occupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,0)], Status.OCCUPIED)

    def test_an_adjacent_occupied_cells_status_changes_correctly(self):
        self.assertNotIn((0,1), self.test_map1.cells)
        self.test_map1.occupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,1)], Status.ADJACENT_OCCUPIED)

    def test_an_adjacent_occupied_cell_can_become_occupied(self):
        self.test_map1.occupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,1)], Status.ADJACENT_OCCUPIED)
        self.test_map1.occupy(0,1)
        self.assertEqual(self.test_map1.cells[(0,1)], Status.OCCUPIED)

    def test_an_occupied_cell_cannot_become_adjacent_occupied(self):
        self.test_map1.occupy(0,0)
        self.assertEqual(self.test_map1.cells[(0,0)], Status.OCCUPIED)
        self.test_map1.occupy(0,1)
        self.assertEqual(self.test_map1.cells[(0,0)], Status.OCCUPIED)

    def test_a_cell_is_correctly_deemed_a_dead_end(self):
        self.test_map1.occupy(1,1)
        self.test_map1.occupy(1,2)
        self.assertTrue(self.test_map1.is_cell_dead_end(1,2))

    def test_a_cell_is_not_incorrectly_deemed_a_dead_end(self):
        self.test_map1.occupy(1,1)
        self.test_map1.occupy(1,2)
        self.test_map1.occupy(2,1)
        self.assertFalse(self.test_map1.is_cell_dead_end(1,1))
