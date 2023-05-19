# coloringAlgorithm
<!--Title-->
# MovieDatabase

## Purpose
<!--Purpose of the project-->
This poject is a Movie database. The purpose of this project is to build a java application to display a list of movies and providing more information on the movies.

![alt text](https://github.com/AichaSidiya/MovieDatabase/blob/main/demoMovie.gif)

<!--Header 2 description of the project-->
## Description

The project is a java application program divided into multiple class. The program start by displaying a login page in case that the user does not have an account he/she can signup and a new account obejct will be created and the user data will be saved in the database. Afterwards a home page will display all the movies when a user clicks on one of them he/she will get more info about the movie. Other freatures exists in the classs but are not implemented in the GUI, as follows:
* Admin can add and delete movies and users. 
* Reviewing the movie/display the characters/directors etc. of a particular movie or display the movies of a prticular director etc (using **action** class)

## Features
* View a list of movies
* Create/Delete account
* Add a new movie
* Rate an existing movie
* Database integration using XAMPP

<!-- Files of the project-->
## Classes
- Abstract class: Person
- Account
  + Admin
  + User
- MovieEcosystem
  + Actor
  + Director
  + Writer
  + Producer
- Action
  + Reviews
  + Acts
  + Writes
  + Produces
- Movie: driver class
### UML 


![UML drawio](https://user-images.githubusercontent.com/91727165/180050404-f86eb84e-53b9-4647-8b3d-17d4c27a158a.png)

<!--Header 3 installation and launching the project-->
## Installation
<!--Steps of Installation-->
* Clone the repository to your local machine:
```
git clone https://github.com/AichaSidiya/MovieDatabase.git
```
* Download the java version 17.0.1. 
* Download [xampp](https://www.apachefriends.org/download.html)
* Import moviedatabse.sql to [phpmyadmin](localhost/phpmyadmin/)
* Make sure to update the connection to your database.
* Open the project in your preferred Java IDE.

### How to run the program

* Look for signIn.java and run it and you can then run your program.

## Built With

- [Java](https://www.java.com/) - Programming language
- [Swing](https://docs.oracle.com/en/java/javase/14/docs/api/javax/swing/package-summary.html) - Framework for creating graphical user interfaces
- [XAMPP](https://www.apachefriends.org/index.html) - A software stack that includes Apache, MariaDB, and PHP

## Authors
<!-- The contributors to the project-->
* [Aicha Sidiya](https://github.com/AichaSidiya)
* [Hanin Alzaher](https://github.com/hanin-az)
* [Reem Alsharbi](https://github.com/ReemAlsharabi)
* Alanoud Alhutami


## Acknowledgments
<!-- Insparation files, codes, and general refrences used in writing the code of the project-->
* [Readme Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [IMBD example](https://uwe.pst.ifi.lmu.de/exampleIMDB.html)
* [Java GUI](https://youtu.be/clKDMtfNNuo)
* [PHP and Java](https://youtu.be/h40mEf7WyMQ)
* [JFrames](https://youtu.be/3dlvseTkRHg)
