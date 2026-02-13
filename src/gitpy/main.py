from files import Files
import click

item = Files()

@click.command()
@click.argument('option')
@click.argument('suboption', default=None)
def run(option, suboption): 

    if option == 'init':
        if suboption is None:
            item.start_repository()

    if option == 'end':
        if suboption is None:
            item.delete_repository()

    if option == 'add':
        if suboption == '.':
            item.add_files()

if __name__ == "__main__":
    run()

