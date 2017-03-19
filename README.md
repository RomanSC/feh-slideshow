# feh-slideshow

A slideshow script written in Python that changes the desktop background using the feh linux program.

### Dependencies

+ feh

### How to use

Start using two arguments -d for the path to your slideshow folder and -t for approximate time in seconds for the image to update.

Order your files in order. The script will sort them by integer. See example pictures directory. "n_10.png" is sorted as "n 10 ", where "_" and ".png" is split and removed to find the sort order. "n_10.png" is before "n_20.png", for example.

If -t is not used the default value for time is 5.

