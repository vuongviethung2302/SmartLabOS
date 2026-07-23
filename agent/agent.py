import time

from heartbeat import send_heartbeat
from config import HEARTBEAT_INTERVAL


def main():

    print("SmartLab Agent Started")

    while True:

        try:
            response = send_heartbeat()
            print(response)

        except Exception as e:
            print("Heartbeat Error:", e)

        time.sleep(HEARTBEAT_INTERVAL)


if __name__ == "__main__":
    main()