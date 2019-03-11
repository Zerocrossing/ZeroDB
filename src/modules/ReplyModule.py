from src.ZeroModule import Zeromodule as ZM
import re


class Reply(ZM):
    """
    ReplyModule simply replies to single words with words or phrases
    Replies can be given by users through commands
    eg) "ZB reply ayy LMAO" will cause the bot to reply to "ayy" with "LMAO" (assuming ZB is the bot prefix)
    TODO: add persistence
    """

    def startup(self):
        self.keywords = {}

    def shutdown(self):
        pass

    async def parse(self, message):
        """
        Main method for the reply module
        Checks the message contents for keywords and if found, replies to them
        """
        for word in message.content.lower().split():
            if word in self.keywords:
                await self.reply(message, self.keywords[word])

    async def command(self, message):
        """
        Command for this module allows users to create custom replies.
        Note that you can only reply to single words, not phrases (currently)
        """
        prefix = self.config['general']['prefix']
        command = self.name
        re_str = r"{} {} (\w+) (.+)".format(prefix, command)
        match = re.search(re_str, message.content)
        if match:
            reply_to = match.group(1)
            reply_with = match.group(2)
            self.keywords[reply_to] = reply_with
            print("ReplyModule: adding '{}' : '{}'".format(reply_to, reply_with))
            await self.reply(message, "I will reply to '{}' with '{}'".format(reply_to, reply_with))
        else:
            await self.reply(message, "I'm sorry, you have used incorrect formatting for the reply command.")
