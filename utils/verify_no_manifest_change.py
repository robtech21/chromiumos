#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Verify no changes are made to full.xml."""

from __future__ import print_function

import argparse
from pathlib import Path
import sys


assert sys.version_info >= (3, 6), 'This module requires Python 3.6+'


def main(argv):
  """Main function."""
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('PRESUBMIT_FILES', nargs='*', type=Path)
  opts = parser.parse_args(argv)

  external_full = 'full.xml'

  if external_full in {x.name for x in opts.PRESUBMIT_FILES}:
    print('You should not update full.xml in this repo. This repo '
          'automatically syncs with the internal repo '
          '(manifest-internal/full.xml). Please only make changes in the '
          'internal repo.')
    sys.exit(1)


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
