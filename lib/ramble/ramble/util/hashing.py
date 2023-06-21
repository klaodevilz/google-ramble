# Copyright 2022-2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.

import hashlib
import spack.util.spack_json as sjson


def hash_file(file_path):
    file_hash = None
    with open(file_path, 'rb') as f:
        bytes = f.read()
        file_hash = hashlib.sha256(bytes).hexdigest()
    return file_hash


def hash_string(string):
    return hashlib.sha256(string.encode('UTF-8')).hexdigest()


def hash_json(in_json):
    return hashlib.sha256(sjson.dump(in_json).encode('UTF-8')).hexdigest()
