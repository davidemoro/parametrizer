# -*- coding: utf-8 -*-


def test_parametrizer():
    """ Test parametrizer """
    from parametrizer import Parametrizer
    assert Parametrizer({'foo': 'bar'}).parametrize('$foo') == 'bar'
