import socket

# A class to scan ports using simple Python
class PortScanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

        # Scan a range of ports

    def scan_ports(self, starting_port, ending_port):
        for port in range(starting_port, ending_port + 1):
            print(f'scanning {port} ....')
            # if port is open update the list
            if self.is_open(port):
                self.open_ports.append(port)

        # this function checks for open port using socket library
    def is_open(self, port):
        s = socket.socket()
        exit_code = s.connect_ex((self.ip, port))
        s.close()
        if exit_code == 0:
            return True
        else:
            return False

        # write open ports to a file of your choosing
        def write_to_file(self, path_to_file):
            with open(path_to_file, "w") as f:
                for port in self.open_ports:
                    print(port)
                    f.write(str(port) + "\n")


def main():
    # My metasploitable is running @ 192.168.1.106
    ip = input("Enter the IP to scan: ")
    starting_port = int(input("Enter the lower end of port to scan: "))
    ending_port = int(input("Enter the upper end of port to scan: "))
    scanner = PortScanner(ip)
    scanner.scan_ports(starting_port, ending_port)
    # print(scanner.open_ports)
    scanner.write_to_file("open_ports.txt")


if __name__ == '__main__':
    main()