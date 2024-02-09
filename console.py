#!/usr/bin/python3

import cmd
from datetime import datetime

class HBNBCONSOLE(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True
    def do_help(self, line):
        return True
    def do_quit(self, line):
        return True

if __name__ == '__main__':
    HBNBCONSOLE().cmdloop()