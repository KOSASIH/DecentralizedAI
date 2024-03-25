import os

class Channel:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)

class Chat:
    def __init__(self):
        self.channels = {}

    def create_channel(self, name):
        if name not in self.channels:
            self.channels[name] = Channel(name)

    def send_message(self, channel_name, message):
        if channel_name in self.channels:
            self.channels[channel_name].send_message(message)

if __name__ == "__main__":
    chat = Chat()

    # create channels
    chat.create_channel("general")
    chat.create_channel("announcements")

    # send messages
    chat.send_message("general", "Hello, world!")
    chat.send_message("announcements", "New version v1.2.0 is out! Download it now.")

    # save to file
    with open("community/chat.json", "w") as f:
        f.write(os.linesep.join([
            "{}: {}".format(channel.name, [message for message in channel.messages])
            for channel_name, channel in chat.channels.items()
        ]))
