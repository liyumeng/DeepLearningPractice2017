#!/usr/bin/env bash
#
# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#

cd "$(dirname "$0")"
cd fastText

RESULTDIR=result

make

CORPUS=../../${1}
VECTOR_SIZE=${2}
OUTPUT=../../${3}

./fasttext skipgram -input "${CORPUS}" -output "${OUTPUT}" -lr 0.025 -dim $VECTOR_SIZE \
  -ws 5 -epoch 5 -minCount 5 -neg 5 -loss ns -bucket 2000000 \
  -minn 3 -maxn 6 -thread 4 -t 1e-4 -lrUpdateRate 100 -verbose 2


