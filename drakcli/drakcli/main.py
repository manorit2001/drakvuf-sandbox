import click
import logging
import os


@click.command(help='Submit a File for analysis',
               no_args_is_help=True)
@click.argument('file', type=click.Path(exists=True))
@click.option('--background', '-b', 'bg',
              is_flag=True,
              help="Run in background")
def submit(file, bg):
    # api call to /upload
    raise NotImplementedError()


@click.command(help='Get list of analysed files')
def list():
    # api call to /list
    raise NotImplementedError()


@click.command(help='Get status of a run',
               no_args_is_help=True)
def status():
    raise NotImplementedError()


@click.group(help="Get the results")
def get():
    pass


@get.command(help='Get the dumps',
             no_args_is_help=True)
@click.option('--dump_type', type=click.Choice(['memory', 'pcap'], case_sensitive=True), help='Dump to download', required=True)
def dumps(dump_type):
    raise NotImplementedError()


@get.command(help='Get the logs',
             no_args_is_help=True)
def logs():
    raise NotImplementedError()


@click.group()
def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s][%(levelname)s] %(message)s',
        handlers=[logging.StreamHandler()]
    )


main.add_command(submit)
main.add_command(get)
main.add_command(list)
main.add_command(status)

if __name__ == "__main__":
    main()
