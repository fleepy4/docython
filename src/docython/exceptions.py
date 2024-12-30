

class DocythonException(Exception):
    pass


class MissArgument(DocythonException):
    def __init__(self):
        super().__init__(
            "\nYou miss some argument\n"
            "Use -cfg for choice config file\n"
            "or use -f to choice single python file\n"
        )


class TooMuchArguments(DocythonException):
    def __init__(self):
        super().__init__(
            "You can input config OR single python file but not both"
        )

