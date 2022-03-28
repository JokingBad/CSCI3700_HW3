Homework 3: Created by Cris Zbavitel

## Quick Start
### Local Test Setup

decompress the templates file - this holds the index.html, unique.html, and update.html

First, install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

When the server starts, go to your browser and enter "127.0.0.1:5000/api/update_fruit_a" or "127.0.0.1:5000/api/unique"
