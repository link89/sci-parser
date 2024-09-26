import unittest
from pathlib import Path
import re

from sci_parser.parser import Parser
from . import DATA_DIR


class TestParser(unittest.TestCase):
    
    def test_parser(self):
        with open(Path(DATA_DIR) / 'multiwfn-01.txt') as fp:
            text = fp.read()
        parser = Parser()
        (
            parser
                .kv_search('Total/Alpha/Beta electrons', v_type=float)
                .kv_search('Net charge', v_type=float)
                .kv_search('Expected multiplicity', v_type=int)
                .kv_search('Atoms', stop_at=',', v_type=int)
                .kv_search('Basis functions', stop_at=',', v_type=int)
                .kv_search('GTFs', v_type=int)
                .kv_search('Total energy', v_type=float)
                .kv_search('Virial ratio', v_type=float)
        )
        result = list(parser.parse(text))
        print(result)