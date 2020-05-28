import sys
import fire
import logging


class Cmd(object):
    def start_server(self):
        pass


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info(sys.path)
    fire.Fire(Cmd)


if __name__ == '__main__':
    main()
