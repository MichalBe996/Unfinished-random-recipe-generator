# Unfinished-random-recipe-generator

The code in this repository was an idea to make an app, in which you add ingredients that you have at the moment in your fridge or your pantry,
submit those ingredients, and get random recipe from the internet that you can make using only said ingredients. Whole project was intentend to be 
an exercise on webscraping using BeautifulSoup module in Python. The project is left unfinished for now, because I had a problem with too many requests 
sent to the website while searching for recipes.

As a so called "beta" GUI I decided to use tkinter just for now, but probably gonna change it to something prettier and not as sterile.
The base of the project is obviously BeautifulSoup, requests, and tkinter modules, and random module as an addition.


I decided to use for loop to iterate over all recipes on chosen website (which was food52.com in my case), and add links which may meet expectations and ingredients to the 
empty list. Then, program should randomly choose one link from the list of links to the recipes. Finally GUI should show the picture of recipe, needed proportions of ingredients
and ofcourse recipe itself.
