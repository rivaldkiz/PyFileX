from pathlib import Path


class Navigation :

    def __init__(self, file_manager):
        self.fm = file_manager

     # ==============================
     # INFORMATION
        # ==============================

    def pwd(self):
        return self.fm.current_directory

    def get_parent(self):
        return self.fm.current_directory.parent

    def get_parts(self):
        return self.fm.current_directory.parts

    # ==============================
    # MODIFICATION
    # ==============================
    
    def is_absolute_path(self, path):

        return Path(path).is_absolute


    # """
    #     Transforme un chemin relatif en chemin absolu
    #     puis le résout.
    # """
    def resolve_path(self, path):
        path = Path(path)

        if not path.is_absolute():
            path = self.fm.current_directory / path
        
        return path.resolve()

    # ==========================================
    # NAVIGATION
    # ==========================================

    def cd(self, path):

        path = Path(path)

        # si chemin relatif

        if not path.is_absolute():
            path = self.fm.current_directory / path

        path = path.resolve()

        # verifit si existe
        if not path.exists():
            print(f"'{path}' n'existe pas .")
            return False


        # verifit si dossier

        if not path.is_dir():
            print(f"'{path}' n'est pas un dossier.")
            return False

        self.fm.current_directory = path

        return True

    def back(self):
        # """
        # Retourne au dossier parent.
        # """

        current = self.fm.current_directory
        parent = current.parent

        if parent == current:

            print("Vous etes deja a la racine \n ")
            return False

        self.fm.current_directory = parent
        return True


    def go_home(self):

        self.fm.current_directory = Path.home()

        return True



    
    # ==========================================
    # CONTENU
    # ==========================================
    def ls(self):
        # """
        # Retourne le contenu du répertoire courant.
        # """
        self.fm.list_directory()


    def tree(self, path=None, level=0):
        # """
        # Affiche récursivement l'arborescence.
        # """

        if path is None:
            path = self.fm.current_directory

        path = Path(path)

        indentation = "     " * level

        print(f"{indentation}{path.name}/")

        # return an ascending list of element
        for element in sorted(path.iterdir()):

            if element.is_dir():
                self.tree(element, level + 1)

            else:

                print(f"{'      ' * (level + 1)}{element.name} \n")


        