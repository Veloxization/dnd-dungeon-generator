from datetime import datetime
from datetime import timedelta
from entities.map import Map
from services.room_generation_service import RoomGenerationService
from services.maze_generation_service import MazeGenerationService
from services.drawing_service import DrawingService
from repositories.map_repository import MapRepository

def main():
    cell_width = 10
    cell_height = 10
    map_width = 100
    map_height = 100
    rooms_to_generate = 100
    room_min_width = 5
    room_max_width = 10
    room_min_height = 5
    room_max_height = 10
    odds_of_loops = 0.05
    map_obj = Map(map_width, map_height)
    room_gen = RoomGenerationService(cell_width, cell_height, map_width, map_height)
    room_gen.generate_random_rooms(rooms_to_generate, room_min_width, room_max_width, room_min_height, room_max_height)
    drawing = DrawingService(room_gen, map_obj, (cell_width, cell_height))
    drawing.draw_rooms()
    maze_gen = MazeGenerationService(map_obj)
    maze_gen.init_maze()
    maze_gen.generate_perfect_maze()
    maze_gen.connect_maze_to_rooms(odds_of_loops)
    maze_gen.prune_dead_ends()
    drawing.draw_corridors()
    drawing.draw_grid()
    MapRepository(drawing.get_image()).save("demo/test")

    #print(performance_test())

def performance_test():
    cell_width = 5
    cell_height = 5
    map_width = 100
    map_height = 100
    rooms_to_generate = 100
    room_min_width = 5
    room_max_width = 20
    room_min_height = 5
    room_max_height = 20
    odds_of_loops = 0.5

    repeats = 50
    totals = {"map init": timedelta(0),
    "room gen service init": timedelta(0),
    "random room generation": timedelta(0),
    "maze gen service init": timedelta(0),
    "maze init": timedelta(0),
    "perfect maze gen": timedelta(0),
    "connect maze to rooms": timedelta(0)}
    for i in range(repeats):
        start_time = datetime.now()
        map_obj = Map(map_width, map_height)
        end_time = datetime.now()
        totals["map init"] += end_time - start_time

        start_time = datetime.now()
        room_gen = RoomGenerationService(cell_width, cell_height, map_width, map_height)
        end_time = datetime.now()
        totals["room gen service init"] += end_time - start_time

        start_time = datetime.now()
        room_gen.generate_random_rooms(rooms_to_generate, room_min_width, room_max_width, room_min_height, room_max_height)
        end_time = datetime.now()
        totals["random room generation"] += end_time - start_time

        start_time = datetime.now()
        maze_gen = MazeGenerationService(map_obj)
        end_time = datetime.now()
        totals["maze gen service init"] += end_time - start_time

        start_time = datetime.now()
        maze_gen.init_maze()
        end_time = datetime.now()
        totals["maze init"] += end_time - start_time

        start_time = datetime.now()
        maze_gen.generate_perfect_maze()
        end_time = datetime.now()
        totals["perfect maze gen"] += end_time - start_time

        start_time = datetime.now()
        maze_gen.connect_maze_to_rooms(odds_of_loops)
        end_time = datetime.now()
        totals["connect maze to rooms"] += end_time - start_time

    totals["map init"] = (totals["map init"].microseconds / repeats) / 1000
    totals["room gen service init"] = (totals["room gen service init"].microseconds / repeats) / 1000
    totals["random room generation"] = (totals["random room generation"].microseconds / repeats) / 1000
    totals["maze gen service init"] = (totals["maze gen service init"].microseconds / repeats) / 1000
    totals["maze init"] = (totals["maze init"].microseconds / repeats) / 1000
    totals["perfect maze gen"] = (totals["perfect maze gen"].microseconds / repeats) / 1000
    totals["connect maze to rooms"] = (totals["connect maze to rooms"].microseconds / repeats) / 1000

    return str(totals)

if __name__ == "__main__":
    main()
