import unittest
from pathlib import Path
import re

from sci_parser.parser import Parser
from . import DATA_DIR


class TestParser(unittest.TestCase):
    
    def test_parser(self):
        with open(Path(DATA_DIR) / 'multiwfn-01.txt') as fp:
            text = fp.read()
        parser = Parser(fmt_fn=lambda m: m.groups(), flags=re.MULTILINE)

        (
            parser
                .kv_search('Total/Alpha/Beta electrons')
                .kv_search('Net charge')
                .kv_search('Expected multiplicity')
                .kv_search('Atoms')
                .kv_search('Basis functions')
                .kv_search('GTFs')
                .kv_search('Total energy')
                .kv_search('Virial ratio')

        )
        result = list(parser.parse(text))
        print(result)