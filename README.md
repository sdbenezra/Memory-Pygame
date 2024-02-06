# Memory Game
## Created with Python and Pygame

Code developed with this Youtube video https://youtu.be/IzsX89ZYGT0?si=2Ck2oSUSsQPhH7_V.  
This repository is part of a larger project during which I will attempt to create several
versions of the classic memory game using various frameworks for creating web apps with Python. 
Some of the frameworks I plan to explore include:

  1. Pygame (Python library for game creation).
  2. Reflex (Create web apps, including front and backend, fully in Python).
  3. Pyscript (Another tool for creating web apps with Python - from the Anaconda folks - can host on Pyscript.com)
  4. Flex (It's like Flutter for Python).
  5. Pygbag (This tool uses Webassembly to compile your Python code to a binary code format that will run in the browser)

## Deploying Memory-Pygame
Now that the basic game is completed I am going to deploy it in Github pages using Pygbag. I will document the process
below as I go.

2/5/24
Success! I deployed the game to Github pages using information from [this Medium Post](https://medium.com/@msgold/from-desktop-to-web-deploying-pygame-projects-with-pybag-a4344a7e06ee) and the [Pygbag Site](https://pypi.org/project/pygbag/)

The following instructions assume use of Pycharm to create a new project called 'memory'
 1. Install Pygbag in the (~/PycharmProjects/memory) environment workspace ```pip install pygbag```
 2. Make the code async aware:
    1. Import 'asyncio' into main.py file ```import asyncio```
    2. Wrap the game loop with async commands ```async def main():```, ```await asyncio.sleep(0)```, ```asyncio.run(main())```
 3. Navigate to directory ```~/PycharmProjects``` that contains the game directory (```memory```) where the main.py file is located.
 4. Enter command ```pygbag memory```, Pygbag converts the files and starts up a server.
 5. The site can be viewed by pointing your browser to ```localhost:8000```.
    1. Game can also still be played on computer using ```python ~/PycharmProjects/memory/main.py```
 6. Deploy to Github pages:
    1. Create a separate branch with the required file structure:
       1. Create a ``docs`` folder under the root of the branch.
       2. Copy the three files from the ```build/web``` folder (favicon.png, index.html, memory.apk) to the ```/docs``` folder.
       3. Follow the [Github directions](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-your-site) to deploy to Github pages.
