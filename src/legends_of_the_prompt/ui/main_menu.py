from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Label
from textual.screen import Screen

from legends_of_the_prompt.ui.create_game import CreateGame
from legends_of_the_prompt.ui.close_screen import CloseScreen
from legends_of_the_prompt.ui.load_game import LoadGame


class MainMenu(Screen):
    BORDER_TITLE = "Main Menu"

    def compose(self) -> ComposeResult:
        """Create child widgets for the main window."""
        with Vertical(id="main-menu"):
            yield Label("Legends of the Prompt", id="main-title")
            yield Button("Create New Game", classes="main-menu-btn")
            yield Button("Load Game", classes="main-menu-btn")
            yield Button("Settings", classes="main-menu-btn")
            yield Button("Exit", classes="main-menu-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.label == "Create New Game":
            self.app.push_screen(CreateGame())
        elif event.button.label == "Load Game":
            self.app.push_screen(LoadGame())
        elif event.button.label == "Settings":
            pass
        elif event.button.label == "Exit":
            self.app.push_screen(CloseScreen())
