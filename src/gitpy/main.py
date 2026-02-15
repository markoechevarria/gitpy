from gitpy.files import Files
import click

item = Files()

@click.command()
@click.argument('option')
@click.argument('suboption', default=None)
def main(option, suboption): 

    match option:
        case "init":
            if suboption is None:
                item.start_repository()
            
        case "end":
            if suboption is None:
                item.delete_repository()

        case "add":
            if suboption == '.':
                item.add_files()
            else:
                click.echo("Files were not specified")

        case _: 
            click.echo("Command unknown. Try again")

if __name__ == "__main__":
    main()