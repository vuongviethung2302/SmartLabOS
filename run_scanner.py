from services.scanner.network_scanner import NetworkScanner


def main():

    scanner = NetworkScanner()

    hosts = scanner.scan_subnet_thread("10.170.44.0/24")

    for host in hosts:
        print(host)


if __name__ == "__main__":
    main()