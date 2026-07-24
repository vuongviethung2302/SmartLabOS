import os


class CommandExecutor:

    def execute(self, command):

        print("=" * 50)
        print("Received Command :", command)
        print("=" * 50)

        try:

            if command == "test":

                print(">>> TEST COMMAND EXECUTED")
                return True

            elif command == "shutdown":

                print(">>> SHUTDOWN EXECUTING...")

                os.system("shutdown /s /t 0")

                return True

            else:

                print(f">>> UNKNOWN COMMAND: {command}")
                return False

        except Exception as e:

            print(">>> EXECUTE ERROR:", e)
            return False