from pathlib import Path



class FileManager:

    def __init__(self):
        self.current_directory = Path.cwd()


    # ==============================
    # INFORMATIONS
    # ==============================

    def get_current_directory(self):
        return self.current_directory

    def get_absolute_path(self, name):
        path = self.current_directory / name
        return path.absolute()

    def get_file_name(self, name):
        path = Path(name)
        return path.name

    def get_file_extension(self, name):
        path = Path(name)
        return path.suffix

    def get_file_stem(self, name):
        path = Path(name)
        # retourne le nom du fichier sans sa derniere extension
        return path.stem


    # ==============================
    # VERIFICATIONS
    # ==============================

    def file_exists(self, name):
        path = self.current_directory / name
        return path.is_file()

    def is_directory(self, name):
        path = self.current_directory / name
        return path.is_dir()
    
   

    def directory_exists(self, name):
        path = self.current_directory / name
        return path.exists()

    # ==============================
    # LECTURE
    # ==============================
    def list_directory(self):
        # itere le contenu d'un dossier
        return list(self.current_directory.iterdir())



    # ==============================
    # CREATION
    # ==============================
    def create_file(self, name):
        path = self.current_directory / name

        if path.exists():
            print(f"'{name}' existe déjà.")
            return False
        
        # creer un fichier
        path.touch()
        print(f"Fichier '{name}' créé.")
        return True

    def create_directory(self, name):
        path = self.current_directory / name

        if path.exists():
            print(f"Le dossier {name} existe deja")
            return False

        path.mkdir()
        print(f"Le dossier {name} a ete cree ")
        return True 

    # ==============================
    # MODIFICATION
    # ==============================

    def rename(self, old_name, new_name):

        old_path = self.current_directory / old_name
        new_path = self.current_directory / new_name

        if not old_path.exists():
            print(f" '{old_name}' n'existe pas ")
            return False

        if new_path.exists():
                print(f" '{new_name}' existe deja ")
                return False

        old_path.rename(new_path)

        print(f"'{old_name}'a été renommé en '{new_name}'.")

        return True

    # ==============================
    # SUPPRESSION
    # ==============================

    def delete_file(self, name):

        path = self.current_directory / name

        if not path.exists():
            print(f"'{name}' n'existe pas.")
            return False

        if not path.is_file():
            print(f"'{name}' n'est pas un fichier.")
            return False

        path.unlink()

        print(f"Fichier '{name}' supprimé.")

        return True

    def delete_directory(self, name):

        path = self.current_directory / name

        if not path.exists():
            print(f"'{name}' n'existe pas.")
            return False

        if not path.is_dir():
            print(f"'{name}' n'est pas un dossier.")
            return False

# any() vérifie s'il existe au moins un élément dans l'iteration.
        if any(path.iterdir()):
            print(f"Le dossier '{name}' n'est pas vide.")
            return False

        path.rmdir()

        print(f"Dossier '{name}' supprimé.")

        return True


   

   

    

