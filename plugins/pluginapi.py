import irc.bot
import irc.strings


class BasicPlugin(object):
    def __init__(self, name, desc, config, connection):
        self.name = name
        self.description = desc
        self.commands = []
        self.config = config
        self.channel = self.config["connection"]["channel"]
        self.connection = connection

    def on_message(self, msg, user):
        pass

    def on_command(self, cmd, user):
        for command in self.commands:
            if command.name == cmd.split(" ")[0]:
                command.action(user, cmd.split(" "))

    def send_msg(self, msg, chan):
        c = self.connection
        c.privmsg(chan, msg)

    def send_notice(self, msg, user):
        c = self.connection
        c.notice(user, msg)

    def on_userjoin(self, usr):
        pass

    def on_userquit(self, usr):
        pass

    def register_command(self, name, action):
        cmd = Command(name, action)
        self.commands.append(cmd)


class Command(object):
    def __init__(self, name, action):
        self.name = name
        self.action = action