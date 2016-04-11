from suds.reader import Reader
from suds.cache import DocumentCache, ObjectCache, FileCache
from suds.options import Options


def clear_suds_cache(wsdl):
    for type in ("wsdl", "document"):
        cacheId = Reader(Options()).mangle(wsdl, type)
        DocumentCache().purge(cacheId)
        ObjectCache().purge(cacheId)
        FileCache().purge(cacheId)
