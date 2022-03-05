# Weekly Report 4
**Time spent:** 9 hours

I started this week's work by looking into various ways performance testing is done with Python, though I eventually ended up going with regular timing with Python's datetime library.

I also finally implemented the functionality that can generate rooms of random sizes and locations, including the necessary automated tests for it. I also expanded the test coverage by implementing more tests for older but untested parts of the program.

I found the reason why the maze generation algorithm was avoiding the edge walls and the walls of the rooms so much and managed to fix it so the space on the map is finally filled properly.

Even though I did not get it done this week, I started implementing the base for connecting the maze corridors into the rooms placed on the map. The map is divided into disconnected regions so making the connections is easier. I naturally also added this functionality's own automated tests as well.

In addition to all that, I also did some performance testing so I could expand the testing document, and I created the base for the implementation document.

The problems of the previous week have finally been solved and the maze properly fills up the map and the rooms are starting to get place now as well. Currently the program already forms a single connection between a room and a corridor, or two rooms. This week's problem, however, is making sure that _all_ rooms are properly connected to the maze instead of just one. The map has become really messy so far when additional connections have been made.

If there's anything I've taken from this week's attempts at solving last week's problems, I have noted that the order in which you specify the placement of new passages in a maze made by a randomized Prim's algorithm, matters.

Next week, will be another week of fixing issues, this time with the maze connecting to the rooms. I will also start removing the dead ends from the maze as those don't make engaging dungeons. Looking at the time and problems so far, I find it unlikely that I'll be able to start making the graphical user interface even next week, but I will do my best.