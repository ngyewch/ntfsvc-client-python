import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')
import ntfsvc


def main():
    client = ntfsvc.Client(os.environ['NTFSVC_URL'], os.environ['NTFSVC_APIKEY'])
    client.send_notification(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
