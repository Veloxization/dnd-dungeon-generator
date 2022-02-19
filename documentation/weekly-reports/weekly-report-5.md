# Weekly Report 5
**Time spent:** 7 hours

I seem to have underestimated myself in my last week's report. The amount of work I got done was much more than I anticipated. The corridors now properly connect to rooms *and* I managed to also prune the dead ends out from the maze utilizing good old depth-first search, meaning the map now looks like a proper dungeon with its rooms and corridors. Since that went without much issues and there was time remaining, I decided to also look into Tkinter since I have barely used it before.

The usage of Tkinter was relatively easy to understand as I've utilized something similar before. That meant that I could go straight into building a GUI for my program. The GUI immediately got controls for specifying the width and height of a single cell of a dungeon in pixels, as well as the width and height of the map and the rooms. I also added a slider so the user can specify how likely it is for their dungeon to have looping paths in it.

On the documentation side, I naturally included the instructions for using the new GUI. I also added a bit more detail to the abandoned implementation document. It still needs a bit more work but it's something!

The program has returned on its previous fast improvement path. The dungeons it generates actually look like dungeons now, and now just a maze in between unattached rooms. Not to mention the GUI, giving the user some sort of control over what kind of dungeon the program generates.

The main thing I learned this week was probably how to use Tkinter. As long as I've been using Python, I seem to have always skirted around building actualy GUIs beyond Pygame. Luckily it was easy to learn and getting started with it offered no trouble.

That said, the main issue I had this week was also with Tkinter. Since I implemented the slider for the odds of loops in the dungeon, I wanted it to have increments of 0.01. There seems to have been a "resolution" option for sliders (or "Scales" as they're called internally) in some version of Tkinter but that seems to not work anymore, or if it does, I was trying to get it working the wrong way.

For next week, I still have some GUI elements to add. I had somehow completely forgotten about the many options I wanted to be customizable and I need to add those. If that goes without much hassle, I'll move on with the user stories I've prepared and make it so the program can assign numbers to the rooms and display them on the map. It is necessary for the Game Master's text document I want the program to also generate. If there is time, I will likely also implement the starting point of this text document.