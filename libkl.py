from tqdm import *
from time import *
import os.path
import sys
import importlib

def progbar(list: tuple, wait: int, **kwargs) -> None:
     for i in tqdm(list, **kwargs):
          sleep(wait)

def modload(modf: str) -> None:
    if os.path.isfile(f"mod\\{modf.lower()}.pyw"):
            modspec = importlib.util.spec_from_file_location("mod", f"mod\\{modf.lower()}.pyw")
            mod = importlib.util.module_from_spec(modspec)
            sys.modules["mod"] = mod
            modspec.loader.exec_module(mod)
            mod.run()
    else:
        print(f"Error! Mod file \"{modf}.pyw\" not found!")

def cls() -> None:
    os.system("cls" if os.name == "nt" else "clear")
