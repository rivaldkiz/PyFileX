import shutil

class Organizer:

    def __init__(self, file_manager):
        self.fm = file_manager
     
        self.categories = {
            "Images": [ ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg" ],
            "Documents": [ ".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".ppt", ".pptx" ],
            "Musique": [ ".mp3", ".wav", ".flac", ".aac", ".ogg" ], 
            "Videos": [ ".mp4", ".avi", ".mkv", ".mov", ".webm" ], 
            "Python": [ ".py", ".pyw" ] 
            }

        # ==============================
        # INFORMATIONS
        # ==============================

    def get_category(self, file):

        extension = file.suffix.lower()

        for category, extension in self.categories.items():

            if extension in extension:
                return category

        return "Autres"

    # ==============================
    # CREATION DE DOSSIER
    # ==============================


    def create_category_directory(self, category):
        directory = (
            self.fm.current_directory / category
        )

        directory.mkdir(parents=True, exist_ok=True)

        return directory


        # ==============================
        # GESTION DES CONFLICTS
        # ==============================

    @classmethod
    def get_unique_destination(cls, destination):

        # Retourne un chemin disponible si un fichier portant le même nom existe déjà. 

        if not destination.exists():
            return destination

        counter = 1

        while True:

            new_name = (
                f"{destination.stem}"
                f"_{counter}"
                f"{destination.suffix}"
            )

            new_destination = (
                destination.parent / new_name
            )


            if not new_destination.exists():
                return new_destination
            
            counter += 1

        # ==============================
        # GESTION DES CONFLICTS
        # ==============================

    def organize(self):

        current_directory = self.fm.current_directory

        for element in current_directory.iterdir():

            # ignorer les dossier
            if not element.is_file():
                continue

            category = self.get_category(element)

            destination_directory = self.create_category_directory(category)

            # chemin initial
            destination = destination_directory / element.name


            # eviter les conflicts

            destination = Organizer.get_unique_destination(destination)

            # deplacer le fichier
            shutil.move(str(element),str(destination))

            print(
                f"[OK] {element.name} "
                f"→ {category}/{destination.name}"
            )

            print("Organisation terminee")
