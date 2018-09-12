# typedtensor

[![Build Status](https://travis-ci.org/junjihashimoto/typedtensor.png?branch=master)](https://travis-ci.org/junjihashimoto/typedtensor)

## Usage

Write a code of checking tensor's type in doctest.

```
import tensorflow as tf
import typedtensor as tt
def test_func(x):
  """
  >>> tt.inout_eq(test_func,\
                  in_shape=[2,2],in_dtype=tf.float32,\
                  out_shape=[2,2],out_dtype=tf.float32)
  True
  """
  ...

```

## Test

Just run below

    tox
