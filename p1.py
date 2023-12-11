from pathlib import Path
from collections import namedtuple
import argparse
import logging

logging.basicConfig(filename='log.log',filemode="a", level=logging.NOTSET, format='[{levelname}] {asctime}: {msg}',
                    style='{')
LOGGER = logging.getLogger(__name__)

parser1 = argparse.ArgumentParser()
parser1.add_argument("dir_path",metavar="P")
args = parser1.parse_args()
p = Path(args.dir_path)
res = []
dir_path = namedtuple("dir_path",["file_name","file_extension","dir_or_file","parent_name"])


for obj in p.iterdir():
    res.append(dir_path(obj.name,obj.suffix.strip("."),"dir" if obj.is_dir() else "file",obj.parent.name))
    logging.info(f"{res[-1]} was added")

print(res)
