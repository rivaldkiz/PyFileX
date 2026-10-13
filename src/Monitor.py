
from pathlib import Path
from datetime import datetime


class Monitor:

    def __init__(self, file_manager):
        self.file_manager = file_manager
        self.previous_state = {}

    def scan_directory(self):
        # """Récupère l'état des fichiers et dossiers."""
        directory = self.file_manager.current_directory
        state = {}

        for element in directory.iterdir():
            try:
                stat = element.stat()

                state[element.name] = {
                    "type": "dossier" if element.is_dir() else "fichier",
                    "size": stat.st_size,
                    "modified": stat.st_mtime
                }

            except OSError:
                # L'élément peut avoir été supprimé pendant le scan.
                continue

        return state

    def start_monitoring(self):
        # """Enregistre l'état initial du répertoire."""
        self.previous_state = self.scan_directory()
        print("Surveillance initialisée.")
        print(f"Dossier surveillé : {self.file_manager.current_directory}")

    def check_changes(self):
        # """Compare l'état actuel avec l'état précédent."""
        current_state = self.scan_directory()

        previous_names = set(self.previous_state)
        current_names = set(current_state)

        added = current_names - previous_names
        deleted = previous_names - current_names
        common = previous_names & current_names

        changes_found = False

        for name in sorted(added):
            print(f"[AJOUTÉ] {name}")
            changes_found = True

        for name in sorted(deleted):
            print(f"[SUPPRIMÉ] {name}")
            changes_found = True

        for name in sorted(common):
            old = self.previous_state[name]
            new = current_state[name]

            if (
                old["size"] != new["size"]
                or old["modified"] != new["modified"]
                or old["type"] != new["type"]
            ):
                print(f"[MODIFIÉ] {name}")
                changes_found = True

        if not changes_found:
            print("Aucun changement détecté.")

        self.previous_state = current_state

    def show_state(self):
        # """Affiche les éléments présents actuellement."""
        state = self.scan_directory()

        print("\nÉtat actuel du dossier :")

        for name, info in sorted(state.items()):
            print(
                f"{info['type'].capitalize()} : {name} "
                f"({info['size']} octets)"
            )
