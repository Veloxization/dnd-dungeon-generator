from tkinter import *
from tkinter import ttk
from entities.map import Map
from services.room_generation_service import RoomGenerationService
from services.maze_generation_service import MazeGenerationService
from services.drawing_service import DrawingService
from services.room_data_generation_service import RoomDataGenerationService
from repositories.map_repository import MapRepository
from repositories.gm_document_repository import GMDocumentRepository

class MainGUI:
    """The main GUI class handling opening of the basic view of the GUI.

    Attributes:
        cell_dimensions: The width and height of a cell in pixels
        map_width: The width of the map in cells
        map_height: The height of the map in cells
        room_min_width: The minimum width of a room in cells
        room_min_height: The minimum height of a room in cells
        room_max_width: The maxiumum width of a room in cells
        room_max_height: The maximum height of a room in cells
        loop_probability: The probability of loops in the dungeon, 0-1
        error_message: Whatever system messages need to be displayed
        error_message_label: The label for the system messages
    """

    def __init__(self):
        """Create a new MainGUI object"""

        root = Tk()
        root.title("D&D Dungeon Generator")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        scaleframe = ttk.Frame(root, padding="3 3 12 12")
        scaleframe.grid(column=0, row=1, sticky=(N, W, E, S))
        filenameframe = ttk.Frame(root, padding="3 3 12 12")
        filenameframe.grid(column=0, row=2, sticky=(N, W, E, S))
        buttonframe = ttk.Frame(root, padding="3 3 12 12")
        buttonframe.grid(column=0, row=3)
        errorframe = ttk.Frame(root, padding="3 3 12 12")
        errorframe.grid(column=0, row=4)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # INPUTS
        self.cell_dimensions = IntVar(value=5)
        cell_dimensions_entry = ttk.Entry(mainframe,
                                          width=7,
                                          textvariable=self.cell_dimensions)
        cell_dimensions_entry.grid(column=2, row=1, sticky=(W, E))

        self.map_width = IntVar(value=20)
        map_width_entry = ttk.Entry(mainframe,
                                    width=7,
                                    textvariable=self.map_width)
        map_width_entry.grid(column=2, row=2, sticky=(W, E))
        self.map_height = IntVar(value=20)
        map_height_entry = ttk.Entry(mainframe,
                                     width=7,
                                     textvariable=self.map_height)
        map_height_entry.grid(column=4, row=2, sticky=(W, E))

        self.room_min_width = IntVar(value=2)
        room_min_width_entry = ttk.Entry(mainframe,
                                         width=7,
                                         textvariable=self.room_min_width)
        room_min_width_entry.grid(column=2, row=3, sticky=(W, E))
        self.room_min_height = IntVar(value=2)
        room_min_height_entry = ttk.Entry(mainframe,
                                          width=7,
                                          textvariable=self.room_min_height)
        room_min_height_entry.grid(column=4, row=3, sticky=(W, E))

        self.room_max_width = IntVar(value=5)
        room_max_width_entry = ttk.Entry(mainframe,
                                         width=7,
                                         textvariable=self.room_max_width)
        room_max_width_entry.grid(column=2, row=4, sticky=(W, E))
        self.room_max_height = IntVar(value=5)
        room_max_height_entry = ttk.Entry(mainframe,
                                          width=7,
                                          textvariable=self.room_max_height)
        room_max_height_entry.grid(column=4, row=4, sticky=(W, E))

        self.room_generation_attempts = IntVar(value=100)
        room_generation_attempts_entry = ttk.Entry(mainframe,
                                                   width=7,
                                                   textvariable=self.room_generation_attempts)
        room_generation_attempts_entry.grid(column=2, row=5, sticky=(W, E))

        self.loop_probability = DoubleVar(value=0.50)
        loop_probability_scale = ttk.Scale(scaleframe,
                                           orient=HORIZONTAL,
                                           length=200,
                                           from_=0.0,
                                           to=1.0,
                                           variable=self.loop_probability)
        loop_probability_scale.grid(column=3, row=1, sticky=(W, E))

        self.file_name = StringVar(value="map")
        file_name_entry = ttk.Entry(filenameframe,
                                    width=7,
                                    textvariable=self.file_name)
        file_name_entry.grid(column=2, row=1, sticky=(W, E))

        # ENTRY LABELS
        cell_dimensions_label = ttk.Label(mainframe, text="Square width and height")
        cell_dimensions_label.grid(column=1, row=1)

        map_dimensions_label = ttk.Label(mainframe, text="Map dimensions")
        map_dimensions_label.grid(column=1, row=2)

        room_min_dimensions_label = ttk.Label(mainframe, text="Room min dimensions")
        room_min_dimensions_label.grid(column=1, row=3)

        room_max_dimensions_label = ttk.Label(mainframe, text="Room max dimensions")
        room_max_dimensions_label.grid(column=1, row=4)

        room_generation_attempts_label = ttk.Label(mainframe, text="Room generation attempts")
        room_generation_attempts_label.grid(column=1, row=5)

        loop_probability_label = ttk.Label(scaleframe, text="Likelihood of loops")
        loop_probability_label.grid(column=1, row=1)

        file_name_label = ttk.Label(filenameframe, text="Map file name")
        file_name_label.grid(column=1, row=1)

        # DIVIDER LABELS
        map_dimensions_divider = ttk.Label(mainframe, text="x")
        map_dimensions_divider.grid(column=3, row=2)

        room_min_dimensions_divider = ttk.Label(mainframe, text="x")
        room_min_dimensions_divider.grid(column=3, row=3)

        room_max_dimensions_divider = ttk.Label(mainframe, text="x")
        room_max_dimensions_divider.grid(column=3, row=4)

        # UNIT LABELS
        cell_dimensions_unit = ttk.Label(mainframe, text="px")
        cell_dimensions_unit.grid(column=3, row=1)

        map_dimensions_unit = ttk.Label(mainframe, text="squares")
        map_dimensions_unit.grid(column=5, row=2)

        room_min_dimensions_unit = ttk.Label(mainframe, text="squares")
        room_min_dimensions_unit.grid(column=5, row=3)

        room_max_dimensions_unit = ttk.Label(mainframe, text="squares")
        room_max_dimensions_unit.grid(column=5, row=4)

        loop_probability_unit_left = ttk.Label(scaleframe, text="None")
        loop_probability_unit_left.grid(column=2, row=1)

        loop_probability_unit_right = ttk.Label(scaleframe, text="All")
        loop_probability_unit_right.grid(column=4, row=1)

        file_extension = ttk.Label(filenameframe, text=".png")
        file_extension.grid(column=3, row=1)

        # SCALE VALUES
        loop_probability_value = ttk.Label(scaleframe, textvariable=self.loop_probability)
        loop_probability_value.grid(column=3, row=2)

        # BUTTONS
        generate_button = ttk.Button(buttonframe,
                                     text="Generate dungeon",
                                     command=self.validate_and_start)
        generate_button.grid(column=1, row=1)

        # ERROR MESSAGES
        self.error_message = StringVar()
        self.error_message_label = ttk.Label(errorframe,
                                        textvariable=self.error_message,
                                        foreground="red")
        self.error_message_label.grid(column=1, row=1)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in scaleframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        root.mainloop()

    def validate_and_start(self):
        """Validate user inputs and start if they're correct"""
        err = False
        try:
            cell_dimensions = self.cell_dimensions.get()
        except TclError as error:
            self.error_message.set(f"Square width and height: {error}")
            err = True
        try:
            map_width = self.map_width.get()
            map_height = self.map_height.get()
        except TclError as error:
            self.error_message.set(f"Map dimensions: {error}")
            err = True
        try:
            room_min_width = self.room_min_width.get()
            room_min_height = self.room_min_height.get()
        except TclError as error:
            self.error_message.set(f"Room min dimensions: {error}")
            err = True
        try:
            room_max_width = self.room_max_width.get()
            room_max_height = self.room_max_height.get()
        except TclError as error:
            self.error_message.set(f"Room max dimensions: {error}")
            err = True
        try:
            room_generation_attempts = self.room_generation_attempts.get()
        except TclError as error:
            self.error_message.set(f"Room generation attempts: {error}")
            err = True
        try:
            odds_of_loops = self.loop_probability.get()
        except TclError as error:
            self.error_message.set(f"Likelihood of loops: {error}")
            err = True
        if not err:
            self.error_message_label.config(foreground="black")
            self.error_message.set("Generating dungeon...")
            self._start_generation(cell_dimensions,
                                map_width,
                                map_height,
                                room_min_width,
                                room_min_height,
                                room_max_width,
                                room_max_height,
                                room_generation_attempts,
                                odds_of_loops)

    def _start_generation(self, cell_dim, map_w, map_h, room_min_w, room_min_h, room_max_w, room_max_h, room_gen_attempts, loop_odds):
        """Start the generation of the dungeon

        Args:
            cell_dim: The width and height of a cell will share the same value
            map_w: The width of the map in squares
            map_h: The height of the map in squares
            room_min_w: The minimum width of a room in squares
            room_min_h: The minimum height of a room in squares
            room_max_w: The maximum width of a room in squares
            room_max_h: The maximum height of a room in squares
            room_gen_attempts: How many rooms will the program attempt to generate
            loop_odds: The likelihood of loops in the dungeon, i.e. the imperfectness of the maze
        """
        map_obj = Map(map_w, map_h)
        room_gen = RoomGenerationService(cell_dim, cell_dim, map_w, map_h)
        room_gen.generate_random_rooms(room_gen_attempts,
                                       room_min_w,
                                       room_max_w,
                                       room_min_h,
                                       room_max_h)
        drawing = DrawingService(room_gen, map_obj, (cell_dim, cell_dim))
        drawing.draw_rooms()
        maze_gen = MazeGenerationService(map_obj)
        maze_gen.init_maze()
        maze_gen.generate_perfect_maze()
        maze_gen.connect_maze_to_rooms(loop_odds)
        maze_gen.prune_dead_ends()
        drawing.draw_corridors()
        drawing.draw_grid()
        drawing.draw_room_numbers()
        err = False
        try:
            MapRepository(drawing.get_image()).save(f"demo/{self.file_name.get()}")
        except OSError as error:
            self.error_message_label.config(foreground="red")
            self.error_message.set(f"Map file name: {error}")
            err = True
        if not err:
            self.error_message_label.config(foreground="green")
            self.error_message.set(f"Generated dungeon saved to demo/{self.file_name.get()}.png")
        data_gen = RoomDataGenerationService(room_gen)
        data_gen.init_data()
        doc_repo = GMDocumentRepository(self.file_name.get())
        doc_repo.write_data(data_gen.print_data(self.file_name.get()))
