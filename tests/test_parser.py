import unittest
from pathlib import Path
from pprint import pprint

from sci_parser.parser import Parser
from . import DATA_DIR


class TestParser(unittest.TestCase):


    def test_parser(self):

        with open(Path(DATA_DIR) / 'multiwfn-01.txt') as fp:
            text = fp.read()
            parser = (
                Parser()
                .kv_search('Total/Alpha/Beta electrons', v_type=float)
                .kv_search('Net charge', v_type=float)
                .kv_search('Expected multiplicity', v_type=int)
                .kv_search('Atoms', stop_at=',', v_type=int)
                .kv_search('Basis functions', stop_at=',', v_type=int)
                .kv_search('GTFs', v_type=int)
                .kv_search('Total energy', v_type=float)
                .kv_search('Virial ratio', v_type=float)
                .kv_search('Formula')
                .kv_search('Total atoms', v_type=int)
                .kv_search('Molecule weight', v_type=float)
                .kv_search('Atom list', multiline=True, stop_at='Note')
                .kv_search('Molecular planarity parameter (MPP)', value=r'(.*)$', sep='is')
            )
        result = list(parser.parses(text))
        pprint(result)