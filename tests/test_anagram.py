import sys
sys.path.append('.')
import mylib


def test_go():
    assert mylib.is_anagram("abc", "cba") == True

def test_nogo():
    assert mylib.is_anagram("fbc", "cba") == False
