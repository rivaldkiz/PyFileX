
from pathlib import Path


class Analyzer:

    def __init__(self, file_manager):
        self.file_manager = file_manager

    def get_size(self, path):
        """Retourne la taille d'un fichier en octets."""
        path = Path(path)

        if not path.is_file():
            return 0

        try:
            return path.stat().st_size
        except OSError:
            return 0

    def format_size(self, size):
        """Convertit les octets en unité lisible."""
        units = ["o", "Ko", "Mo", "Go", "To"]

        size = float(size)

        for unit in units:
            if size < 1024 or unit == "To":
                return f"{size:.2f} {unit}"
            size /= 1024

    def scan_directory(self, recursive=False):
        """Analyse le dossier courant."""
        directory = self.file_manager.current_directory

        elements = (
            directory.rglob("*")
            if recursive
            else directory.iterdir()
        )

        files = []
        directories = []

        for element in elements:
            try:
                if element.is_file():
                    files.append(element)
                elif element.is_dir():
                    directories.append(element)
            except OSError:
                continue

        return files, directories

    def get_total_size(self, recursive=False):
        """Calcule la taille totale des fichiers."""
        files, _ = self.scan_directory(recursive)

        return sum(self.get_size(file) for file in files)

    def get_extension_stats(self, recursive=False):
        """Compte les fichiers par extension."""
        files, _ = self.scan_directory(recursive)
        stats = {}

        for file in files:
            extension = file.suffix.lower() or "Sans extension"
            stats[extension] = stats.get(extension, 0) + 1

        return stats

    def get_largest_files(self, limit=5, recursive=False):
        """Retourne les fichiers les plus volumineux."""
        files, _ = self.scan_directory(recursive)

        files_with_size = [
            (file, self.get_size(file))
            for file in files
        ]

        files_with_size.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return files_with_size[:max(0, limit)]

    def show_report(self, recursive=False):
        """Affiche un rapport complet."""
        files, directories = self.scan_directory(recursive)
        total_size = sum(self.get_size(file) for file in files)

        print("\n" + "=" * 45)
        print("          RAPPORT DE STOCKAGE")
        print("=" * 45)

        print(f"Dossier analysé : {self.file_manager.current_directory}")
        print(f"Nombre de fichiers : {len(files)}")
        print(f"Nombre de dossiers : {len(directories)}")
        print(f"Taille totale : {self.format_size(total_size)}")

        print("\n--- Répartition par extension ---")

        stats = self.get_extension_stats(recursive)

        if stats:
            for extension, count in sorted(stats.items()):
                print(f"{extension} : {count} fichier(s)")
        else:
            print("Aucun fichier.")

        print("\n--- Les fichiers les plus volumineux ---")

        largest_files = self.get_largest_files(
            limit=5,
            recursive=recursive
        )

        if largest_files:
            for file, size in largest_files:
                print(f"{file.name} : {self.format_size(size)}")
        else:
            print("Aucun fichier.")
