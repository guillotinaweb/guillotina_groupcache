import pytest


@pytest.fixture(scope='session')
def groupcache():
    from guillotina_groupcache import includeme
    includeme(None, {
        'groupcache': {
            'addr': "127.0.0.1:9000"
        }
    })
