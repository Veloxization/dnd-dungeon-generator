# Weekly Report 2
**Time spent:** 8 hours

I have successfully met my goals for this week, and more. I started my work by writing the [user stories](https://github.com/Veloxization/dnd-dungeon-generator/blob/main/documentation/userstories.md) like I planned to do last week. This is going to make it considerably easier to tackle each individual goal on coming weeks.

Since coming up with the user stories was so easy in the end, I went ahead and started preparing for writing the code by configuring *Poetry, Pytest, Coverage* and *Pylint* for ease of use, automated testing, testing coverage reporting and style check respectively. I also had to separately refresh my memory on how Pytest and Coverage work and how to configure them to my liking.

With the configuration out of the way, I could start tackling coding. The user stories I wrote really helped in deciding what to start with, and at the bottom was an image generator. I decided to use the *Pillow* library as that's familiar to me. To help with the dungeon generation, I also made classes that keep track of the different rooms of the dungeon and the "cells" occupied on the dungeon map.

I didn’t want to leave automated testing halfway done so I created new tests as I created the functionalities, with the goal of having as high a testing coverage as reasonably possible.

I got frustrated having to write the same commands through Poetry repeatedly to run tests etc. so I decided to also implement the *Invoke* library into my project so it's easier to run the commands I run often. I also made a user manual, so others also know about these easy tasks.

To finish off the work for this week, I also configured GitHub Actions and Codecov and their respective badges to show off the results of tests and their coverage.

From last week's zero code to actual functional classes, I can say there has been an improvement with the project, as much as I was skeptical about it sometimes.

As to what I've learned this week, I now know how important it is to somewhat plan ahead when creating functions and classes and the automated testing for them. Values need to be easily modified so expanding the program does not add impossible amount of work. I could claim that this has been something that has been evolving throughout different projects I've worked on.

This week's work was surprisingly smooth. I had a small hiccup while setting up Poetry and its dependencies, which was easily fixed by updating it to the latest version. Another slightly difficult thing was planning the class structure, i.e., where to put different functions.

For next week, I am planning to finish up the rest of the tests I have planned for the already created classes, especially the couple that need mock class objects to work. I must also investigate Prim's algorithm to create the dungeon corridors and their connections to the rooms. If this is not enough work, I have more things down the line of user stories, namely creating the graphical user interface and giving the user actual control on how the program works.