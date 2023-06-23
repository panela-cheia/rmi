import sys
import json

from base.base import Bootstrap
from tests.messages import aux26

#sys.tracebacklimit=0

if __name__ == "__main__":
    base = Bootstrap()

    base.run(json.dumps(aux26))