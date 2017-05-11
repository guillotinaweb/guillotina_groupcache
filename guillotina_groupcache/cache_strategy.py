from guillotina import configure
from guillotina.db.cache.base import BaseCache
from guillotina.db.interfaces import IStorage
from guillotina.db.interfaces import IStorageCache
from guillotina_groupcache import cache

import base64
import json


@configure.adapter(for_=IStorage, provides=IStorageCache, name="groupcache")
class GroupCache(BaseCache):

    def dumps(self, value):
        value = dict(value)
        if isinstance(value['state'], bytes):
            value['state'] = base64.b64encode(value['state']).decode('ascii')
        return json.dumps(value)

    def loads(self, value):
        if isinstance(value, bytes):
            value = value.decode('utf-8')
        value = json.loads(value)
        value['state'] = base64.b64decode(value['state'].encode('ascii'))
        return value

    async def get(self, oid, default=None):
        val = cache.get(oid)
        if val in b'':
            return default
        return self.loads(val)

    async def get_child(self, oid, id, prefix=''):
        key = prefix + oid + '/' + id
        val = cache.get(key)
        if val in b'':
            return None
        return self.loads(val)

    async def set_child(self, oid, id, value, prefix=''):
        key = prefix + oid + '/' + id
        cache.set(key, self.dumps(value))

    async def get_len(self, oid):
        key = oid + '-length'
        val = cache.get(key)
        if val in b'':
            return None
        return int(val)

    async def set_len(self, oid, val):
        key = oid + '-length'
        cache.set(key, str(val))

    async def set(self, ob, value):
        cache.set(ob._p_oid, self.dumps(value))

    async def clear(self):
        pass

    async def invalidate(self):
        pass
