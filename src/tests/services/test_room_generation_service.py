import unittest
from services.room_generation_service import RoomGenerationService
from entities.room import Room

class TestRoomGenerationService(unittest.TestCase):
    def setUp(self):
        self.test_room_generation_service1 = RoomGenerationService()

    def test_the_right_kind_of_room_is_added_to_the_list(self):
        self.test_room_generation_service1.generate_room((1,2), 3, 4)
        room = Room((1,2), 3, 4)
        self.assertEqual(self.test_room_generation_service1.rooms[0], room)

    def test_the_correct_amount_of_random_rooms_is_generated(self):
        self.test_room_generation_service1.generate_random_rooms(10)
        self.assertEqual(len(self.test_room_generation_service1.rooms), 10)
        self.test_room_generation_service1.generate_random_rooms(20)
        self.assertEqual(len(self.test_room_generation_service1.rooms), 30)
