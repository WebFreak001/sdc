#!/usr/bin/env python3

import os
llvmconfig = os.getenv('LLVM_CONFIG', 'llvm-config')

import subprocess
import sys

# Make sure we can find the lit package.
llvm_source_root = subprocess.check_output([llvmconfig, "--src-root"]).decode('utf-8').strip()
sys.path.insert(0, os.path.join(llvm_source_root, 'utils', 'lit'))

# src-root mayb be bogous with some packaging of LLVM, so we use obj-root as a fallback.
llvm_obj_root = subprocess.check_output([llvmconfig, "--obj-root"]).decode('utf-8').strip()
sys.path.insert(0, os.path.join(llvm_obj_root, 'build', 'utils', 'lit'))

if __name__=='__main__':
    from lit.main import main
    main()
