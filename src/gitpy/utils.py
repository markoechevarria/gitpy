import os
from pathlib import Path
import hashlib
import zlib

class Utils:

    @staticmethod
    def list_gitpyignore() -> list[str]:
        """Retrive files and directories in the current paht"""

        try:
            with open( Path('.gitpyignore'), 'r') as file:
                files = [ file.strip() for file in file.readlines() ]

            return files
        
        except Exception as e:
            print( "Doesnt exists the .gitpyignore file")
            return []

    @staticmethod
    def create_hash_object(file: str) -> tuple[ str, str ] | None:
        """ Add a header to the file, creat a sha-1 code and converto to a blob object"""
        try:
            with open( Path(file), 'r') as f:
                file_read = f.read()
                size = os.path.getsize(file)

            file_with_header = f"blob {size}\0\n" + file_read
            encoded_file = file_with_header.encode('utf-8')
            sha1_hash = hashlib.sha1()

            sha1_hash.update(encoded_file)
            return ( sha1_hash.hexdigest(), file_with_header )

        except Exception as e:
            print("Error trying to get the sha-1 code for the file", e)

    @staticmethod
    def create_blob_object(file_content: str) -> bytes | None :
        """ Create the blob object """

        try:
            data = file_content.encode('utf-8')
            compressed_date = zlib.compress( data )
            return compressed_date

        except Exception as e:
            print("Error trying to convert the file content to a blob object")
        
    @staticmethod
    def insert_blob( root_path: str, sha_code: str, blob_file: bytes ):
        """ Create the blob file with path in .gitpy/objetcts/ """ 

        try:
            folder_name = sha_code[:2]
            file_name = sha_code[2:]
            route = Path(root_path, '.gitpy', 'objects', folder_name )
            os.mkdir( route )
            with open( Path( route, file_name ), 'wb' ) as file:
                file.write(blob_file)
 
        except Exception as e:
            print("Error trying to create the blobl object in the path")

    @staticmethod
    def insert_row_to_index( root_path: str, sha_code: str, file_path: str ):
        
        try:
            code_type_file = 100644
            stage_number = 0

            row = f"{code_type_file} {sha_code} {stage_number} {file_path}"

            with open( Path(root_path, '.gitpy', 'index'), 'a') as f:
                f.write(row + '\n')

        except Exception as e:
            print("Error trying to insert the row to the .git/index ")

    @staticmethod
    def insert_branch_to_head( root_path: str, branch_name: str):

        try:
            with open( Path(root_path, '.gitpy', 'HEAD'), 'w') as f:
                f.write(f"ref: refs/heads/{branch_name}")
            
        except Exception as e:
            print("Error trying to define the branch name")

    @staticmethod
    def create_tree_object( blob_list: dict[str, str ]):
        text = ""
        for blob_sha, file_name in blob_list.items():

            text = text + f"blob {blob_sha} {file_name}"


    @staticmethod
    def create_commit_object( tree_hash: str, author: str, message: str):
        content = f"tree {tree_hash}\nauthor {author}\ncommiter {author}\n\n{message}"