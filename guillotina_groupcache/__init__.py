from guillotina import configure
from guillotina_groupcache import cache


app_settings = {
    "groupcache": {
        "addr": "127.0.0.1:9000"
    }
}


def includeme(root, settings):
    cache.setup(settings.get('groupcache', {}).get('addr', app_settings['groupcache']['addr']))
    configure.scan('guillotina_groupcache.cache_strategy')
