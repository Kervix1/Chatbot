from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os



app = Flask(__name__)
#app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
#socketio = SocketIO( app )

#bot = ChatBot('Chatterbot')
#conv = open('chats.txt', 'r').readlines()
#for _file in os.listdir('ChatTopics'):
	#chats = open('ChatTopics/' + _file, 'r').readlines()

#trainer = ListTrainer(bot)

#trainer.train(chats)

bot = ChatBot("Candice", logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
    {  'import_path': 'chatterbot.logic.TimeLogicAdapter'
       },
    {  'import_path': 'chatterbot.logic.MathematicalEvaluation'
       },
    {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        }
    ])
for _file in os.listdir('ChatTopics'):
    chats = open('ChatTopics/' + _file, 'r').readlines()

conv = open('ChatTopics/heyChatbot!.txt', 'r').readlines()
conv2 = open('ChatTopics/MovieConv.txt', 'r').readlines()
trainer2 = ListTrainer(bot)

trainer2.train(chats)
trainer2.train(conv)
trainer2.train(conv2)

trainer = ChatterBotCorpusTrainer(bot)


trainer.train("chatterbot.corpus.english")
trainer.export_for_training('./my_export.json')


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run()
 
