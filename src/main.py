from FileManager import FileManager


# ==========================================
# PROGRAMME PRINCIPAL
# ==========================================

# manager = FileManager()

# print("================================")
# print("       PyFileX - Niveau 1       ")
# print("================================")

# print("\nRepertoire courant :")
# print(manager.get_current_directory())

# print("\n--- Creation des dossiers ---")

# manager.create_directory("Documents")
# manager.create_directory("Images")

# print("\n--- Creation des fichiers ---")

# manager.create_file("test.txt")
# manager.create_file("photo.jpg")

# print("\n--- Vérifications ---")

# print("Documents existe :",manager.directory_exists("Documents"))

# print("Documents est un dossier :",manager.is_directory("Documents"))

# print("test.txt existe :",manager.file_exists("test.txt"))

# print("\n--- Informations sur photo.jpg ---")

# print("Nom :",manager.get_file_name("photo.jpg"))

# print("Extension :",manager.get_file_extension("photo.jpg"))

# print("Nom sans extension :",manager.get_file_stem("photo.jpg"))

# print("\n--- Contenu du dossier ---")

# for element in manager.list_directory():
#     print(element)

# print("\n--- Chemin absolu ---")

# print(manager.get_absolute_path("photo.jpg"))


manager = FileManager()

print("Répertoire :", manager.get_current_directory())

manager.create_directory("Test")
manager.create_file("test.txt")

print("\nContenu :")

for element in manager.list_directory():
    print(element)

print("\nRenommage :")

manager.rename("test.txt", "document.txt")

print("\nSuppression du fichier :")

manager.delete_file("document.txt")

print("\nSuppression du dossier :")

manager.delete_directory("Test")
