from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import response_selection
from chatterbot import comparisons , logic

chat_bot=ChatBot("IT Dep.", read_only = False, database_uri='sqlite:///databasechatbot.sqlite3',
            logic_adapters = [
                {
                    "import_path" : 'chatterbot.logic.MathematicalEvaluation'
                },
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    "statement_comparison_function" : comparisons.SynsetDistance,
                    "response_selection_method" : response_selection.get_random_response,
                    'maximum_similarity_threshold': 0.8
                    #'default_response': 'I am sorry, but I do not understand.'
                }            ]
                )



#tranning data function

'''
import os
if os.path.exists("db.sqlite3"):
  os.remove("db.sqlite3")
'''

trainer = ChatterBotCorpusTrainer(chat_bot)
trainer.train("./greetings.yml","./ITDept.yml","./bot_profile.yml","./converstions.yml")
