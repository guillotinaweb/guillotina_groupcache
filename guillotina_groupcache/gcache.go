package main

import (
  "github.com/golang/groupcache"
  "net/http"
  "log"
  "errors"
)

import "C"

// temporary storage to be able to set data
var Store = map[string]string{}

var peers *groupcache.HTTPPool = nil
var cache *groupcache.Group = nil
var srv *http.Server = nil


//export cache_set
func cache_set(key *C.char, value *C.char) *C.char {
  // groupcache does not have a way to set a value in the cache(pass through cache)
  // so we fake it by setting value in global store and then getting the value immediately..
  var gkey = C.GoString(key)
  var gvalue = C.GoString(value)
  Store[gkey] = gvalue;
  var data = ""
  cache.Get(nil, gkey, groupcache.StringSink(&data))
  delete(Store, gkey)
  return C.CString(data)
}


//export cache_get
func cache_get(key *C.char) *C.char {
  var data = ""
  cache.Get(nil, C.GoString(key), groupcache.StringSink(&data))
  return C.CString(data)
}

//export setup
func setup(addr *C.char) {

  go func() {
    peers = groupcache.NewHTTPPool(C.GoString(addr))
    cache = groupcache.NewGroup("Cache", 64<<20, groupcache.GetterFunc(
    	func(ctx groupcache.Context, key string, dest groupcache.Sink) error {
        v, ok := Store[key]
    		if !ok {
    			return errors.New("cache key not found")
    		}
        dest.SetBytes([]byte(v))
    		return nil
    	}))

    srv := &http.Server{Addr: C.GoString(addr), Handler: http.HandlerFunc(peers.ServeHTTP)}

    if err := srv.ListenAndServe(); err != nil {
      log.Fatal("ListenAndServe: ", err)
  	}
  }()
  // do it in a go routine so we don't block
  log.Print("Running cache server node\n")
}

//export initialized
func initialized() bool {
  return cache != nil
}

func main() {}
