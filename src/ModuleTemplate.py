"""
Empty Template for ZDB Modules
"""
from src.ZeroModule import Zeromodule as ZM


class MY_CLASS(ZM):
    """
    Module Description Goes Here
    """

    def startup(self):
        pass

    def shutdown(self):
        pass

    async def parse(self, message):
        """
        Parse is the main method for each module.
        :param message: a discord.py message object
        :return: none
        """
        pass

    async def command(self, message):
        """
        Command is invoked by calling "$prefix$ $module_name$" followed by args.
        :param message: discord.py message (already assumed to begin with the above format)
        :return: none
        """
        pass
