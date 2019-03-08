# ZeroDB
#### A simple discord bot designed with flexibility and modularity in mind.

I have written this bot primarily for my own personal use, as well as encouraging friends
and new programmers to create modules for it. As such the goal is to make writing additional modules
relatively simple for someone with a small amount of python experience.

## Dependencies:
[Discord.py](https://github.com/Rapptz/discord.py)

## To Run
To run on your own device, first you will need to create a discord app / bot. 
There are tutorials online on how to do this. After setting up your bot, you need to create a file called
token.ini in the src directory of the project. This file needs to contain only your discord token in plain text.
After creating the file, assuming all dependencies have been installed you can run 
ZeroDB.py and the bot will run.


## Architecture:
ZeroDB is designed to be modular, so people can contribute modules without having to concern themselves with much more than text parsing.
This likely means that there are many redundancies with discord.py, as it contains it's own bot and cog modules, but as this is a personal project for fun and experience I don't mind.
***

### Writing your own module
ZeroModule.py is the abstract class for ZeroDB modules, and is fairly well commented.
Each module consists of 4 'abstract' methods. These methods can be overwritten in your own custom 
module.
The methods are:
* startup: called once upon boot
* shutdown: called before a proper shutdown
* parse: the parse method receives every discord message object in the server, regardless of 
commands or context.
* command: any text prefixed with the prefix of the bot as well as the name of a module is 
considered a command. Commands are parsed by the main module and are only sent to the module.
This is useful for sending modules specific configuration methods, or for writing any kind of 
utility that doesn't need to listen to arbitrary messages.

As an example, ReplyModule and MockModule exist currently: They are simple examples of using
the parse and command methods for some useful (if silly) functionality.


