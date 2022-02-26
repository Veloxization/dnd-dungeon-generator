import unittest
from entities.room import Room
from services.room_generation_service import RoomGenerationService
from services.room_data_generation_service import RoomDataGenerationService

class TestDrawingService(unittest.TestCase):
    def setUp(self):
        self.room_generation_service = RoomGenerationService()
        self.empty_data_generation_service = RoomDataGenerationService(self.room_generation_service)
        room = Room((1,1))
        room.is_generated = True
        room_gen = RoomGenerationService()
        room_gen.rooms.append(room)
        self.data_generation_service = RoomDataGenerationService(room_gen)

    def test_if_there_are_no_rooms_placed_rooms_remains_empty(self):
        self.assertEqual(len(self.empty_data_generation_service._placed_rooms), 0)

    def test_number_of_placed_rooms_displayed_correctly(self):
        self.assertEqual(len(self.data_generation_service._placed_rooms), 1)

    def test_a_non_generated_room_is_not_a_placed_room(self):
        room = Room((1,1))
        self.room_generation_service.rooms.append(room)
        data_gen = RoomDataGenerationService(self.room_generation_service)
        self.assertEqual(len(data_gen._placed_rooms), 0)

    def test_if_there_are_no_rooms_data_remains_empty(self):
        self.empty_data_generation_service.init_data()
        self.assertEqual(len(self.empty_data_generation_service._data), 0)

    def test_rooms_number_is_displayed_correctly_in_the_data(self):
        self.data_generation_service.init_data()
        self.assertEqual(self.data_generation_service._data[0][0], 1)

    def test_empty_data_is_formatted_correctly(self):
        self.empty_data_generation_service.init_data()
        self.assertEqual(self.empty_data_generation_service.print_data("test"), "test - GM Document\n\n")

    def test_data_with_one_room_is_formatted_correctly(self):
        self.data_generation_service.init_data()
        self.assertEqual(self.data_generation_service.print_data("test"), "test - GM Document\n\nRoom 1\n\n")