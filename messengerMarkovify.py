import Config
import markovify
import getpass
from fbchat import Client
from fbchat.models import *

thread_id = 0
messageTexts = []

password = getpass.getpass("FB Password: ")

client = Client(Config.email, password)
threads = client.fetchThreadList()

for thread in threads:
    if (thread.name == Config.chatName):
        thread_id = thread.uid
        break

messages = client.fetchThreadMessages(thread_id=thread_id, limit=Config.messageLimit)
messages.reverse()

for message in messages:
    if (message.text != "" and message.text != None):
        messageTexts.append(message.text.encode("utf-8", errors='ignore').decode('utf-8'))

newlineMessages = "\n".join(messageTexts)

markov_model = markovify.NewlineText(newlineMessages,state_size=Config.stateSize)

print("")
print("Group chat: " + Config.chatName)
print("")
print("Markovified messages:")
print("")

for i in range(Config.numMarkovs):
    print(str(i+1) + '. ' + markov_model.make_short_sentence(140, tries=Config.numTries))

print("")
input("Press any key to continue")
