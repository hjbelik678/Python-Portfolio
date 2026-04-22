#Authors Fox W and Henry B.

import shutil
import time
import random

# Constants
SYMBOLS = ["0", "1", "2", "3", "4"]
NEW_STREAM_PROBABILITY = 0.5
BASE_STREAM_LENGTH = 10
MAX_STREAM_LENGTH_DELTA = 5
SLEEP_TIME = 3


def main():

    # Get the width of the terminal window
    width = shutil.get_terminal_size()[0]

    # Initialize the stream lengths
    stream_lengths = [0] * width
    while True:
        for f in range(width):
            if stream_lengths[f] > 0:
                # Writes a random number and decrease the length
                print(random.choice(SYMBOLS), end='')
                stream_lengths[f] -= 1
            else:
                # Print a space and possibly start a new stream
                print(' ', end='')
                if random.random() < NEW_STREAM_PROBABILITY:
                    stream_lengths[f] = random.randint(max(BASE_STREAM_LENGTH - MAX_STREAM_LENGTH_DELTA, 1),
                                                       BASE_STREAM_LENGTH + MAX_STREAM_LENGTH_DELTA)
        print()  # Move to the next line
        time.sleep(SLEEP_TIME)  # Pause before the next frame


if __name__ == "__main__":
    main()
