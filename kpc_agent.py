import keypad
import led_board
from led_board import Led_board
import rule
import GPIOSimulator_v5



class Agent:
    """Random doc:)"""

    def __init__(self):
        self.keypad = keypad.KeyPad()
        self.led_board = Led_board()
        self.pathname = 'password.txt'
        self.override_signal = None
        self.cump = ''
        self.led_num = ''
        self.led_dur = ''

    def append_digit(self, digit):
        self.cump += digit
        print('Cumulative password: {}'.format(self.cump))

    def read_password(self, *_):
        """ Reads and returns password from file """
        with open(self.pathname, 'r') as password_file:
            return password_file.readline().rstrip('\n')

    def reset_passcode_entry(self, *_):
        """Clear the passcode-buffer and initiate a “power up” lighting sequence on the LED Board."""
        # Method is called when user tries to log in and when user tries to change password
        self.cump = ''
        self.led_board.powering_up()
        print('Enter password')

    def reset_passcode_entry2(self, *_):
        """Clear the passcode-buffer and initiate a “power up” lighting sequence on the LED Board."""
        # Method is called when user tries to log in and when user tries to change password
        self.cump = ''
        self.led_board.powering_up()
        print('Enter new password')

    def get_next_signal(self, *_):
        if self.override_signal is not None:
            sig = self.override_signal
            self.override_signal = None
            return sig
        else:
            # query the keypad for the next pressed key
            return self.keypad.get_next_signal()

    def verify_login(self, *_):
        """Check that the password just entered via the keypad matches that in the
        password file. Store the result (Y or N) in the override signal. Also, this should call the
        LED Board to initiate the appropriate lighting pattern for login success or failure."""
        # Not implemented yet
        current_password = self.read_password()
        if self.cump == current_password:
            self.twinkle_leds()
            print('Correct password')
            self.override_signal = 'Y'
        else:
            self.flash_leds()
            print('Wrong password')
            self.override_signal = 'N'
        self.cump = ''

    def validate_passcode_change(self, *_):
        """  Check that the new password is legal. If so, write the new
        password in the password file. A legal password should be at least 4 digits long and should
        contain no symbols other than the digits 0-9. As in verify login, this should use the LED
        Board to signal success or failure in changing the password."""
        if self.cump.isdigit() and len(self.cump) >= 4:
            with open(self.pathname, 'w') as password_file:
                password_file.write(self.cump)
            self.twinkle_leds()
            print('New password saved')
        else:
            self.flash_leds()
            print('Password must be at least 4 digits and only digits 0-9')



    def select_led(self, led_digit):
        print('Led {} is selected'.format(led_digit))
        self.led_num = led_digit

    def reset_duration(self, *_):
        print('Enter duration')
        self.led_dur = ''

    def add_duration_digit(self, digit):
        self.led_dur += digit
        print('Current duration: {}'.format(self.led_dur))

    def logout1(self, *_):
        print('Press # again to log out')

    def light_one_led(self, *_):
        """ Using values stored in the Lid and Ldur slots, call the LED Board and
        request that LED # Lid be turned on for Ldur seconds"""
        self.led_board.light_led(self.led_num, self.led_dur)

    def flash_leds(self):
        """Call the LED Board and request the flashing of all LEDs."""
        self.led_board.flash_all_leds(1)

    def twinkle_leds(self):
        """Call the LED Board and request the twinkling of all LEDs."""
        self.led_board.twinkle_all_leds(1)

    def exit_action(self, *_):
        """Call the LED Board to initiate the “power down” lighting sequence."""
        self.led_board.powering_down()
        print('Logging out.')


    def d_function(self, *_):
        """Dummy function"""
        pass

