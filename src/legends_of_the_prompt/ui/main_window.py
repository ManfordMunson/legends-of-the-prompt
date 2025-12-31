from textual.app import App

from legends_of_the_prompt.ui.main_menu import MainMenu
from legends_of_the_prompt.utils.io import get_all_css_files, save_character_data
from legends_of_the_prompt.utils.calculations import get_experience_needed_for_level
from legends_of_the_prompt.messages.action_progress import ActionProgress


class MainWindow(App):
    """A main window widget for the Legends of the Prompt game."""

    CSS_PATH = get_all_css_files()

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.push_screen(MainMenu())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def add_experience(self, skill: str, amount: int) -> None:
        """Add experience to a specific skill."""
        if hasattr(self, "character_data"):
            if skill in self.character_data.get("skills", {}):
                current_level = self.character_data["skills"][skill]["level"]
                xp_needed = get_experience_needed_for_level(current_level)
                self.character_data["skills"][skill]["experience"] += amount

                current_xp = self.character_data["skills"][skill]["experience"]
                self.screen.post_message(
                    ActionProgress(
                        action_name=skill,
                        xp=current_xp,
                        xp_needed=xp_needed,
                        current_level=current_level,
                    )
                )

                if xp_needed <= current_xp:
                    self.character_data["skills"][skill]["level"] += 1
                    self.character_data["skills"][skill]["experience"] -= xp_needed
                    self.notify(
                        f"{skill.capitalize()} leveled up to Level {self.character_data['skills'][skill]['level']}!"
                    )
                    save_character_data(self.character_data)

    def post_idle_status(self) -> None:
        """Post the current idle status to the top bar."""
        self.screen.post_message(
            ActionProgress(
                action_name="Idle",
                xp=0.0,
                xp_needed=100.0,
                current_level=0,
            )
        )
