from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Button, Label, Static, ListView

from legends_of_the_prompt.ui.clock import Clock
from legends_of_the_prompt.ui.close_screen import CloseScreen

class MainWindow(App):
    """A main window widget for the Legends of the Prompt game."""
    BORDER_TITLE = "Main Menu"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = ["css/main_menu.tcss", "css/close_screen.tcss"]

    def compose(self) -> ComposeResult:
        """Create child widgets for the main window."""
        with VerticalScroll():
            yield Label("Legends of the Prompt", id="main-title")
            yield Button("Create New Game", classes="main-menu-btn")
            yield Button("Load Game", classes="main-menu-btn")
            yield Button("Settings", classes="main-menu-btn")
            yield Button("Exit", classes="main-menu-btn")
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.label == "Create New Game":
            pass
        elif event.button.label == "Load Game":
            pass
        elif event.button.label == "Settings":
            pass
        elif event.button.label == "Exit":
            self.app.push_screen(CloseScreen(), lambda result: self.exit() if result else None)
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"
