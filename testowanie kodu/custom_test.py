import pytest
import os


@pytest.mark.skipif(os.environ.get("NO_SUMMING") == "1", reason="NO_SUMMING SET ON 1")
def test_sum():
    assert 2 + 2 == 4

@pytest.mark.xfail
def test_get_element_from_lista():
    lista = ["object"]
    assert lista[0] == "fail"

