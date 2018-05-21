# Simple one page data visualization app written with Flask + MongoDB + D3.js

## Installation and start

To run this project you'll need installed MongoDB.
You can follow the link below and go through the installation process and get some tips for use.
https://activewizards.com/blog/practical-mongodb-in-10-minutes/

From now on this tutorial assume that you have MongoDB installed and running.

1. Clone this project or download and unzip to your project directory

2. Create virtualenv in your project dir

`virtualenv venv`

and activate it

`source venv/bin/activate`

If you're not familiar with virtualenv, follow this link - http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv

3. Install project required dependencies

`pip install -r requirements.txt`

4. Run Mongo shell and create the database named 'world_bank' using

`mongod`

`>> use world_bank`

5. Create collection named 'world':

`>> db.createCollection('world')`

Close Mongo shell

6. Import collection from world_bank.json:

`mongoimport --db world_bank --collection world --type json --file world_bank.json`

7. Run the project by executing

`python run.py`