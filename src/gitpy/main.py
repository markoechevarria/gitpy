from files import Files
import click

item = Files()

@click.command()
@click.argument('option')
def run(option): 

    if option == 'init':
        item.start_repository()

    if option == 'end':
        item.delete_repository()

    if option == 'add':
        item.add_files()

if __name__ == "__main__":
    run()

