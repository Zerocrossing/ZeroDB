from ZeroModule import Zeromodule as ZM
import re
import json
import string


class SciWhy(ZM):
    """
    SciWhy checks incoming messages for the titles of science fiction novels,
    then links the wikipedia page for those novels or their authors.
    """

    def check_ahead(self, message, index, count, distance, wordNo, search):
        """
        When the first word of a search phrase matches a word in the message,
        this method recursively checks forward to ensure that ensuing search terms occur
        in the same sequence and within a given distance of each other
        """
        if wordNo >= len(search):
            return True
        elif (count > distance) or (index + count >= len(message)):
            return False
        if search[wordNo] == message[index + count]:
            return self.check_ahead(message, index + count + 1, 0, distance, wordNo + 1, search)
        else:
            return self.check_ahead(message, index, count+1, distance, wordNo, search)

    def strip_lower_split(self, phrase):
        """
        This method removes punctuation and capitalization, then splits a phrase into words
        """
        terms = phrase.split(" ")
        translator = str.maketrans('', '', string.punctuation)
        result = phrase.translate(translator)
        return result.lower().split(" ")

    
    def check_message(self, message, search_term):
        """
        This method processes, then checks a message for correspondence with a scifi novel
        """
        message = self.strip_lower_split(message)
        search_term = search_term.lower().split(" ")
        for i, word in enumerate(message):
            if (word == search_term[0]):
                if (self.check_ahead(message, i+1, 0, self.distance, 1, search_term) == True):
                    return True
        return False

    def load_books(self):
        """
        This message loads a list of novels from a .json file
        """
        book_file = open('../data/sf_books.json', 'r')
        book_list = json.load(book_file)
        book_file.close()
        return book_list

    def startup(self):
        self.book_list = self.load_books()
        self.distance = 2 # TODO: Make distance customizable by command

    def shutdown(self):
        pass

    async def parse(self, message):
        """
        Main method for the SciWhy module
        Checks the message contents for book titles and if found, replies with a link to them
        """
        for item in self.book_list:
            if self.check_message(message.content, item["search_words"]):
                await self.reply(message, item["link"])
                break

    async def command(self, message):
        """
        TODO: change distance with command
        """
        pass
