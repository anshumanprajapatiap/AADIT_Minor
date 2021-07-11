from .KEYwords import reply
from chatterbot import ChatBot

IT_Bot=ChatBot("IT_Bot", read_only = True, database_uri='sqlite:///databasechatbot.sqlite3')

# press ctrl+c to exit conversation

#continous loop
'''
while True:
    try:
        inp = input().strip()
        if inp == '':
            print("Enter a valid input")
            continue
        bot_output = IT_Bot.get_response(inp)
        bot_output=str(bot_output)
        print(reply(bot_output,inp))

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
'''
#single statement

def get_keyword(statement_input):
    IT_Bot=ChatBot("IT_Bot", read_only = True, database_uri='sqlite:///databasechatbot.sqlite3')
    try:
        inp = statement_input.strip()

        
        if inp == '':
            return "Enter a valid input"
                  

        bot_output = IT_Bot.get_response(inp)
        bot_output=str(bot_output)
        return reply(bot_output,inp)

    except(KeyboardInterrupt, EOFError, SystemExit):
        return "exception"
