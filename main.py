import socket


def running_site(site):
    """This function tries to connect to a given server using a socket. It returns whether it was able to connect to the server or not."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False


if __name__ == "__main__":
    while True:
        site = input("Enter the website to check(without .com):\n")
        if running_site(f"{site}.com"):
            print(f"{site}.com is running")
        else:
            print("There is a problem with the site!")

        if input("Would you like to try again, or enter a new website? Y/N \n") in {'n', 'N'}:
            break


