# Testing document
This program has been automatically tested using pytest. Always up-to-date testing coverage percentage is available in the [README](https://github.com/Veloxization/dnd-dungeon-generator/blob/master/README.md). Instructions on running the tests and creating the complete coverage report in [MANUAL](https://github.com/Veloxization/dnd-dungeon-generator/blob/main/documentation/MANUAL.md).

## Coverage report
<img src="https://github.com/Veloxization/dnd-dungeon-generator/blob/main/documentation/images/coveragereport.png">

## What has been tested?
### entities/map
- The constructor assigns the map's height and width correctly
    - Tested with width of 10 and height of 20
- Corners have only two neighbours
    - Tested with the top left corner
- Edges have only three neighbours
    - Tested with the top edge
- Other cells have four neighbours
    - Tested with the cell in coordinates (1,1)
- When a cell is marked occupied, its status changes correctly
    - Tested by changing the status of the top left corner
- When a cell is marked unoccupied, its status changes correctly
    - Tested by changing the status of the top left corner
- When a cell is unoccupied and it's changed to occupied, thet status changes correctly
    - Tested by changing the status of the top left corner to unoccupied and then occupied
- When a cell is marked occupied, the adjacent cells are marked with an adjacent occupied cell
    - Tested by changing the top left corner's status to occupied and then checking the status of the cell below it
- When a cell has an adjacent occupied cell, it can also become occupied
    - Tested by occupying the top left corner and checking if the cell below it also becomes occupied when changed
- When a cell is occupied, it can't be marked as having an adjacent occupied cell
    - Tested by first occupying the top left corner, then occupying the cell below it and checking that the top left corner's status does not change
- When a cell has one or less neighbours, it is considered a dead end
    - Tested by occupying cells (1,1) and (1,2), then checking that (1,2) is considered a dead end
- When a cell has more than one neighbour, it is not considered a dead end
    - Tested by occupying cells (1,1), (1,2) and (2,1) and checking that (1,1) is not considered a dead end
- When a cell that has two occupied neighbors has one neighbor marked unoccupied, the cell itself does not become unoccupied
    - Tested by occupying cells (1,1) and (1,3) and then unoccupying cell (1,1) and checking that cell (1,2) between them didn't get unoccupied
- When a cell gets unoccupied, its adjacent neighbors also get unoccupied
    - Tested by occupying cell (1,1) and checking that the cells around it turn into unoccupied cells after cell (1,1) is unoccupied
### services/drawing_service
- When a room's right edge extends beyond the right edge of the map, it's not drawn
    - Tested by drawing a 2x2 room to coordinates (49,1) on a 50x50 map and checking that it can't be drawn
- When a room's bottom edge extends beyond the bottom edge of the map, it's not drawn
    - Tested by drawing a 2x2 room to coordinates (1,49) and checking that it can't be drawn
- When an attempt is made to draw a room on top of an existing room, it fails
    - Tested by drawing 2x2 rooms to coordinates (1,1) and (2,2) and checking that the latter is not generated
- A room can be drawn on an unoccupied space
    - Tested by drawing a 2x2 room to coordinates (1,1)
- A cell's coordinates are converted to pixel coordinates correctly
    - Tested by checking that with 20x20-pixel cells, the given coordinates for cell (1,1) are given as (20,20)
- A valid room will be drawn on the map image
    - Tested by checking that a mock object's room drawing function is called when attempting to draw a 2x2 room at coordinates (1,1)
- An invalid room will not be drawn on the map image
    - Tested by checking that a mock object's room drawing function is not called when attempting to draw a 2x2 room at coordinates(1,49)
- The movement grid is drawn with the correct line thickness
    - Tested by checking that a mock object's grid drawing function is called with the correct line thickness of 2
- When trying to get the map image object, the function of the image generation service is called correctly
    - Tested by checking that a mock object's generated image getter function is called
- Corridors are placed in the correct spots on the map image
    - Tested by first checking that a corridor drawn to coordinates (1,1) called an image generation service mock object for coordinates (20, 20) and coordinates (1,2) for (20,40)
- Room numbers are placed in the correct spots on the map image
    - Tested by creating a 2x2 room at coordinates (2,3) with a cell size of 20x20, and checking that image generation service's mock object is called with coordinates 2\*20=40, 3\*20=60 and with a font size of 20, and that the drawn text is "1"
- If only one of the generated rooms is valid, only one number will be drawn
    - Tested by creating 2x2 rooms at coordinates (1,1) and (1,2) so they would overlap. Then checking that image generation service's mock object's draw_text function is called only once
- The amount of numbers matches the number of rooms generated
    - Tested by placing two valid rooms at coordinates (1,1) and (3,3) and then checking that the latest call to image generation service's mock object happens with the drawn text of "2"
### services/maze_generation_service
- When a maze is initialized, the rooms added on the map will appear in the maze surrounded by walls
    - Tested by checking that a room generated at coordinates (1,1) will also be marked at coordinates (1,1) and all the adjacent cells are marked as walls
- When a wall is added, it's correctly reflected in the maze cells
    - Tested by checking that the cell at (1,1) changes to a wall when it's added there
- When a passage is added, it's correctly reflected in the maze cells and surrounded by walls
    - Tested by checking that the cell at (1,1) changes into a passage when added, and that the adjacent cells are turned into walls
- Once a passage is placed, it cannot be replaced by a wall
    - Tested by placing a passage at (1,1) and trying to change the same cell into a wall
- Once a wall is placed, it can be replace by a passage
    - Tested by placing a wall at (1,1) and trying to replace it with a passage, making sure that the wall is removed from the list of walls
- The amount of non-diagnonally adjacent passages is calculated correctly
    - Tested by placing new passages around a certain point and checking that the amount increases accordingly
- When looking for a starting cell for a maze, it's correctly found
    - Tested with a maze filled with walls and cell (5,5) replaced by an unvisited marker, then checking that its coordinates are found correctly
- When there are no valid starting points, the starting point searching function returns _None_
    - Tested with a maze filled with walls and checking that the starting point searching function returns _None_
- When a full maze is generated, no passages will override an already placed room
    - Tested by occupying cell (2,2) and having that act as a room, then checking that a generated maze does not replace this cell
- When there's a passage on the left and a room on the right with a wall between them, it is considered a valid place for a connection
    - Tested by occupying cell (3,3) on the map as a room and then adding a passage to (1,3) and checking whether the wall in between is considered a connection
- When there's a passage on the right and a room on the left with a wall between them, it is considered a valid place for a connection
    - Tested by occupying cell (1,3) on the map as a room and then adding a passage to (3,3) and checking whether the wall in between is considered a connection
- When there's a passage above and a room below with a wall between them, it is considered a valid place for a connection
    - Tested by occupying cell (3,3) on the map as a room and then adding a passage to (3,1) and checking whether the wall in between is considered a connection
- When there's a passage below and a room above with a wall between them, it is considered a valid place for a connection
    - Tested by occupying cell (3,1) on the map as a room and then adding a passage to (3,3) and checking whether the wall in between is considered a connection
- If a cell is not a wall, it is not considered a valid place for a connection
    - Tested by placing a passage at coordinates (1,1) and a room at coordinates(1,3) and checking that the unvisited cell in between is not considered a connection
- If nothing has been added to the map, the number of connections is 0
    - Tested by creating an empty map and checking for valid connections, expecting the number of connections to be 0
- If there are three rooms with walls between them, the number of valid connections
    - Tested by creating 1x1 rooms at coordinates (1,1), (1,3) and (3,1), then checking the number of valid connections, expecting 2
- The first connection is drawn correctly
    - Tested by creating 1x1 rooms at coordiantes (1,1) and (1,3), then checking if the cell between them becomes a passage when connections are searched
- When odds of loops is 0, only one connection to the room is made
    - Tested by creating a 6x6 map, placing a room at coordinates (2,3), creating passages with two possible connections around it, and checking that only one of those connections is used
- When odds of loops is 1, all possible connections are made
    - Tested by creating a 6x6 map, placing a room at coordinates (2,3), creating passages with two possible connections around it, and checking that both of those connections are used
- When there are two possible ways to make connections between two regions, only one of those connections is used if the odds of loops is 0
    - Tested by creating two 1x1 rooms at coordinates (1,1) and (1,3) and then stretching a hallway next to the two (coordinates (3,1), (3,2), (3,3)) and checking that only two of the possible connections is filled with passages
- Dead ends are pruned from the corridors correctly
    - Tested by placing 1x1 rooms at coordinates (1,1) and (5,1) and building a corridor in between them, with a small branching dead end in the middle of it, pruning dead ends and checking that the dead end cell is turned into a wall
### services/room_generation_service
- When a room is added, it's correctly added into the list of rooms
    - Tested by generating a room in coordinates (1,2) with the width of 3 and height of 4, and checking that it's added to a list of rooms
- When rooms are randomly generated, the amount of rooms is correct
    - Tested by first generating 10 random rooms and checking that the amount of rooms is 10, then generating 20 additional rooms and checking that the amount is 30
### services/room_data_generation_service
- If there are no rooms on the map, the list of placed rooms remains empty
    - Tested by initializing a room data generation service object and not adding any rooms to the attributed room generation service object
- If there is a single generated room, it is added to the list of placed rooms
    - Tested by adding a single room marked as generated in the attributed room generation service object and checking that the list of placed rooms has a single object
- If there are rooms but none of them are generated, they will not become placed rooms
    - Tested by adding a single room marked as not generated and checking that the number of placed rooms remains at 0
- If there are no rooms on the map, no data will appear
    - Tested by not adding any rooms and checking that the amount of data on the data list is 0
- A placed room has its number displayed correctly
    - Tested by placing a single room and checking that its associated data displays the number 1
- If data is empty, the string presentation is formatted correctly
    - Tested by printing the empty data and checking that it only contains the name, the text "GM Document" and ends with two line breaks
- If there is a single room, it appears in the string presentation of the data correctly
    - Tested by placing a single room and checking that the string representation of the data includes the text for "Room 1"
## Performance test results
**Map:** 100x100    **Room generation attempts:** 100   **Repeats:** 1000
### Initialize map
0.001062 ms
### Initialize room generation service
0.000968 ms
### Generate random rooms
0.230440 ms
### Initialize drawing service
0.347949 ms
### Draw rooms
0.000900 ms
### Initialize maze generation service
0.384006 ms
### Initialize maze
0.677761 ms
### Generate a perfect maze
0.223764 ms
### Connect maze to rooms
0.340917 ms
### Prune dead ends from the dungeon
0.332636 ms
### Draw corridors
0.045636 ms
### Draw grid
0.832158 ms
### Draw room numbers
0.005694 ms
### Initialize room data generation service
0.062727 ms
### Initialize room data
0.000788 ms
## Performance test breakdown
<img src="https://github.com/Veloxization/dnd-dungeon-generator/blob/main/documentation/images/performancechart.png">
