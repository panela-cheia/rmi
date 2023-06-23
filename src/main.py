import sys
import os

# Obtenha o caminho absoluto do diretório que contém o arquivo main.py
current_dir = os.path.dirname(os.path.abspath(__file__))
#Adicione o diretório acima ao sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import json

from base.base import Bootstrap
from tests.messages import aux5

if __name__ == "__main__":
    base = Bootstrap()

    answer = base.run(json.dumps(aux5))