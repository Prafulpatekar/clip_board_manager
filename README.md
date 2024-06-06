[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


[![version][version-badge]][RELEASES]

# A clipboard manager in python, built using tkinter and pyperclip


## How to run clipbot

- Clone the repo
- Use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) to create a virtual env with `python>=3.7`
- Run `python3.7 -m venv venv`
- Run `source venv/bin/activate`
- Run `python setup.py install` (it will install all the required dependencies)
- Run `python src/clipbot.py`


## How to make it a standalone Mac OS X application file

I used [`py2app`](https://py2app.readthedocs.io/en/latest/) to make standalone application bundles.

To make the standalone app, just run:

- `python setup.py py2app`

It will create the `.app` folder under the `dist` folder, which you can copy to your `Applications` folder in your Mac, and open `Clipbot` just like any other application!



> Note: If you got error for py2app then run below commands then again run `python setup.py py2app`
- `pip3.7 install -U py2app`
- `pip show py2app`
