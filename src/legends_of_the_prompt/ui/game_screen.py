from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import TabbedContent, TabPane, Label, Static, ProgressBar
from textual.containers import Vertical, Horizontal

from legends_of_the_prompt.messages.action_progress import ActionProgress
from legends_of_the_prompt.ui.menu_tab import MenuTab
from legends_of_the_prompt.ui.woodcutting_tab import WoodcuttingTab


class GameScreen(Screen):
    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        # Top Bar for quick stats
        with Horizontal(id="top-bar"):
            with Vertical(id="top-stats-bar"):
                yield Label(f"Name: [b]{self.app.character_data['name']}[/b]")
                yield Label(f"Level: {self.app.character_data.get('level', 1)}")
                yield Label(
                    f"Experience: [green]{self.app.character_data.get('experience', 0)}[/green]"
                )
            with Vertical(id="top-skills-bar"):
                yield Label("Current Task: IDLE", id="current-task-label")
                yield Label("Current Level: 0", id="current-level-label")
                yield ProgressBar(total=100, id="current-task-progress-bar")

        # Main Tabbed Interface
        with TabbedContent(initial="stats"):
            with TabPane("Woodcutting", id="woodcutting", classes="game-tab-container"):
                yield WoodcuttingTab(classes="tab-container")

            with TabPane("Attributes", id="stats", classes="game-tab-container"):
                yield Vertical(
                    Label(f"Strength: {self.app.character_data.get('strength', 10)}"),
                    Label(f"Agility: {self.app.character_data.get('agility', 10)}"),
                    Label(
                        f"Intelligence: {self.app.character_data.get('intelligence', 10)}"
                    ),
                    classes="tab-container",
                )
            with TabPane("Inventory", id="inventory", classes="game-tab-container"):
                yield Static(
                    "Your backpack is currently empty.", classes="tab-container"
                )
            with TabPane("Quest Log", id="quests", classes="game-tab-container"):
                yield Static("No active quests.", classes="tab-container")

            with TabPane("Menu", id="menu", classes="game-tab-container"):
                yield MenuTab(classes="tab-container")

    def on_action_progress(self, message: ActionProgress) -> None:
        self.query_one("#current-task-label", Label).update(
            f"Current Task: {message.action_name}"
        )
        self.query_one("#current-level-label", Label).update(
            f"Current Level: {message.current_level}"
        )

        if message.xp_needed > 0:
            percentage = (message.xp / message.xp_needed) * 100
            self.query_one("#current-task-progress-bar").progress = percentage
