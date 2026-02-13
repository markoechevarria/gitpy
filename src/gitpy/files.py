import os
from pathlib import Path
import shutil
from utils import Utils
from color import Color

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
            open( Path('.gitpy', 'HEAD'), 'w').close()
            with open( Path('.gitpyignore'), 'w') as file:
                file.write(".gitignore\n.git/\n.gitpyignore\n.gitpy/")
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

    def add_files(self):
        """Add files to the stage area"""

        try:
            ignore_files = Utils.list_gitpyignore()
            target_files = os.listdir()

            for target in target_files:
                if target in ignore_files:
                    continue

                if not os.path.isfile( Path(target) ):
                    continue

                hast_object = Utils.create_hash_object(target)

                if not hast_object:
                    continue
                    
                sha_code, file_with_header = hast_object
                file_blob = Utils.create_blob_object( file_with_header )

                print(f"{Color.GREEN}{"Stagging":^10} {target:^20} {sha_code:^20}{Color.END}")

        except Exception as e:
            print( "Ocur a problem trying to add files")


    def list_files(self):
        list_directories = os.listdir( os.getcwd() )
        for entry in list_directories:
            print(entry)


    def stage_files(self):
        pass
