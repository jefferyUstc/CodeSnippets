# -*- coding:utf-8 _*-  
""" 
@author:jeffery
@time: 2019/04/29 10:30
@contact: jeffery_cpu@163.com
"""

from types import FunctionType
import six


def activation1():
    print('i am activation 1')


def activation2():
    print('i am activation 2')


def serialize(activation):
    return activation.__name__


def deserialize(name, custom_objects=None):
    return deserialize_object(
        name,
        module_objects=globals(),
        custom_objects=custom_objects,
        printable_module_name='activation function')


def get(identifier):
    """Get the `identifier` activation function.

    # Arguments
        identifier: None or str, name of the function.

    # Returns
        The activation function, `activation1` if `identifier` is None.

    # Raises
        ValueError if unknown identifier
    """
    if identifier is None:
        return activation1

    if isinstance(identifier, six.string_types):
        identifier = str(identifier)
        return deserialize(identifier, None)

    elif isinstance(identifier, FunctionType):
        return identifier
    else:
        raise ValueError('Could not interpret '
                         'activation function identifier:', identifier)


def deserialize_object(identifier,
                       module_objects=None,
                       custom_objects=None,
                       printable_module_name='object'):
    """
    这个函数可以放到其他模块，以进行功能扩展，使其不但能寻找activations
    :param identifier: str type
    :param module_objects:
    :param custom_objects:
    :param printable_module_name:
    :return:
    """
    if isinstance(identifier, six.string_types):
        function_name = identifier
        if custom_objects and function_name in custom_objects:
            fn = custom_objects.get(function_name)
        else:
            fn = module_objects.get(function_name)
            if fn is None:
                raise ValueError('Unknown ' + printable_module_name +
                                 ':' + function_name)
        return fn

    else:
        raise ValueError('Could not interpret serialized ' +
                         printable_module_name + ': ' + identifier)


if __name__ == '__main__':
    activation = get('activation3')

