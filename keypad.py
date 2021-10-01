import sys

from GPIOSimulator_v5 import *
import time

GPIO = GPIOSimulator()


class KeyPad:
    key_coord = {(3, 7): '1', (3, 8): '2', (3, 9): '3',
                 (4, 7): '4', (4, 8): '5', (4, 9): '6',
                 (5, 7): '7', (5, 8): '8', (5, 9): '9',
                 (6, 7): '*', (6, 8): '0', (6, 9): '#'}

    def setup(self):
        """initialize the row pins as outputs and the column pins as inputs."""
        GPIO.setup(PIN_KEYPAD_ROW_0, GPIO.OUT)
        GPIO.setup(PIN_KEYPAD_ROW_1, GPIO.OUT)
        GPIO.setup(PIN_KEYPAD_ROW_2, GPIO.OUT)
        GPIO.setup(PIN_KEYPAD_ROW_3, GPIO.OUT)

        GPIO.setup(PIN_KEYPAD_COL_0, GPIO.IN, state=GPIO.LOW)
        GPIO.setup(PIN_KEYPAD_COL_1, GPIO.IN, state=GPIO.LOW)
        GPIO.setup(PIN_KEYPAD_COL_2, GPIO.IN, state=GPIO.LOW)




    def do_polling(self):
        """Use nested loops (discussed above) to determine the key currently being
        pressed on the keypad."""

        time.sleep(0.3)  # kan endre på antall sekunder
        for row_pin in keypad_row_pins:
            GPIO.output(row_pin, GPIO.HIGH)
            for col_pin in keypad_col_pins:
                high = GPIO.input(col_pin)
                if high == GPIO.HIGH:
                    # Hvis den kommer inn i denne if-en, så betyr det at denne knappen (rad, kolonne) er trykket ned
                    return (row_pin, col_pin)
            GPIO.output(row_pin, GPIO.LOW)
        return None

    def get_next_signal(self):
        """This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected."""
        self.setup()
        while True:
            poll = self.do_polling()
            if poll is not None:
                GPIO.cleanup()
                break

        return self.key_coord.get(poll)


def main():
    """The main function for keypad for testing purposes"""
    keypad = KeyPad()
    keypad.setup()

    signal = keypad.get_next_signal()

    print(f"sigalet er {signal}")
    GPIO.cleanup()


if __name__ == "__main__":
    main()
