from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_report, get_citations_needed_count


def test_version():
    assert __version__ == '0.1.0'

def test_count():
    actual = get_citations_needed_count()
    expected = 5
    assert actual == expected

def test_report():
    actual = get_citations_needed_report()[0]
    expected = 'The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.'
    assert actual == expected