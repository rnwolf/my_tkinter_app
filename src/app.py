from src.controller.main_controller import MainController
import argparse
import sys
from src import __version__  # Import the version from your package

def main() -> None:
    parser = argparse.ArgumentParser(
        prog='app',  # Optional: Specify the program name
        description='An Tkinter application',
    )

    # Add the version argument
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=f'%(prog)s {__version__}',  # Display version
    )
    # parse the command line arguments and display version information
    args = parser.parse_args()

    # If no arguments are provided, launch the GUI app
    if len(sys.argv) == 1:
        controller = MainController()
        controller.run()

if __name__ == "__main__":
    main()
