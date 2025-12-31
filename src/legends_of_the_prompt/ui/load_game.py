from textual.screen import Screen
from textual.widgets import Button, ListView, ListItem, Label
from textual.containers import Horizontal, Vertical

from legends_of_the_prompt.ui.delete_screen import DeleteScreen
from legends_of_the_prompt.ui.game_screen import GameScreen

from legends_of_the_prompt.utils.io import (
    delete_character_save,
    get_all_save_names,
    load_character_data,
)


class LoadGame(Screen):
    BORDER_TITLE = "Load Game"

    def compose(self):
        """Create child widgets for the Load Game screen."""
        save_names = get_all_save_names()

        with Vertical(id="load-game-container"):
            yield Label("Select your Character", id="select-character-label")
            with Horizontal(id="nested-load-game-container"):
                with ListView(id="save-list"):
                    for name in save_names:
                        yield ListItem(Label(name), id=name)
                with Vertical(id="load-game-buttons"):
                    yield Button.success(
                        "Load Character", id="load-game-btn", classes="load-menu-btn"
                    )
                    yield Button.error(
                        "Delete Character",
                        id="delete-game-btn",
                        classes="load-menu-btn",
                    )
                    yield Button(
                        "Back to Main Menu", id="load-back-btn", classes="load-menu-btn"
                    )

    def get_selected_character(self) -> str | None:
        save_list = self.query_one("#save-list", ListView)
        selected_item = save_list.highlighted_child
        if selected_item:
            return selected_item.id
        raise Exception("No character selected")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        def check_delete(result: bool) -> None:
            if result:
                character_name = self.get_selected_character()
                delete_character_save(character_name)
                self.notify(f"Deleted character: {character_name}")
                self.query_one(f"#{character_name}").remove()

        # Go back
        if event.button.id == "load-back-btn":
            self.app.pop_screen()
        # Load character
        elif event.button.id == "load-game-btn":
            character_data = load_character_data(self.get_selected_character())
            self.app.character_data = character_data
            self.app.push_screen(GameScreen())
        # Delete character
        elif event.button.id == "delete-game-btn":
            self.app.push_screen(
                DeleteScreen(self.get_selected_character()), check_delete
            )
