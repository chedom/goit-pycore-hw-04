import sys
from pathlib import Path
from colorama import Fore 

# virtual environment is created for the whole repo

def print_folder_content(path: Path, identation = 0):
    name = path.name
    identation_str = " " * identation # to build visual hierarchy

    if not path.is_dir(): # stop recursion, it's file
        print(f"{Fore.GREEN}{identation_str}{name}")
        return

    print(f"{Fore.BLUE}{identation_str}{name}/")

    for child_path in path.iterdir():
        print_folder_content(child_path, identation+1)

def main():
    if len(sys.argv) <= 1:
        print("Path to directory must be specified !")
        return

    dir_to_print = sys.argv[1]
    path = Path(dir_to_print)

    if not path.exists():
        print(f"{path} doesnt exist !")
        return

    if not path.is_dir():
        print(f"{path} is not a directory !")
        return

    print_folder_content(path)


if __name__ == "__main__":
    main()
