"""
Class for representing a move
"""
class Move:
    """
    This class is dedicated for representing a move for a character
    """
    def __init__(self,
                 move_name,
                 pln_cmd,
                 num_cmd,
                 cmd_name,
                 startup,
                 active):
        self.move_name = move_name
        self.plain_command = pln_cmd
        self.number_command = num_cmd
        self.command_name = cmd_name
        self.startup = startup
        self.active = active
