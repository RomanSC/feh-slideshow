""" feh-slideshow.py | Sun, Mar 20, 2017 | Roman S. Collins

    A slideshow program written in Python that changes
    the desktop background using feh

    Only tested on i3 window manager.

    How to use:

    python feh-slideshow.py -d ~/Pictures/cubes/ -t 0.5

    Options:
    -d directory
    -t time (in approximately seconds)

    Dependencies:
    - feh

"""
import sys, os, time

def decodeargs(args):
    if ("-d" not in args) and ("--directory" not in args):
        print("MissingDirectoryError: Please at least specify a slideshow directory.")
        exit()

    for x in range(len(args)):

        if ("-d" in args[x]) or ("--directory" in args[x]):
            slide_dir = args[x+1] # arg after -d or --directory is the slideshow path

        if ("-t" in args[x]) or ("--time" in args[x]): # Check for -t argument
            try:
                sec = int(args[x+1])
            except ValueError:
                sec = float(args[x+1])

    # If no time is provided default to 5
    try:
        return slide_dir, sec
    except NameError:
        return slide_dir, 5

def readdir(slide_dir):
    # TODO:
    # Support all filetypes that feh supports
    filetypes = [".png", ".jpeg", ".jpg"]

    # TODO:
    # Read only files...
    # onlyfiles = [f for f in os.listdir(slide_dir) if os.isfile(os.join(slide_dir, f))]

    # Make sure slide_dir ends in "/" preventing an error when full path is created
    if slide_dir[-1:] != "/":
        slide_dir = slide_dir + "/"

    files = os.listdir(slide_dir) # Read in files

    for f in range(len(files)):
        files[f] = str(slide_dir) + files[f] # Make full path for feh

    # Sort files by integer
    # https://stackoverflow.com/questions/4287209/sort-list-of-strings-by-integer-suffix-in-python
    for ft in filetypes:
        try:
            files = sorted(files, key = lambda x: int((x.split(ft)[0]).split("_")[1]))
        except ValueError:
            pass

    # Alternately sort alphabetically also works too
    # files.sort()

    return files

def slideshow(files, sec):
    while True:
        for f in files:
            os.system("feh --bg-scale {}".format(f))
            time.sleep(sec)

def main(args):
    slide_dir, sec = decodeargs(args)
    files = readdir(slide_dir)
    slideshow(files, sec)

if __name__ == "__main__":
    args = sys.argv
    main(args)
