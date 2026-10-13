
from pathlib import Path


class Search:

    def __init__(self, file_manager):
        self.file_manager = file_manager

    def search_by_name(self, name, recursive=False):
        # """Recherche par nom complet ou partiel."""
        directory = self.file_manager.current_directory

        elements = (
            directory.rglob("*")
            if recursive
            else directory.iterdir()
        )

        results = []

        for element in elements:
            if name.lower() in element.name.lower():
                results.append(element)

        return results

    def search_by_extension(self, extension, recursive=False):
        # """Recherche les fichiers selon leur extension."""
        directory = self.file_manager.current_directory

        extension = extension.lower()

        if not extension.startswith("."):
            extension = "." + extension

        elements = (
            directory.rglob("*")
            if recursive
            else directory.iterdir()
        )

        results = []

        for element in elements:
            if element.is_file() and element.suffix.lower() == extension:
                results.append(element)

        return results

    def search_by_type(self, element_type, recursive=False):
        # """Recherche des fichiers ou des dossiers."""
        directory = self.file_manager.current_directory

        elements = (
            directory.rglob("*")
            if recursive
            else directory.iterdir()
        )

        results = []

        for element in elements:
            if element_type == "fichier" and element.is_file():
                results.append(element)

            elif element_type == "dossier" and element.is_dir():
                results.append(element)

        return results

    def search_by_size(self, min_size=0, max_size=None, recursive=False):
        # """Recherche les fichiers selon leur taille en octets."""
        directory = self.file_manager.current_directory

        elements = (
            directory.rglob("*")
            if recursive
            else directory.iterdir()
        )

        results = []

        for element in elements:
            if not element.is_file():
                continue

            try:
                size = element.stat().st_size
            except OSError:
                continue

            if size >= min_size and (
                max_size is None or size <= max_size
            ):
                results.append(element)

        return results

    def display_results(self, results):
        # """Affiche les résultats d'une recherche."""
        if not results:
            print("Aucun résultat trouvé.")
            return

        print(f"\n{len(results)} résultat(s) trouvé(s) :")

        for element in results:
            element_type = "Dossier" if element.is_dir() else "Fichier"
            print(f"[{element_type}] {element}")

