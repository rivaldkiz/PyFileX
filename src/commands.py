
from pathlib import Path

from FileManager import FileManager
from Navigation import Navigation
from Search import Search
from Organizer import Organizer
from Backup import Backup
from Analyzer import Analyzer
from Monitor import Monitor


class Commands:

    def __init__(self):
        self.file_manager = FileManager()

        self.navigation = Navigation(self.file_manager)
        self.search = Search(self.file_manager)
        self.organizer = Organizer(self.file_manager)

        backup_directory = Path.home() / "PyFileX_Backups"
        self.backup = Backup(
            self.file_manager,
            backup_directory
        )

        self.analyzer = Analyzer(self.file_manager)
        self.monitor = Monitor(self.file_manager)

    def show_menu(self):
        print("\n" + "=" * 40)
        print("             PyFileX")
        print("=" * 40)
        print("1. Afficher le dossier courant")
        print("2. Lister le contenu")
        print("3. Changer de dossier")
        print("4. Revenir au dossier parent")
        print("5. Créer un fichier")
        print("6. Créer un dossier")
        print("7. Renommer un élément")
        print("8. Supprimer un fichier")
        print("9. Supprimer un dossier vide")
        print("10. Rechercher par nom")
        print("11. Rechercher par extension")
        print("12. Organiser les fichiers")
        print("13. Sauvegarder un fichier")
        print("14. Sauvegarder un dossier")
        print("15. Analyser le stockage")
        print("16. Initialiser la surveillance")
        print("17. Vérifier les changements")
        print("18. Afficher les sauvegardes")
        print("0. Quitter")
        print("=" * 40)

    def list_directory(self):
        elements = self.navigation.ls()

        if not elements:
            print("Ce dossier est vide.")
            return

        for element in sorted(elements):
            kind = "DOSSIER" if element.is_dir() else "FICHIER"
            print(f"[{kind}] {element.name}")

    def create_file(self):
        name = input("Nom du fichier : ").strip()

        if name:
            self.file_manager.create_file(name)
        else:
            print("Le nom ne peut pas être vide.")

    def create_directory(self):
        name = input("Nom du dossier : ").strip()

        if name:
            self.file_manager.create_directory(name)
        else:
            print("Le nom ne peut pas être vide.")

    def rename_element(self):
        old_name = input("Nom actuel : ").strip()
        new_name = input("Nouveau nom : ").strip()

        if old_name and new_name:
            self.file_manager.rename(old_name, new_name)
        else:
            print("Les deux noms sont obligatoires.")

    def delete_file(self):
        name = input("Nom du fichier à supprimer : ").strip()

        if not name:
            print("Le nom ne peut pas être vide.")
            return

        confirmation = input(
            f"Confirmer la suppression de '{name}' ? (o/n) : "
        ).strip().lower()

        if confirmation == "o":
            self.file_manager.delete_file(name)
        else:
            print("Suppression annulée.")

    def delete_directory(self):
        name = input("Nom du dossier vide à supprimer : ").strip()

        if not name:
            print("Le nom ne peut pas être vide.")
            return

        confirmation = input(
            f"Confirmer la suppression de '{name}' ? (o/n) : "
        ).strip().lower()

        if confirmation == "o":
            self.file_manager.delete_directory(name)
        else:
            print("Suppression annulée.")

    def change_directory(self):
        path = input("Chemin du dossier : ").strip()

        if path:
            if self.navigation.cd(path):
                print(f"Nouveau dossier : {self.navigation.pwd()}")

    def search_by_name(self):
        name = input("Nom ou partie du nom : ").strip()

        if not name:
            print("La recherche ne peut pas être vide.")
            return

        recursive = input(
            "Inclure les sous-dossiers ? (o/n) : "
        ).strip().lower() == "o"

        results = self.search.search_by_name(name, recursive)
        self.search.display_results(results)

    def search_by_extension(self):
        extension = input("Extension recherchée (ex. pdf) : ").strip()

        if not extension:
            print("L'extension ne peut pas être vide.")
            return

        recursive = input(
            "Inclure les sous-dossiers ? (o/n) : "
        ).strip().lower() == "o"

        results = self.search.search_by_extension(
            extension,
            recursive
        )
        self.search.display_results(results)

    def organize_files(self):
        confirmation = input(
            "Les fichiers seront déplacés dans des catégories. "
            "Continuer ? (o/n) : "
        ).strip().lower()

        if confirmation == "o":
            self.organizer.organize()
        else:
            print("Organisation annulée.")

    def backup_file(self):
        name = input("Nom du fichier à sauvegarder : ").strip()

        if name:
            self.backup.backup_file(name)
        else:
            print("Le nom ne peut pas être vide.")

    def backup_folder(self):
        name = input("Nom du dossier à sauvegarder : ").strip()

        if name:
            self.backup.backup_folder(name)
        else:
            print("Le nom ne peut pas être vide.")

    def analyze_storage(self):
        recursive = input(
            "Inclure les sous-dossiers ? (o/n) : "
        ).strip().lower() == "o"

        self.analyzer.show_report(recursive)

    def show_backups(self):
        backups = self.backup.list_backups()

        if not backups:
            print("Aucune sauvegarde disponible.")
            return

        for item in backups:
            kind = "DOSSIER" if item.is_dir() else "FICHIER"
            print(f"[{kind}] {item.name}")

    def run(self):
        while True:
            print(f"\nDossier courant : {self.navigation.pwd()}")
            self.show_menu()

            choice = input("Choix : ").strip()

            try:
                if choice == "1":
                    print(self.navigation.pwd())

                elif choice == "2":
                    self.list_directory()

                elif choice == "3":
                    self.change_directory()

                elif choice == "4":
                    self.navigation.back()

                elif choice == "5":
                    self.create_file()

                elif choice == "6":
                    self.create_directory()

                elif choice == "7":
                    self.rename_element()

                elif choice == "8":
                    self.delete_file()

                elif choice == "9":
                    self.delete_directory()

                elif choice == "10":
                    self.search_by_name()

                elif choice == "11":
                    self.search_by_extension()

                elif choice == "12":
                    self.organize_files()

                elif choice == "13":
                    self.backup_file()

                elif choice == "14":
                    self.backup_folder()

                elif choice == "15":
                    self.analyze_storage()

                elif choice == "16":
                    self.monitor.start_monitoring()

                elif choice == "17":
                    self.monitor.check_changes()

                elif choice == "18":
                    self.show_backups()

                elif choice == "0":
                    print("Fermeture de PyFileX.")
                    break

                else:
                    print("Choix invalide.")

            except (OSError, PermissionError) as error:
                print(f"Erreur d'accès au fichier : {error}")

            except Exception as error:
                print(f"Une erreur inattendue est survenue : {error}")
