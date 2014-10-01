from unittest import TestCase
from BoxContentApiAdapter import BoxContentApiAdapter
__author__ = 'bcao'


class TestBoxContentApiAdapter(TestCase):

    def test_authorize1(self):
        o = BoxContentApiAdapter
        res = o.authorize('glacierwn','Xiaoziyu33')
