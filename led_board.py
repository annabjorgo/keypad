from GPIOSimulator_v5 import *
import time

GPIO = GPIOSimulator()


class Led_board:
    """ A charliplexed circuit with 6 leds and 3 pins"""

    def setup(self):
        GPIO.cleanup()
        GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.IN, state=GPIO.LOW)
        GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.IN, state=GPIO.LOW)
        GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.IN, state=GPIO.LOW)

    def light_led(self, led_num, duration_wait=0):
        """Turn on one of the 6 LEDs by making the appropriate combination of input
        and output declarations, and then making the appropriate HIGH / LOW settings on the
        output pins."""
        led_num = int(led_num)
        self.setup()
        if led_num == 0:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.HIGH)
            GPIO.show_leds_states()
            print('Led 0 on')

        elif led_num == 1:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.HIGH)
            GPIO.show_leds_states()
            print('Led 1 on')

        elif led_num == 2:
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)
            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.HIGH)
            GPIO.show_leds_states()
            print('Led 2 on')
        elif led_num == 3:
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.HIGH)
            GPIO.show_leds_states()
            print('Led 4 on')

        elif led_num == 4:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)
            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.HIGH)
            GPIO.show_leds_states()
            print('Led 5 on')

        elif led_num == 5:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.HIGH)
            GPIO.show_leds_states()
            print('Led 5 on')
        time.sleep(int(duration_wait))
        print('Led off')


    def flash_all_leds(self, k):
        """Flash all 6 LEDs on and off for k seconds, where k is an argument of the
        method."""
        print("Flashing")
        for i in range(6):
            self.light_led(i, k / 6)
            time.sleep(k / 6)
        print("------------------------")

    def twinkle_all_leds(self, k):
        """Turn all LEDs on and off in sequence for k seconds, where k is an
        argument of the method."""

        start_t = time.time()
        print("Twinkling")
        while time.time() - start_t < k:
            for i in range(6):
                self.light_led(i, 0.5)
                GPIO.show_leds_states()
        print("--------")


    def powering_up(self):
        """ Light show for startup """
        print("Powering up")
        self.light_led(3, 0.1)
        self.light_led(4, 0.1)
        self.light_led(5, 0.1)
        print("--------")


    def powering_down(self):
        """ Light show for shutdown """
        self.light_led(0, 0.1)
        self.light_led(1, 0.1)
        self.light_led(2, 0.1)
        print("--------")


def main():
    led_board = Led_board()
    led_board.twinkle_all_leds(4)


if __name__ == '__main__':
    main()
