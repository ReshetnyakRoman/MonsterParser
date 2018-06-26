Job Description parser for https://www.monster.com/ (release 26.06.2018)

This parser creates file 'position.txt' with position title description for given search criteria
You can put your own search parameters in 'config.py'
There are 3 only params with comments-descriptors for each one directly in file

default: Python Developer in  NewYork City, for last 3 days.

Installation:

You need to clone repository, 
	git clone https://github.com/ReshetnyakRoman/MonsterParser

install packages from requirements file with 
	pip install beautifulsoup4 html5lib parse requests

and run main.py in Python3 interpreter

in the project directory you'll find resulting file: 'positions.txt'

Enjoy!