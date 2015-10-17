import sys
sys.path.append("../src")

import pytest

pytest.main("-l test" + " ".join(sys.argv[1:]))
