from pymetabiosis.module import import_module
from pymetabiosis.wrapper import MetabiosisWrapper, cpy_to_pypy_converters


def register_cpy_numpy_to_pypy_builtin_converters():
    ''' Converts numpy types to builtin python types on PyPy side
    '''
    numpy = import_module("numpy")
    builtin = import_module("__builtin__", noconvert=True)
    def call_direct(f):
        f = MetabiosisWrapper(f.obj, noconvert=False)
        return lambda x: f._call((x,), args_kwargs_converted=True)

    cpy_to_pypy_converters.update({
        numpy.bool_.obj: call_direct(builtin.bool),
        numpy.int8.obj: call_direct(builtin.int),
        numpy.int16.obj: call_direct(builtin.int),
        numpy.int32.obj: call_direct(builtin.int),
        numpy.int64.obj: call_direct(builtin.int),
        numpy.float16.obj: call_direct(builtin.float),
        numpy.float32.obj: call_direct(builtin.float),
        numpy.float64.obj: call_direct(builtin.float),
    })

    if hasattr(numpy, "float128"):
        cpy_to_pypy_converters.update({numpy.float128.obj: call_direct(builtin.float)})
