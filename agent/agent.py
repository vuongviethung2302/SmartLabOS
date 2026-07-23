import time

from heartbeat import send_heartbeat
from command import get_command
from config import HEARTBEAT_INTERVAL
from executor import CommandExecutor


def main():

    print("===================================")
    print("SmartLab Agent Started")
    print("===================================")

    while True:

        try:

            heartbeat_response = send_heartbeat()
            print("Heartbeat :", heartbeat_response)

            command_response = get_command()
            print("Command   :", command_response)
            if command_response["command"]:
                CommandExecutor().execute(
                    command_response["command"]
                )
        except Exception as e:

            print("Agent Error:", e)

        time.sleep(HEARTBEAT_INTERVAL)


if __name__ == "__main__":
    main()