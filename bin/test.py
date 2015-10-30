import sys
sys.path.append("../")

import pytest

pytest.main("-l test " + " ".join(sys.argv[1:]))
