from textual.containers import HorizontalGroup, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label


class CloseScreen(ModalScreen):
    def compose(self):
        with Vertical(id="dialog"):
            yield Label("Are you sure you want to quit?", id="question")
            with HorizontalGroup(id="buttons"):
                yield Button("Yes", variant="error", id="yes")
                yield Button("No", variant="primary", id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.app.exit()
        else:
            self.app.pop_screen()
