import numpy as np


class SaveMixin:
    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')


class DisplayMixin:
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.shape[0]}x{self.shape[1]}):\n{self.data}"


class PropertyMixin:
    @property
    def shape(self):
        return self.data.shape

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.asarray(value)


class Matrix(np.lib.mixins.NDArrayOperatorsMixin, PropertyMixin, SaveMixin, DisplayMixin):
    def __init__(self, data):
        self.data = data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        args = []
        for i in inputs:
            if isinstance(i, Matrix):
                args.append(i.data)
            else:
                args.append(i)

        outputs = kwargs.get('out', None)
        if outputs:
            out_args = []
            for o in outputs:
                if isinstance(o, Matrix):
                    out_args.append(o.data)
                else:
                    out_args.append(o)
            kwargs['out'] = tuple(out_args)

        result = getattr(ufunc, method)(*args, **kwargs)

        if type(result) is tuple:
            return tuple(Matrix(r) if isinstance(r, np.ndarray) else r for r in result)
        elif method == 'at':
            return None
        else:
            return Matrix(result) if isinstance(result, np.ndarray) else result
