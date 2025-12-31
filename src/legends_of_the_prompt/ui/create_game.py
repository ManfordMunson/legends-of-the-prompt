import json
from pathlib import Path
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Vertical, HorizontalGroup
from textual.widgets import Button, Input, Label

from legends_of_the_prompt.ui.game_screen import GameScreen


class CreateGame(Screen):
    BORDER_TITLE = "Create New Game"

    def compose(self) -> ComposeResult:
        """Create child widgets for the create game screen."""
        with Vertical(id="create-game-menu"):
            yield Label("Character Name", id="character-name-label")
            yield Input(
                placeholder="Enter your character's name", id="character-name-input"
            )
            with HorizontalGroup(id="create-game-buttons"):
                yield Button.success("Start Game", id="start-game-btn")
                yield Button("Back to Main Menu", id="back-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Start game
        if event.button.id == "start-game-btn":
            character_name_input = self.query_one("#character-name-input", Input)
            character_name = character_name_input.value.strip()
            default_character = {
                "name": character_name,
                "level": 1,
                "experience": 0.0,
                "skills": {
                    "woodcutting": {"level": 1, "experience": 0.0},
                    "mining": {"level": 1, "experience": 0.0},
                    "fishing": {"level": 1, "experience": 0.0},
                    "combat": {"level": 1, "experience": 0.0},
                },
            }
            # Make sure the directory exists
            save_dir = Path("data") / "saves"
            file_path = save_dir / f"{character_name}.json"
            save_dir.mkdir(parents=True, exist_ok=True)

            with open(file_path, "w") as file:
                json.dump(default_character, file, indent=4)

            self.app.push_screen(GameScreen(default_character))
        # Go back
        elif event.button.id == "back-btn":
            self.app.pop_screen()
