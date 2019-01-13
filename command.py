def __init__(self):
    self.commands = {
        "sup": self.sup,
        "help": self.help
    }


def handle_command(self, user, command):
    response = "<@" + user + ">: "

    if command in self.commands:
        response += self.commands[command]()
    else:
        response += "Sorry I don't understand the command: " + command + ". " + self.help()

    return response


def sup(self):
    return "Suhhhhhh"


def help(self):
    response = "Currently I support the following commands:\r\n"

    for command in self.commands:
        response += command + "\r\n"

    return response