import os
from pathlib import Path
import shutil

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class Files:

    def __init__(self): 
        self.repository_route = os.getcwd()

    def start_repository(self):
        
        if os.path.exists( Path( os.getcwd(), '.gitpy')):
            print(f"{Color.YELLOW}Here already exists a respository{Color.END}")
            return  

        print(f"{Color.GREEN}Initalizing repository...{Color.END}")

        os.mkdir('.gitpy')
        with open( Path('.gitpy','commit_0'), 'w') as f:
            f.write( "commiting" )

        print(f"{Color.GREEN}Repository initalized{Color.END}")


    def delete_repository(self):

        if not os.path.exists( Path( os.getcwd(), '.gitpy')):
            print(f"{Color.YELLOW}Here doesn't exist a respository{Color.END}")
            return 

        shutil.rmtree( Path(os.getcwd(), '.gitpy') )

        print(f"{Color.GREEN}Repository deleted{Color.END}")


    def list_files(self):
        list_directories = os.listdir( os.getcwd() )
        for entry in list_directories:
            print(entry)


    def stage_files(self):
        pass


