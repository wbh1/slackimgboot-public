# Slack Imagebot
This is a Slack Imagebot written in Python for deployment on a Django webserver running on Heroku. It utilizes Imgur's API for standard searches and falls back to a search with Bing's Cognitive Services Search API if no Imgur result is found.

## Requirements
+ An API key from [Imgur](http://api.imgur.com/)
+ An API key from Microsoft
+ Heroku account (optimal)
+ Django webserver running on Heroku (optimal)

## Heroku Setup
My recommended way of setting up this project would be to create your own Django webserver on Heroku and only add the files of mine that you need.

You can get a great Django starter template from [here](https://github.com/heroku/heroku-django-template).

Once you have that up and running, you should insert/overwrite the following the folders/files:
+ requirements.txt (all of the dependencies Heroku needs to install)
+ runtime.txt (which version of Python this runs on)
+ the entire **img2** folder
+ copy/overwrite all of the contents of the **slack_imageboot** folder to your corresponding "project_name" folder
   + **BEFORE DOING THIS, OPEN YOUR _settings.py_ FILE AND SAVE THE "SECRET_KEY".**
   + Paste YOUR "SECRET_KEY" into the corresponding field in the _settings.py_ that I provided

With all of the files in place, you can insert your API keys into the creds file.

You can deploy your app to Heroku now.

## Slack Setup
Create a new Custom Integration for your Slack team.

This works as a slash command. I use "/img" to trigger mine.

The link will be `YOURAPPNAME.herokuapp.com/img2/`

Customize the name of the integration and the icon to your pleasing.

Save it and test it out.

## Acknolwedgements
The following projects were invaluable in helping me get this working:
+ [Heroku Django Template](https://github.com/heroku/heroku-django-template)
+ [Tristan Tao's py-bing-search](https://github.com/tristantao/py-bing-search)
+ [Imgur's Python library](https://github.com/Imgur/imgurpython)
