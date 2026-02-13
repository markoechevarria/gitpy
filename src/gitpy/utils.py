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