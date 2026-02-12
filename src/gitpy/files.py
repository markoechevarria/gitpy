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
        """Creating .gitpy directorie, other directories and files"""

        if os.path.exists( Path( os.getcwd(), '.gitpy')):
            print(f"{Color.YELLOW}Here already exists a respository{Color.END}")
            return  

        try: 
            print(f"{Color.GREEN}Initalizing repository...{Color.END}")
            os.mkdir( '.gitpy')
            os.mkdir( Path('.gitpy', 'objects') )
            os.mkdir( Path('.gitpy', 'refs') )
            open( Path('.gitpyignore'), 'w').close()
            open( Path('.gitpy', 'HEAD'), 'w').close()
            print(f"{Color.GREEN}Repository initalized{Color.END}")
        except Exception as e:
            print('Error trying to start the repository', e)

    def delete_repository(self):
        """ Delete .gitpy directorie and .gitpyignore file"""

        if not os.path.exists( Path( os.getcwd(), '.gitpy')):
            print(f"{Color.YELLOW}Here doesn't exist a respository{Color.END}")
            return 

        try:
            os.remove('.gitpyignore')
            shutil.rmtree( Path(os.getcwd(), '.gitpy') )
            print(f"{Color.GREEN}Repository deleted{Color.END}")
        except Exception as e:
            print('Error trying to delete repository', e)

    def list_files(self):
        list_directories = os.listdir( os.getcwd() )
        for entry in list_directories:
            print(entry)


    def stage_files(self):
        pass


