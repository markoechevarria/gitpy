import click 

class Reader(): 

    def __init__(self):
        pass

    def info(self):
        click.echo("Reader class working")

    @click.option('--count', default=1, help='gaa')
    def hello(self, count):
        if not count : return ;

        print("ga" + count)

