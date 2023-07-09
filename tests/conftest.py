import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from sklearn.model_selection import train_test_split

@pytest.fixture
def sample_input_data():
    return 10
