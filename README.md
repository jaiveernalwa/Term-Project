# Big Idea / Goal

The Goal of the project was to create a trivia game that leverages OpenAI API to generate questions for the user. There were many constituents to this that we wanted to include. To start with, we wanted the score to be determined by how many questions the user gets right and for the user to have 3 lives, after which their game would end and the score would be recorded. The score would record itself in our leaderboard file. We also wanted the questions to come from 1 of 7 categories, randomly chosen, and we wanted questions to get harder in increments of 5. Ultimately, the purpose of the project was to create an AI based trivia game that challenged users in different creative ways without becoming stale or repetitive.

# User Instructions

In order to play the game succesfully, a new user must run the trivia.py file, and follow the terminal instructions. Users must enter their name when prompted, and then answer questions when they are asked. Alternatively, a frontend website was attempted for the project, but will only take the input of a users name, whereas the rest of the game will need to be played on the terminal.

# Implementation Instructions

There were many implementation techniques used to get the trivia game running. The first is the use of individual functions to carry out each goal. Functions were used to initialize openAI, randomize categories, generate prompts for openAI to use, check answers with openAI, and host the leaderboard. In addition, when making API requests and generating prompts for openAI to use, we had to be very clear in our verbiage in order to get results that we wanted. For example asking questions without any unecesary jargon, or providing responses in a purely yes or no format so our code could interpret as a boolean. 

# Results

The results of our project was a succesfully running trivia game. We were able to create it so that it can effective use the API to generate unique questions and check them, as well as store the scores in a leaderboard. One result we struggled to accomplish was an adequate frontend website. We attemped to make it with flask, but quickly found that we would need to use some sort of tool in order to account for the dynamic element of the questions that openAI would generate. We attempted to solve this using AJAX, Javascript, and Jinja2, but were ultimately unable to find a solution for this. Instead, when the website is run, it just allows for the first page where a user would enter their name, but would continue the game in a python terminal.

# Project Evolution / Narrative

Our project evolved throughout our development, as we wanted to construct applications not based on our capabilities but on our immaginative use cases. That is to say - we wanted to code not what we knew was possible but what we wanted our trivia game to feel like to a user. This required out of the box thinking and research on how to do things that we weren't familiar with. While this allowed us to overcome some hurdles and learn a lot, it also left a lot to be learned, such as the dynamic element of working with a frontend, which was something we imagined and didn't know how to properly do, but attempted to learn with different tools. Ultimately, the project shifted our paradigm in regards to coding, making it a tool for our imagination as opposed to a tool with set rules.