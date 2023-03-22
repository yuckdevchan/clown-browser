# Ringmaster - file that interprets command line arguments
import argparse
from puppets.reset import reset_app

def cli_args(program_name, program_desc):
  parser = argparse.ArgumentParser(
    prog=program_name,
    description=program_desc)
  arg_group = parser.add_mutually_exclusive_group()
  # Inputs that specify a value
  arg_group.add_argument('-i', '--input', metavar="", help="Specify and input URL or URI")
  arg_group.add_argument('-c', '--cache', metavar="", help="Specify and cache folder")
  # Inputs that are on/off flags
  arg_group.add_argument('-r', '--reset', action="store_true", help="Reset Clown Browser")
  arg_group.add_argument('-q', '--quiet', action="store_true", help="Make output less verbose")
  arg_group.add_argument('-v', '--verbose', action="store_true", help="Make output more verbose")
  arg_group.add_argument('-r', '--reset', action="store_true", help="Reset Clown Browser")
  
  args = parser.parse_args()
  
  if args.reset:
    reset_app()
  else:
    pass
  