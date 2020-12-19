import logging
import click
import cij

def run(config_fname: str):
    import cij.core.calculator
    calculator = cij.core.calculator.Calculator(config_fname)
    calculator.write_output()
    
@click.command()
@click.argument("settings_filename", type=click.Path(exists=True))
@click.version_option(version=cij.__version__, prog_name="cij")
@click.option("--debug", default="INFO", type=click.Choice(logging._levelToName.values()), help="Logging level")
def main(settings_filename: str, debug: str):

    logger = logging.getLogger("cij")
    logger.setLevel(debug)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    run(settings_filename)