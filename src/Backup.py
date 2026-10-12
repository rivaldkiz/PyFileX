from pathlib import Path

import shutil

class Backup:

    def __init__(self, fm, backup_directory):
        self.fm = fm
        self.bkd =Path(backup_directory).resolve()


    def create_backup_directory(self):
        self.bkd.mkdir(parents=True, exist_ok=True)
        return self.bkd


    # ==============================
    # INFO
    # ==============================
    def get_backup_directory(self):
        return self.bkd

    def list_backup(self):
        self.create_backup_directory()

        return sorted(self.bkd.iterdir()) 

    def get_unique_destination(self, destination):
            if not destination.exists():
                 return destination

            counter = 1

            while True:
                 new_name = (f"{destination.stem}_{counter}"
                             f"{destination.suffix}")

                 new_destination = (destination.parent / new_name)
                 if not new_destination.exists():
                      return new_destination

                 counter +=1

    # ==============================
    # SAVE FILE
    # ==============================


    def backup_file(self, name):
        source = (self.fm.current_directory / name).resolve()

        if not source.is_file():
            print(f"Impossible de sauvegarder :" 
                    f" '{name}' n'est pas un fichier. ")
            return False
        self.create_backup_directory()
        dest = (self.bkd / source.name)
        dest = self.get_unique_destination(dest)

        shutil.copy2(source, dest)

        print(f"Sauvegarde creee : {dest.name}")

        return True

            # ==============================
            # SAVE DIRECTORY
            # ==============================

    def backup_directory(self, name):
        source = (self.fm.current_directory / name).resolve()

        if not source.is_dir():
            print(f"Impossible de sauvegarder :" 
                    f" '{name}' n'est pas un dossier. ")
            return False

        # empeche la copie d'un dossier dans son propre contenu
        try:
             self.bdk.relative_to(source)
        except ValueError:
             pass
        else:
             print("Erreur : le dossier de sauvegarde ne peut pas situe le dossier a sauvegarder.")
             return False
        
        self.create_backup_directory()
        dest = (self.bkd / source.name)
        dest = self.get_unique_destination(dest)

        shutil.copytree(source, dest)

        print(f"Dossier sauvegarde : {dest.name}")

        return True

        # ==============================
        # FILE RESTORATION
        # ==============================

    def restore_file(self, back):
            source = (self.bkd / back).resolve()

            try:
                source.relative_to(self.bkd)
            except ValueError:
                 print("Chemin de sauvegarde non autorise")
                 return False

            if not source.is_file():
                 print(f"Sauvegarde introuvable : '{back}' ")
                 return False

            dest = (self.fm.current_directory(dest))

            shutil.copy2(source,dest)

            print(f"Fichier restaure : {dest.name}")

            return True