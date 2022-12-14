#!/usr/bin/env python3
# vim: ts=2 sts=0 sw=2 tw=120 et

from dotenv import load_dotenv
load_dotenv()

import deebee
from deebee import menu

if __name__ == "__main__":
  deebee.setup()
  menu.menu(deebee.CONNECTION)
  deebee.close()