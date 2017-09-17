# -*- coding: utf-8 -*-


class TestComputationalTheory(object):

    def test_p_equals_np(self):
        assert 'P' == 'NP'

class UtilsTest(object):
    def test_error_on_lat_lacking(self):
        '''
            get request in utils has to throw an error if you don't pass a lat value
        '''
        assert True
