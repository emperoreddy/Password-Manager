# Password Manager

**Password manager** is an app used to store different app's passwords with different users.

[![asciicast](https://asciinema.org/a/aZjCOwUUdgHxYNIza0TWcR234.svg)](https://asciinema.org/a/aZjCOwUUdgHxYNIza0TWcR234)

------------


### Usage

* To use the app, you need at least python 3 and pip, you can download and install [_**python**_](https://www.python.org/downloads/ "*python*") from the source website  and [_**pip for windows**_](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/ "*pip for windows*") / [_**pip for linux**_](https://linuxconfig.org/install-pip-on-linux "*pip for linux*").

* After installing python and pip, install sqlite3 with pip and then clone this repository
```
pip install pysqlite3 
git clone https://github.com/emperoreddy/Password-Manager
```
* Navigate into the created directory and run the python script
```
cd .\Password-Manager\
py userGui.py
```
> If the first method doesn't work, try the other ones below (one at a time)
```
python3 userGui.py
python3 -m userGui.py
```

From here you can create a new user, login into a new user and then store/delete/get passwords

------------


### Technologies used
This was made with:
1. Python for the main code
2. SQLite database for storing passwords locally

------------


### Todo in the future
- [ ] Store passwords into an online database
- [ ] More user-friendly (using GUI)
- [ ] Change user's passwords
- [ ] Delete one / all users



