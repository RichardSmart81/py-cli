import subprocess


class Script:
    def __init__(self, file_backup=True, log_file=None):
        self.commands = list()
        self.file_backup = file_backup
        self.log_file = log_file

    def run_commands(self):
        for command in self.commands:
            args_list = [command] + command.args
            output = subprocess.call(args_list, timeout=command.timeout)


class Command:
    def __init__(self, command=None, args=list(), timeout=None):
        self.command = command
        self.args = args
        self.timeout = timeout
