import sys
import os
import json
from tqdm import tqdm
import make_json as mj

output_dir = sys.argv[1]
for fname in sys.argv[2:]:
    print(fname)
    mj.make_json_from_conllu(fname, output_dir)
