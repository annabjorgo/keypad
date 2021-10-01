from kpc_agent import Agent
from rule import Rule


class FSM():
    """The Finite State Machine"""

    def __init__(self):
        """The FSM begins in state S-Init"""
        self.state = "S-init"
        self.agent = Agent()
        self.fsm_rule_list = [
            Rule('S-init', 'S-read', signal_is_any_symbol, self.agent.reset_passcode_entry),  # Initializing
            Rule('S-read', 'S-read', signal_is_digit, self.agent.append_digit),  # Reads digit
            Rule('S-read', 'S-verify', '*', self.agent.verify_login),  # Request for verification
            Rule('S-verify', 'S-active', 'Y', self.agent.d_function),  # Password accepted
            Rule('S-verify', 'S-init', 'N', self.agent.d_function),  # Password not accecpted
            Rule('S-active', 'S-read-2', '*', self.agent.reset_passcode_entry2),  # Attempt to change password
            Rule('S-read-2', 'S-read-2', signal_is_digit, self.agent.append_digit),  # Reads digit
            Rule('S-read-2', 'S-active', '*', self.agent.validate_passcode_change),  # Validates new password
            Rule('S-active', 'S-led', signal_is_valid_led, self.agent.select_led),  # Selects a led
            Rule('S-led', 'S-time', '*', self.agent.reset_duration),  # Resets duration
            Rule('S-time', 'S-time', signal_is_digit, self.agent.add_duration_digit),  # Adds digit to duration
            Rule('S-time', 'S-active', '*', self.agent.light_one_led),  # Light chosen led for "duration" time
            Rule('S-active', 'S-logout', '#', self.agent.logout1),  # Start logout process
            Rule('S-logout', 'S-final', '#', self.agent.exit_action)  # Finish logout process
        ]

    def add_rule(self, rule):
        """Add a new rule to the end of the FSM’s rule list"""
        self.fsm_rule_list.append(rule)

    def get_next_signal(self):
        """Query the agent for the next signal"""
        return self.agent.get_next_signal()

    def run(self):
        """Begin in the FSM’s default initial state and then repeatedly call get next signal and
        run the rules one by one until reaching the final state"""
        self.set_state('S-init')
        while self.state != 'S-final':
            print(self.state)
            next_signal = self.get_next_signal()
            for rule in self.fsm_rule_list:
                if rule.match(self.state, next_signal):
                    rule.fire(self, next_signal)
                    break

    def set_state(self, state):
        self.state = state

    def get_agent(self):
        return self.agent


def signal_is_digit(signal): return 48 <= ord(signal) <= 57


def signal_is_any_symbol(*_): return True


def signal_is_valid_led(signal): return 48 <= ord(signal) <= 54


def main():
    """The main function for keypad for testing purposes"""
    fsm = FSM()
    fsm.run()


if __name__ == "__main__":
    main()
