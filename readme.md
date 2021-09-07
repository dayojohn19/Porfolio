

To run this 
on your CLI , assuming you have alread installed docker and running, type <strong> `docker-compose up`
    </strong>
    <br><br>
    <p>if you <strong>DONT</strong> have docker, just type <strong>`pip install -r requirements.txt>`</strong></p>
    <h1>About the Project</h1>
    <p>:grinning:  :smile: This capstone is a pigeon racing game, it hosts pigeon fancier/player and integrate all the pigeon, <br>
        Getting the user's: location to calculate their pigeon `distance` and `speed`, it also store every pigeon racing history, picture, and user picture<p>
    <p>It is composed of two application<br>
        <ul>
            <li>'race' application that utilize the racing of the pigeon</li>
            <li>'user' application that utilize each users and their pigeon</li>
        </ul>
        I used javascript under race template to post a request in race.models  and on 'user' interface to have a better view of the app,
    <p> I use @media inside .css file to make it mobile responsive and , i made the video on mobile view to show that it is mobile responsive
    <h1>Distinctivness and Complexity</h1>
    <p>Unlike any other projects that focus on business and networking, My Project focus on game, a racing game, any user from different location can participate in a race in the comfort of their home with this Project</p>
    <h2>Race.models</h2>
        <ul>
            <li><p>Class Point<br>
                the model that store user's location, and map coordinates</li>
            <li><p>Class Race<br>
                model that create the racename and price where the user can participate</li>
            <li><p>Class Lap<br>
                it stores each  on a race where it store map coordinate, loading cost, release time, racename, and a boolean released or not. </li>
            <li><p>Class Code<br>
                where is the unique code that the user need to enter to load their pigeon on each lap</li>
            <li><p>Class Measurement<br>
                this is the model that take the user's coordinate</li>
            <li><p>Class Loaded<br>
                model where the user put the unique code to load their pigeon</li>
            <li><p>Class Entries<br>
                this is the list of all pigeon that entry the races</li>
            <li><p>Class Record<br>
                model which stores each pigeon historical race</li>
        </ul>
    <h2>User.models</h2>
        <ul>
            <li><p>Class User<br>
                This is what creates a unique user</li>
            <li><p>Class Image<br>
                This take the pigeon's image</li>
            <li><p>Class UserImage<br>
                This take the user's image</li>
            <li><p>Class MyPigeon<br>
                This stores all the user's pigeon</li>
        </ul>
    <h2>User.forms</h2>
        <ul>
            <li><p>ImageForm<br>
                    this is the form for the pigeon</li>
                <li><p>UserImageForm<br>
                    form for each user's profime image</li>
        </ul>                    
    <h1>To run this application</h1>
        <ul>
            <h2>Clone this project</h2>
            <h3>There are several ways to run this application</h3>
            <li>On your terminal type `pip install -r requirements.txt` </li>
            <li>If you have docker install, on your terminal `docker-compose up` </li>
        </ul>
    <h1>Instructions</h1>
    <ol>
        <h2>How to Use the app</h2>
        <li>Register Account</li>
        <li>Register Pigeon</li>``you can check pigeons if you clicked on player name``
        <li>Join Race</li>
        <li>Scroll to `Open Race`</li>``before you click open race submit your loft complete address below``
        <li>Join !! Race</li>
        <li>Entry Your Pigeon</li>
        <li>Load Pigeon</li>`` you can see the next lap release, go to pigeon loading station and ask for a load code sticker``
        <br>`` load your pigeon to the truch and wait for the release until your pigeon return ``<br>
        <br>`` your pigeon return with a sticker tag on its ring, get the load code  and clock it``
        <li>Clock !</li> `` you will see your pigeon speed `` <br>
    </ol>
    <br><br>
        <ul>
            <h2>Checking Pigeon Record</h2>
            <li>`view Players`</li>
            <li>`player_name`</li>  view all their pigeons 
            <li>`pigeon_name`</li> to view players' pigeon records 
        </ul>
    
