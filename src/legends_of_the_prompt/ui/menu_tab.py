from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Vertical

from legends_of_the_prompt.ui.close_screen import CloseScreen


class MenuTab(Static):
    def compose(self) -> ComposeResult:
        with Vertical(id="game-menu-container"):
            yield Button.success("Swag TODO", id="swag")
            yield Button.warning(
                "Return to Character Selection", id="game-menu-back-btn"
            )
            yield Button.error("Exit", id="game-menu-exit-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "swag":
            pass
        elif event.button.id == "game-menu-back-btn":
            self.app.pop_screen()
        elif event.button.id == "game-menu-exit-btn":
            self.app.push_screen(CloseScreen())
