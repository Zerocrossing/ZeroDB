import discord
import configparser


class Zeromodule:
    """
    Abstract class for modules for the discord bot
    """

    def __init__(self, name, client, config):
        """
        :type config: configparser.ConfigParser
        :type client: discord.Client
        """
        self.name = name
        self.client = client
        self.config = config
        print("Loading module: {}".format(name))
        self.startup()

    # region OVERRIDES

    def startup(self):
        """
        Called by the constructor. A place for each module to do it's own initialization
        :return: None
        """
        pass

    def shutdown(self):
        """
        Called for every module on shutdown, a place to store data, ect.
        :return:
        """
        pass

    async def parse(self, message):
        """
        Parse is the main method for each module.
        :param message: a discord.py message object
        :return:
        """
        pass

    async def command(self, message):
        """
        Command is invoked by calling "$prefix$ $module_name$" followed by args.
        :param message: discord.py message (already assumed to begin with the above format)
        :return: none
        """
        pass

    # endregion

    async def get_cfg(self, value):
        return self.config[self.name][value]

    async def reply(self, message, reply):
        """
        convenience method to send a message on the same channel as the recieved message
        """
        await self.client.send_message(message.channel, reply)
