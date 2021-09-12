
   # About the Project
   :grinning:  :smile: This capstone is a pigeon racing game, it hosts pigeon fancier/player and integrate all the pigeon, <br>
        Getting the user's location to calculate their pigeon `distance` and `speed`, it also store every pigeon racing history, picture, and user picture
   ## It is composed of two application
- 'race' application that utilize the racing of the pigeon
- 'user' application that utilize each users and their pigeon

I used javascript under race template to post a request in race.models  and on 'user' interface to have a better view of the app,
# Distinctivness and Complexity
Unlike any other projects that focus on business and networking, My Project focus on game, a racing game, any user from different location can participate in a race in the comfort of their home with this Project
## [Race models](g_pigeon_race/models.py)
- Class Point
     `the model that store user's location, and map coordinates`
- Class Race 
     `model that create the racename and price where the user can participate`
- Class Lap
     `it stores each  on a race where it store map coordinate, loading cost, release time, racename, and a boolean released or not.`
- Class Code
     `where is the unique code that the user need to enter to load their pigeon on each lap ` 
- Class Measurement
     `this is the model that take the user's coordinate`
- Class Loaded
     `model where the user put the unique code to load their pigeon`
- Class Entries
     `this is the list of all pigeon that entry the races ` 
- Class Record
     `model which stores each pigeon historical race`

## [User models](user/models.py)

- Class User
`     This is what creates a unique user`
- Class Image
`     This take the pigeon's image`
- Class UserImage
     `This take the user's image` 
- Class MyPigeon
     `This stores all the user's pigeon`
## [User form](user/forms.py)
- ImageForm
`this is the form for the pigeon`
- UserImageForm
`form for each user's profime image`

# To run this application
## Clone this project
### There are several ways to run this application
- On your terminal type `pip install -r requirements.txt`
- If you have docker install, on your terminal `docker-compose up`

# Instructions
## How to Use the app
1. Register Account
2. Register Pigeon ``you can check pigeons if you clicked on player name``
3. Join Race
4. Scroll to `Open Race` ``before you click open race submit your loft complete address below``
5. Join !! Race
6. Entry Your Pigeon
7. Load Pigeon`` you can see the next lap release, go to pigeon loading station and ask for a load code sticker``
`` load your pigeon to the truch and wait for the release until your pigeon return ``
`` your pigeon return with a sticker tag on its ring, get the load code  and clock it``
8. Clock !!  `` you will see your pigeon speed `` 
## Checking Pigeon Record
- `view Players` view players
- `player_name `view player pigeons
- `pigeon_name`  to view players pigeon records 
## Hash Function
x = user
y = coin
z = chain
r = request

x+y = z
(r/z)-x = y
(y*z)+x = r





    
