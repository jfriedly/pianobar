#!/usr/bin/python
import time
import sys
import subprocess
import logging
import re


LOGLEVEL = logging.DEBUG


def process_input(regex):
    while True:
        # Need to strip off '\x1b[2K' -- the 4-byte string that clears the
        # current terminal line
        instring = raw_input()
        instring = regex.sub('', instring)
        logging.debug('instring = ')
        logging.debug(repr(instring))
        if instring.startswith('Welcome to pianobar'):
            logging.debug('welcome statement')
            logging.info(instring)
        elif instring.startswith('(i)'):
            logging.debug('started with (i)')
            logging.info(instring)
        elif instring.startswith('|>  Station'):
            logging.debug('started with |>  Station')
            logging.info(instring)
        elif instring.startswith('#'):
            logging.debug('started with #')
            logging.info(instring)
        else:
            logging.debug('else')
            logging.info(instring)
            time.sleep(5)
            break


def main():
    pianobar = subprocess.Popen('pianobar', stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
    sys.stdin = pianobar.stdout
    sys.stdout = pianobar.stdin
    logging.basicConfig(format=None, level=LOGLEVEL)
    # Have to concatenate two strings here because one is unicode and the other
    # contains a regex special character
    regex = re.compile('\x1b' + r'\[2K')

    while True:
        process_input(regex)
        cmd = 'n'
        print cmd
        logging.info(cmd)


if __name__ == "__main__":
    main()
