import re

class Parser():
    '''A class containing regex tags that we're interested in to facilitate parsing of files.'''
    # Regex for parsing notes file
    tags = { 
        'scanned' :'<!-- scanned for trello -->\n',
        'open_task' : '@TASK|@TODO',
        'close_task' : '@END|\n',
        'due_date' : '@due',
        'white_space': '\s'
    }

    def __init__(self, custom_tags=None):
        # add any custom tags provided by user
        if custom_tags:
            pipe = '|'
            for key in self.tags:
                if key in custom_tags:
                    self.tags[key] = pipe.join(self.tags[key], custom_tags[key])

        # for k, v in self.tags.items():
        #     self.tags[k] = re.compile(v)

    def parse_file(self, path):
        '''Extracts tasks from file at @param path.'''
        # List of cards that have been identified in the file
        cards = []
        if path.endswith('.md'):
            with open(path, 'r') as f:
                if not re.search(self.tags['scanned'], f.readline()):
                    # this file hasn't been scanned before
                    contents = f.read()
                    while contents:
                        # Find another card
                        match = re.search(tags['open_task'], contents)
                        if match:
                        # we've found a new card       
                            card = {} # dict to hold extracted card information

                            start_card = match.span()[1]
                            contents = contents[start_card:]
                            match_end = re.search(tags['close_task'], contents)
                            if match_end:
                                end_card = match_end.span()[0]
                            else:
                                raise Exception("Expect close task tag but file ended.")
                            
                            card_text = contents[:end_card]
                            due_date_match = re.search(tags['due_date'], card_text)
                            if due_date_match:
                                # this card contains a due date, let's add it to our card dict
                                due_date = card_text[due_date_match.span()[1]:]
                                end_due_date = re.search(tags['white_space'], due_date)
                                due_date = due_date[:end_due_date.span()[0]]
                                if re.seach('\\d{4}-\\d{2}-\\d{2}', due_date):
                                    card['due'] = due_date
                                else:
                                    # due date does not meet ISO 8601 formatting
                                    print("Skipping due date [{}] in file '{}' as does not follow ISO8601 formatting".format(due_date, path))
                            



                    # prepend the 'scanned' tag to the file 
                    f.seek(0, 0)
                    f.write(tags['scanned'] + f.read())
