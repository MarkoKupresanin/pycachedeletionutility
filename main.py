import os
import re
from pathlib import Path


def iterativeDelete(path, extensive):
    numPycacheDeleted = 0
    directories = []
    for i in path.iterdir():
        if i.is_dir():
            directories.append(i)

    if extensive == True:
        for generalPath in directories:
            for specificPosixPath in generalPath.iterdir():
                if (specificPosixPath.name == "__pycache__"):
                    try:
                        Path.rmdir(Path(specificPosixPath))
                        numPycacheDeleted += 1
                    except OSError as o:
                        if int(o.errno) == int(39):
                            for item in specificPosixPath.iterdir():
                                item.unlink()
                            Path.rmdir(Path(specificPosixPath))
                        else:
                            print(o)
                    print(f"Removing pycache folder from {specificPosixPath}")    
    else:
        for item in directories:
            if item.name == "__pycache__":
                try:
                    Path.rmdir(Path(item))
                    numPycacheDeleted += 1
                except OSError as o:
                    if int(o.errno) == int(39):
                        for stuff in item.iterdir():
                            stuff.unlink()
                        Path.rmdir(Path(item))
                    else:
                        print(o)
                print(f"Removing pycache folder from {item}")
    return numPycacheDeleted

def main():
    userPath = input("Enter full path to delete pycache files [Default cwd] ")
    extensive = True

    if userPath == "":
        userPath = Path(os.getcwd())
    else:
        userPath = Path(userPath)

    goWithinFolders = input("Do you want to search inner folders to remove pycache? [Y/n] ")
    if goWithinFolders == "":
        extensive = True
    elif goWithinFolders.lower() == "y" or goWithinFolders.lower() == "yes":
        extensive = True
    elif goWithinFolders.lower() == "n" or goWithinFolders.lower() == "no":
        extensive = False
    else:
        print("Input not recognized")


    deleted = iterativeDelete(userPath, extensive)
    if deleted > 0:
        print(f"{deleted} pycache folder(s) deleted")
    else:
        print("0 pycache folders were found to delete, if this is not what you expected, try double-checking the path you entered")

if __name__ == "__main__":
    main()