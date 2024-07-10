
class ApiErrorException(Exception):
    def __init__(self, *args):
        assert(len(args) >= 2)
        self.error_code     = args[0]
        self.error_message  = args[1]
        self.add_note(args[0]+": "+args[1])