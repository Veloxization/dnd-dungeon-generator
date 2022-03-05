# Weekly Report 6
**Time spent:** 5.5 hours

New progress and new bugs this week!

Like stated in last week's report, I've added new adjustment options for the user in the GUI. I added a field that allows the user to specify how many rooms the program will attempt to create, and a field so that the user can name the saved files whatever they want. I also noted a bug with the GUI that didn't allow error messages to show, so I fixed that.

Other more minor changes happened in the docstring of the Map entity's class where I added a little bit more information on how two map regions can combine. I also removed an old band-aid solution for pruning disattached cells as the clearing of dead ends also does that.

The actual progress happened with the addition of room numbers. When the user generates a map now, a number will appear on the generated map in the upper left corner of each room. That works as a reference for the completely new feature: Game Master's Document, which I successfully managed to implement. Currently the document is relatively empty, only displaying its title and the numbered rooms.

However, the addition of that document means a lot for the development as it means I can move on to the next stage of development, mainly adding information to the document. I also overhauled the way the map image is generated. Previously the stages had to go in specific orders and would completely take over their areas of the map, replacing the black pixels of the background, and even each other. Now, everything is layered properly with added translucency. It also doesn't matter in which order each layer is drawn as the layer order is specified in the function that returns the image.

While I don't feel like I've learned anything new this week, I feel like there will be some reflection on my old code next week as I've noted a bug where some parts of the map are still generated completely disattached from the rest. I will have to find a way to either attach them to the rest of the map, delete them, or somehow utilise them as secret rooms.

Fixing the disattached rooms is certainly a priority as a reasonable connection between rooms was an early goal in the development and it working incorrectly is detrimental. If the fix ends up being simple, I'll move on with the GM's document by adding a new GUI element which allows the user to write desriptions for the rooms.