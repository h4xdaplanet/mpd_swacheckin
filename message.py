# -*- coding: utf-8 -*-
"""
Python Slack Message class for use with the pythOnBoarding bot
"""
# TODO: Fix hack with yaml library for handling unicode encoding issues
import pyaml


class Message(object):
    """
    Instanciates a Message object to create and manage
    Slack onboarding messages.
    """
    def __init__(self):
        super(Message, self).__init__()
        self.channel = ""
        self.timestamp = ""
        self.text = ("Welcome to Southwest Check-in "
                     "\nPlease use the following syntax to begin checkin:"
                     "\n*checkin ConfirmationNumber Firstname Lastname*")
        self.emoji_attachment = {}
        self.pin_attachment = {}
        self.share_attachment = {}
        self.attachments = [self.emoji_attachment,
                            self.pin_attachment,
                            self.share_attachment]

    def create_attachments(self):
        """
        Open JSON message attachments file and create attachments for
        onboarding message. Saves a dictionary of formatted attachments on
        the bot object.
        """
        with open('welcome.json') as json_file:
            json_dict = pyaml.safe_load(json_file)
            json_attachments = json_dict["attachments"]
            [self.attachments[i].update(json_attachments[i]) for i
             in range(len(json_attachments))]