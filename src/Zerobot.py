"""
Zerobot.py
A simple discord bot
"""
import discord
import configparser

# Custom modules
from src.ReplyModule import Reply
from src.MockModule import Mock

# evil globals
config = configparser.ConfigParser()
client = discord.Client()
modules = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    """
    Starting point for all messages. Checks if the message is a command
    Else passes it to every module to run a generic parse
    """
    # check for prefixes
    if message.content.startswith(config['general']['prefix']):
        await parse_commands(message)
    else:
        for module in modules:
            await module.parse(message)


async def parse_commands(message):
    """
    Commands are messages prefixed with the bot name
    It allows users to make queries, configure modules, get help ect
    """
    m_split = message.content.lower().split()
    # prefix but no commands
    if len(m_split) == 1:
        errmsg = config['errors']['prefix_no_command']
        await reply(message, errmsg)
        return
    # reserved keywords come first
    cmd = m_split[1]
    if cmd == 'modules':
        await parse_module_command(message)
        return
    # reserved keywords done, check module names
    for mod in modules:
        if mod.name.lower() == cmd:
            await mod.command(message)
            return
    # not a keyword and not a module
    errmsg = config['errors']['cmd_not_recognized']
    await reply(message, errmsg)


async def parse_module_command(message):
    """
    Invoked using "{prefix} modules"
    Right now just lists modules, but maybe add plans for expansions
    """
    module_names = "Current module list:\n"
    for mod in modules:
        module_names += "{}\n".format(mod.name)
    await reply(message, module_names)


def load_modules():
    global modules
    reply = Reply("reply", client, config)
    mock = Mock("mock", client, config)
    modules.append(reply)
    modules.append(mock)


def startup():
    global config
    config.read('config.ini')
    load_modules()
    client.run(config['security']['token'])


async def reply(message, reply):
    """
    helper to send messages to the same channel
    """
    await client.send_message(message.channel, reply)


if __name__ == '__main__':
    startup()
