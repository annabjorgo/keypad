import inspect
from inspect import isfunction


class Rule():

    def __init__(self, state1, state2, signal, action):
        """State1 og state2 are strings. Action is a function that tells the agent what to do.
        Signal can be a symbol or a function that takes in a symbol and returns true if the symbol is valid for the rule"""
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action

    def match(self, state, sig):
        """Check whether the rule condition is fulfilled"""
        if (inspect.isfunction(self.signal) and self.signal(sig)) or (sig == self.signal):
            if state == self.state1:
                return True

    def fire(self, fsm, sig):
        """Use the consequent of a rule to a) set the next state of the FSM, and b)
        call the appropriate agent action method."""
        fsm.set_state(self.state2)
        self.action(sig)

    def __str__(self):
        return "state1: {}, signal: {}, state2: {}".format(self.state1, self.signal, self.state2)
