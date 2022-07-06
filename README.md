# Stardew Valley Wiki Discord Bot

## Description
This is a Discord bot that allows users to easily get commonly searched information from the Stardew Valley Wiki. While playing Stardew Valley, users often have to pull up the Wiki to get information such as a NPC's birthday or where to catch a certain type of fish. This disrupts the gameplay, so my goal for this project was to make it as easy as possible to get that information

I broke this application down into 2 services: the API that scrapes the information off of the Wiki and the actual Discord bot itself. I decided to split it into those two services in order to seperate concerns and to make it easy to reuse my API if I decide to come up with another avenue of providing this information. I chose Flask over Django for my web framework because I loved how lightweight it is for a small project like this. I noticed that my API responses were fairly slow (since I have to make a request for the right wiki page and then scrape it), so I decided to implement API level caching using Redis, reducing response times from 600ms to 10ms on average. I decided against just storing all of the wiki information in a database/file for 2 reasons: 1. there really isn't that much data so it didn't really make sense to implement a full persistence system, and 2. the game is still receiving updates, so I want to ensure users are always getting the most up to date information

## Usage
1. Ensure that you have Docker and Docker Compose installed on your machine
2. Run ```docker-compose up -d --build```

## Future Expansion

I would love to deploy this bot at some point, probably using Heroku, so that other people can use it as well. There's also probably more routes that I could add to the API that I haven't thought of yet, but I'll have to continue play testing the bot in order to figure out what would be most helpful.