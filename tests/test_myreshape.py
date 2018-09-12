import sys
sys.path.append("samples")

import typedtensor as tt
import myreshape
import pytest

import inspect
import re

def test_verify_package():
  ignored_functions = [
    "dummy"
  ]
  assert tt.verify_package(myreshape,ignored_functions) == True
