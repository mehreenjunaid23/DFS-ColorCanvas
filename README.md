# Coloring Algorithm

## Purpose
<!--Purpose of the project-->
This poject aims to build a GUI interface to draw and color using Depth First Search (DFS) algorithm. 

### Draw and Color
![alt text](https://github.com/AichaSidiya/coloringAlgorithm/blob/main/p1gif.gif)
### Color
![alt text](https://github.com/AichaSidiya/coloringAlgorithm/blob/main/p2gif.gif)
<!--Header 2 description of the project-->
## Description

The project is a python application program. The program start by displaying a question box asking theuser if they wish to draw a picture and color it or if they only want to color. Then if they want to draw an alert message will be displayed stating that if they finish drawing that they should close the original window to color. To color the user has to click on any part of the drawing and a flood fill will color the drawing till the black borders with random generated color, they can chnage the color by recoloring. If they choose to color only they will have to upload a png image to color from their device. 

## Features
* Draw and color 
* Color
* 
<!-- Files of the project-->
## Functions
- Flood fill using DFS
- Drawing
- Main: composed of an if else for drawing and color when drawing is chose the draw function is called when the drawing window is closed the call returns to main where the image that was drew is saved and reaploded auomatically into the gui to be colored. 
## Installation
<!--Steps of Installation-->
* Clone the repository to your local machine:
```
git clone https://github.com/AichaSidiya/coloringAlgorithm.git
```
* Download the python version 3.8.6. 
* Install pygame version  2.1.2 
* Install tikinter version 8.6 

### How to run the program

* Launch the program from any python interpreter and start colorin !!
* 
## Built With

- [Python](https://www.python.org/) - Programming language
- [Pygame](https://www.pygame.org/docs/) - Framework for creating graphical user interfaces
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Framework for creating graphical user interfaces

## Authors
<!-- The contributors to the project-->
* [Aicha Sidiya](https://github.com/AichaSidiya)
* [Hanin Alzaher](https://github.com/hanin-az)
* [Razan Almahdi](https://github.com/RazanAlmahdi)
* [Mehreen Junaid](https://github.com/mehreenjunaid23)


## Acknowledgments
<!-- Insparation files, codes, and general refrences used in writing the code of the project-->
* [Readme Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Flood Fill](https://stackoverflow.com/questions/41656764/how-to-implement-flood-fill-in-a-pygame-surface)
* [Mouse Events](https://www.tutorialspoint.com/pygame/pygame_mouse_events.htm)
* [Message Box](https://stackoverflow.com/questions/41639671/pop-up-message-box-in-pygame)
