
from pathlib import Path
from datetime import datetime


def format_size(size):
    # """Convertit une taille en octets vers une unité lisible."""
    units = ["o", "Ko", "Mo", "Go", "To"]
    size = float(size)

    for unit in units:
        if size < 1024 or unit == "To":
            return f"{size:.2f} {unit}"
        size /= 1024


def get_timestamp():
    # """Retourne la date et l'heure actuelles."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def is_valid_name(name):
    # """Vérifie qu'un nom n'est pas vide et ne contient pas de séparateur."""
    if not isinstance(name, str) or not name.strip():
        return False

    if name in {".", ".."}:
        return False

    return (
        "/" not in name
        and "\\" not in name
        and Path(name).name == name
    )


def get_extension(path):
    # """Retourne l'extension en minuscules, ou une chaîne vide."""
    return Path(path).suffix.lower()


def ensure_directory(path):
    # """Crée un dossier s'il n'existe pas."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def format_number(number):
    # """Affiche un nombre avec des séparateurs de milliers."""
    return f"{number:,}".replace(",", " ")
