import pytest

from solution import lexographical_min

test_01 = ("eggegg", "egg")

test_2 = ("aaaabbbbccccccbbbbccaaaa", "aaaabbbbcccc")

test_03 = (
    """sbcnzxqnrygkocahxjebvueaawwcythjdrhvizqsshgtwdolmillxpshxpxqrywkivceufclhydhshrklkphajbftuapiocjlcthfirhgaohfysqjolssbzhbovdstbyqdpnjbpfmgqrzfctcwcrztvgbegunarvecseoulabaonguckqbtrvuagreyclyjytpvozqdnhldlnsocenuzksawirgsbjobpldjdlrxbricrauuksbmecvvwagnnacaqghmjpzrlsvlpbbcuaddgvlhvuvkxexjcfhxrodmcwlrzyyiksuksshhonahsyzbbprwuitmoyoqurtqsaslevgvpfbzkkhgcnpjdpseuiylluvdetsqssbrxpiclxxvosuqipsqvvwsezhl""",
    """aaaaaavvcembskuabxddlpbbsgiaskucosdlhndqzovpjlcyerauvrbcugnbluescevrnubgvtzrcwccfzrqgmfpbjnpdqybtsdvobhzsslojqsyfhoghrifhtclcoiputjhpklkrhsdyhlcuevikwyrqxpxhspxllimlowtghssqzivhrjtywweuvejxokgyrnqxzns"""
)
test_4 = ("zzaabbezzzzzzebbbbaabb", "aabbbbezzzz")

test_5 = ("bbbbbccccjcjjjjjcbbb", "bbbcjjcjcb")

test_08 = ("""zzzzaaaaxxffbbzzffaaxx""", """aabffxxazzz""")


@pytest.mark.parametrize(
    "merged, original",
    [("ccbbaa", "abc"), test_01, test_2, test_03, test_4, test_5, test_08])
def test_lexographical_min(merged, original):
    assert lexographical_min(merged) == original
