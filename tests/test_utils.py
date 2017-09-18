# -*- coding: utf-8 -*-
 
from server.utils import get_distance_m, contains_tags

class TestUtils(object):

    def test_contains_tags(self):
        test_data = list(
            {'container': set('home', 'bath'), 'tags': ['foo', 'bar'], 'result': False},
            {'container': set('home', 'bath'), 'tags': ['home'], 'result': True},
            {'container': set('home', 'bath'), 'tags': ['home', 'bath'], 'result': True},
            {'container': set('home', 'bath'), 'tags': None, 'result': True},
            {'container': set('home', 'bath'), 'tags': [], 'result': True},
        )
        for test in test_data:
            assert contains_tags(test['tags'], test['container']) == test['result']
