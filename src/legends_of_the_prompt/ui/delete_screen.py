from textual.screen import ModalScreen
from textual.widgets import Input, Label, Button
from textual.containers import Vertical, HorizontalGroup


class DeleteScreen(ModalScreen[bool]):
    def __init__(self, character_name: str):
        super().__init__()
        self.character_name = character_name

    def compose(self):
        with Vertical(id="delete-dialog"):
            yield Label(
                f"Are you sure you want to delete [b red]{self.character_name}[/b red]?"
            )
            yield Label("Type [b]DELETE[/b] to confirm:")
            yield Input(placeholder="Type DELETE here...", id="delete-input")
            with HorizontalGroup(id="delete-actions"):
                yield Button(
                    "Confirm Deletion", variant="error", id="confirm", disabled=True
                )
                yield Button("Cancel", variant="primary", id="cancel")

    def on_input_changed(self, event: Input.Changed):
        # Enable the button only if the word matches exactly
        self.query_one("#confirm").disabled = event.value != "DELETE"

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "confirm":
            self.dismiss(True)
        else:
            self.dismiss(False)
