# feh-slideshow

<iframe src='//gifs.com/embed/feh-slideshow-python-66NPON' frameborder='0' scrolling='no' width='640px' height='360px' style='-webkit-backface-visibility: hidden;-webkit-transform: scale(1);' ></iframe>

A slideshow script written in Python that changes the desktop background using the feh linux program.

### Dependencies

+ feh <br><a href="https://github.com/derf/feh">https://github.com/derf/feh</a></br>

### How to use

Start using two arguments -d for the path to your slideshow folder and -t for approximate time in seconds for the image to update.

Order your files in order. The script will sort them by integer. See example pictures directory. "n_10.png" is sorted as "n 10 ", where "_" and ".png" is split and removed to find the sort order. "n_10.png" is before "n_20.png", for example.

If -t is not used the default value for time is 5.

...turns out feh already supports slideshows, eh.. oh well.

