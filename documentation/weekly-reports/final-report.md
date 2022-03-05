# Final report
**Time spent:** 6.5 hours

**Time spent in total:** 48 hours

**Busiest week:** [Week 4](https://github.com/Veloxization/dnd-dungeon-generator/blob/main/documentation/weekly-reports/weekly-report-4.md) (9 hours)

There was no specific mention of having to write a weekly report for the final week but I decided to do it anyway just so I could document how finishing up the project has gone.

I ended up coming to the conclusion that having a correctly functioning program to demo was more important than adding more features from the backlog so this week has been spent focusing on bug fixes. This required a complete change in how I connect the maze to the rooms. Instead of having a (likely slow) method of making two connected regions into a single one, I now keep them as their own separate regions but keep track of which regions are connected to each other, either directly or indirectly. This seems to have fixed the issue of some rooms being completely disconnected from the maze, at least most of the time.

Because this kind of change required me to completely rewrite some methods, it also meant that I had to change the automated tests to reflect these changes. Due to this, I didn't have time to implement any more new features. I was aiming to at least have a feature that allows the user to write room descriptions from within the program and having that appear in the generated Game Master's text document. At the very least the game master's document is generated so the user _can_ still write descriptions, just not directly from the program.

In addition to bug fixes, I also tried to make the documentation more presentable. I specified and added some details where I deemed it necessary and I believe it is (at least mostly) up to date.

The program seems to be presentable now at the very least, and I feel comfortable demoing it. Tackling the bug of unconnected rooms this week was surprisingly difficult as it took me a while to figure out where the problem actually lied. My initial solution caused the "odds of loops" variable to sometimes be ignored until I added a form of path-finding to find out if you can already travel between two regions of the map.

With that said, developing all of this was surprisingly lot of work but I have also learned a lot during this time. Thank you for the course!