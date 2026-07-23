import os


class CommandExecutor:

    def execute(self, command):

        print("=" * 50)
        print("Received Command :", command)
        print("=" * 50)

        if command == "test":

            print(">>> TEST COMMAND EXECUTED")

            return True

        print(">>> UNKNOWN COMMAND")

        return False