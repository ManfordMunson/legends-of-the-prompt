from textual.message import Message


class ActionProgress(Message, bubble=True):
    """Message indicating progress of an action."""

    def __init__(
        self, action_name: str, xp: float, xp_needed: float, current_level: int
    ) -> None:
        self.action_name = action_name
        self.xp = xp
        self.xp_needed = xp_needed
        self.current_level = current_level
        super().__init__()
