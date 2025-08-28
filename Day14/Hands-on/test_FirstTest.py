from FirstTest import FindEvenNumber

def test_FindEvenNumber():
    assert FindEvenNumber(10) == "Even"
    assert FindEvenNumber(13) == "Odd"
    assert FindEvenNumber(0) == "Even"
    assert FindEvenNumber(11) == "Even"

