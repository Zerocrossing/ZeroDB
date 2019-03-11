from src.ZeroModule import Zeromodule as ZM
import re
import random


class Mock(ZM):
    """
    Uses CUNNING and WIT to BRUTALLY MOCK people you disagree with
    Usage: Only responds to commands (eg. "ZB mock *arg")
        if *arg is an @user then it will iter over the most recent messages to find the last one the @user sent
        if *arg is a name it will look for that instead
    TODO: Currently this messes up emojis in the original message
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
        prefix = self.config['general']['prefix']
        command = self.name
        re_str = r"{} {} (.+)".format(prefix, command)
        match = re.search(re_str, message.content)
        if match:
            msgs = self.client.messages
            target = match.group(1)
            # "That" means we mock the last message before the command
            if target.lower() == "that":
                mock_me = msgs[-2]
                await self.mock_reply(mock_me)
                return
            # if a user is specified it's either a name or an @
            else:
                # if it's an @ lets parse it (@s contain the ID)
                dont_at_me = r"<@(\d+)>"
                match = re.search(dont_at_me, target)
                if match:
                    target = match.group(1)
                for msg in reversed(self.client.messages):
                    auth = msg.author
                    if auth.name.lower() == target.lower() or auth.id == target:
                        await self.mock_reply(msg)
                        return
        # if we got here without returning,
        else:
            await self.reply(message,
                             "Sorry, I don't understand that, or you've asked me to mock someone who hasn't spoken in a long time, or isn't here.")

    async def mock_reply(self, message):
        """
        helper method. Takes a message and sends it back but in AlTeRnAtInG cApS
        """
        pwnd = ""
        chance_thresh = self.config.getfloat(self.name,"emoji_chance")
        max_emoji = self.config.getint(self.name, "max_emoji")
        emoji = [":joy:", ":clap:", ":ok_hand:", ":sweat_drops:", ":eggplant:", ":100:", ":laughing:"]
        for word in message.content.split():
            # skip emoji
            if word.startswith(":"):
                pwnd += word + " "
                continue
            pwnd +=  await self.alt_cap(word) + " "
            add_emoji = random.random() < chance_thresh
            if add_emoji:
                pwnd += " "
                for n in range(random.randint(1, max_emoji)):
                    pwnd += random.choice(emoji)
                pwnd += " "
        await self.reply(message,pwnd)

    async def alt_cap(self, str_in):
        case = False
        pwnd = ""
        for c in str_in:
            if case:
                pwnd += c.upper()
                case = not case
            else:
                pwnd += c.lower()
                case = not case
        return pwnd