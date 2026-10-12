from FileManager import FileManager
from Navigation import Navigation


file_manager = FileManager()

navigation = Navigation(file_manager)


print("================================")
print("          PyFileX")
print("================================")

print("\nRépertoire courant :")
file_manager.create_directory("PyFileXTest")
navigation.cd("PyFileXTest")
print(navigation.pwd())

print("\nContenu :")

for element in navigation.ls():

    if element.is_dir():
        print(f"📁 {element.name}")

    else:
        print(f"📄 {element.name}")