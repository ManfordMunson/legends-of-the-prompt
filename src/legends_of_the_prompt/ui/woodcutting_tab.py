from textual.app import ComposeResult
from textual.widgets import Static, Label, ProgressBar, Button
from textual.containers import Vertical


class WoodcuttingTab(Static):
    """A tab for woodcutting skill interface."""

    def compose(self) -> ComposeResult:
        with Vertical(classes="tab-container"):
            yield Label("[b]Forest Area[/b]", id="area-title")
            yield Label("Tree Type: Oak", classes="tree-info")

            yield ProgressBar(
                total=100,
                id="chop-progress",
                show_percentage=True,
            )

            yield Label("Idle Status: Waiting...", id="action-text")
            yield Button("Start Chopping", variant="success", id="btn-chop")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-chop":
            self.toggle_chopping()

    def toggle_chopping(self) -> None:
        btn = self.query_one("#btn-chop")
        status = self.query_one("#action-text")

        if btn.variant == "success":
            # Start the timer (ticks every 100ms)
            self.chop_timer = self.set_interval(0.1, self.tick_chopping)
            btn.label = "Stop Chopping"
            btn.variant = "error"
            status.update("[yellow]Chopping Oak...[/yellow]")
        else:
            # Stop the timer
            self.chop_timer.stop()
            self.app.post_idle_status()
            btn.label = "Start Chopping"
            btn.variant = "success"
            status.update("Idle Status: Waiting...")

    def tick_chopping(self) -> None:
        bar = self.query_one("#chop-progress")
        bar.advance(5)  # 2 seconds to finish a tree

        if bar.progress >= 100:
            bar.progress = 0
            self.app.notify("Tree felled! +10 XP")
            xp = 10.0
            self.app.add_experience("woodcutting", xp)
