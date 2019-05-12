# RandomicRabbit

A python web server for generating random numbers at random intervals and sending them to
connected users in real time.

The repository consists of a python web service using flask & flask-socket.io python libraries.
The web service supports asynchronous flask communication with a front end web page, which is
updated using a background thread for all users connected.
It is based on the useful Flask-SocketIo code from Miguel Grinberg & the example from Shane Lynn.

```
https://github.com/miguelgrinberg/Flask-SocketIO
https://github.com/shanealynn/async_flask
```

To run - please clone the repository and then set up your virtual environment using the requirements.txt file with pip and virtualenv. Following are the steps:

```
git clone https://github.com/Messier87/RandomicRabbit.git
cd RandomicRabbit
virtualenv randomicrabbit
./randomicrabbit/Scripts/activate
pip install -r requirements.txt  #(or in Windows - sometimes python -m pip install -r requirements.txt )
```

Start the web service with:
```
python app.py
```
and visit [(http://localhost:5000)] to see the updating numbers and the graph.