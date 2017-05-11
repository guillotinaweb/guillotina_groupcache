from guillotina_groupcache import cache


def test_get_from_cache(groupcache):
    foobar = cache.get('foo').decode('utf-8')
    assert foobar == ''


def test_set_value_in_cache(groupcache):
    cache.set('foo', 'bar')
    bar = cache.get('foo').decode('utf-8')
    assert bar == 'bar'
