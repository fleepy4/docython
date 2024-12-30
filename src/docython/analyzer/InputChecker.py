from argparse import Namespace
from ..exceptions import MissArgument, TooMuchArguments


class InputChecker:
    """
    class which contains methods to check CLI input
    """
    def __init__(self, parser: Namespace):
        self.parser = parser

    def check_input_completeness(self):
        if not self.parser.file and not self.parser.cfg:
            raise MissArgument
        if self.parser.file and self.parser.cfg:
            raise TooMuchArguments
