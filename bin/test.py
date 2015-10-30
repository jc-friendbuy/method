import sys
sys.path.append("../method")

import pytest

pytest.main("-l test" + " ".join(sys.argv[1:]))
