import json
from pathlib import Path


def load_character_data(character_name):
    save_path = Path("data") / "saves" / f"{character_name}.json"

    if not save_path.exists():
        return None

    try:
        with open(save_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        print(f"Error: {save_path} is corrupted.")
        return None


def get_all_save_names():
    save_dir = Path("data") / "saves"

    # Create the directory if it doesn't exist to avoid errors during scanning
    save_dir.mkdir(parents=True, exist_ok=True)

    # Find all .json files and return just the names (without the .json extension)
    return [file.stem for file in save_dir.glob("*.json")]


def get_all_css_files():
    css_dir = Path(__file__).parent.parent / "ui" / "css"
    return [str(file) for file in css_dir.glob("*.tcss")]


def delete_character_save(character_name: str):
    save_path = Path("data") / "saves" / f"{character_name}.json"
    if save_path.exists():
        save_path.unlink()
        return True
    else:
        return False


def save_character_data(character_data: dict):
    save_path = Path("data") / "saves" / f"{character_data['name']}.json"
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(character_data, f, indent=4)
