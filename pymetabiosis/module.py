from pymetabiosis.bindings import ffi, lib
from pymetabiosis.wrapper import MetabiosisWrapper

def import_module(name):
    module_object = lib.PyImport_ImportModule(name)
    if module_object == ffi.NULL:
        exc = lib.PyErr_Print()
        raise Exception()
    return MetabiosisWrapper(ffi.gc(module_object, lib.Py_DECREF))