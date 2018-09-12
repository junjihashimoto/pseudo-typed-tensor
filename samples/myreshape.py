"""
>>> 3+3
6

"""

import tensorflow as tf
import random
import typedtensor as tt


def myreshape(x):
    """
    >>> x = tf.zeros([10,56,56,1],name='x')
    >>> myreshape(x)
    <tf.Tensor 're:0' shape=(40, 28, 28, 1) dtype=float32>
    >>> v = myreshape(x)
    >>> tt.shape_eq(v,[40,28,28,1])
    True
    >>> tt.type_eq(v,[40,28,28,1],tf.float32)
    True
    >>> tt.inout_eq(myreshape,\
                    in_shape=[10,56,56,1],in_dtype=tf.float32,\
                    out_shape=[40,28,28,1],out_dtype=tf.float32)
    True
    >>> tt.prop(["int"],lambda n: tt.inout_eq(myreshape,\
                                              in_shape=[n,56,56,1],in_dtype=tf.float32,\
                                              out_shape=[n*4,28,28,1],out_dtype=tf.float32))
    True
    """
    return tf.reshape(x, [-1, 28, 28, 1], name="re")


def dummy():
    return
