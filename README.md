Embedded Final Project
=============

This code is for the final project of the Embedded Systems course taught by [Dr. Mohsen Ansari](https://scholar.google.com/citations?user=Dhfls4sAAAAJ&hl=en) in fall semester of 2022.

Collaborators:
- [Mohammad Abolnejadian](https://github.com/theablemo)
- [Kian Omoomi](https://github.com/kianomoomi)
- [Mohammadali Khodabandelou]()

# Introduction

This project is meant to be run on a Raspberry Pi and develop students' skills in working with Raspberry Pi, its GPIO, and different hardware modules such as 7segment LED, active buzzer, RFID, etc. 

In this project, we made a Flappy Bird game, which can be run on a Raspberry Pi and the bird can jump by hearing the clap of a hand! The game was initially forked from [here](https://github.com/sourabhv/FlapPyBird), but we changed it drastically as we needed more features such as authentication and interacting with hardware modules. 

# Setup

In order to use this code, you need the following:
- Raspberry Pi (1x)
- 7-Segment LED (1x)
- Active Buzzer (1x)
- LED (1x)
- RFID (card and reader) (1x)
- Sound module (1x)

After setting up your hardware, you can play the game by running `RBPFlappy.py`

# Modules

- **7-Segments LED**: Used to show the score
- **Active Buzzer**: Used to make a sound every time the bird passes a barrier
- **LED**: Used to show when the user loses the game
- **RFID**: Used to authenticate users and login to the game
- **Sound Sensor**: Used to detect the clapping sound

By leveraging Raspberry Pi's GPIO, we orchestrated all of these modules with Raspberry Pi. The code to handle these modules can be found in the [modules directory](</modules/>)
