#!/usr/bin/env python3
import music_tag
import argparse
from pathlib import Path

def parse_path(path):
    if not path.is_dir():
        dirty = False 
        try:
            f = music_tag.load_file(path)
            if 'album' not in f:
                print(path, "does not have an album name!")
                name = input("Give it a name?")
                if name:
                    f.append_tag('album', name)
                    dirty = True
            if 'artist' not in f:
                print(path, "does not have an artist name!")
                name = input("Give it a name?")
                if name:
                    f.append_tag('artist', name)
                    dirty = True
            if 'artwork' not in f:
                return
                print(path, "does not have artwork!")

            if dirty:
                f.save()
        except:
            pass
            #print(path, "not supported")
    else:
        for subpath in path.glob("*"):
            parse_path(subpath)

def main():
    parser = argparse.ArgumentParser(description="Give a list of files and I'll tell you which ones need tags!")
    parser.add_argument('-r', "--recurse", help="recurse through folders", action="store_const", const=True)
    parser.add_argument('paths', metavar='PATH', type=str, nargs="+")
    args = parser.parse_args()

    for path in args.paths:
        parse_path(Path(path))

if __name__ == "__main__":
    main()
