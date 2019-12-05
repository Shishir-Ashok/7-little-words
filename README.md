# Words-Verbose

A program that finds words and their meaning using the letters recognized from an image taken by the user. 
Take a clear photo of the letters and save it. 
Provide the path to that image file during the execution of this code. See #Examples for better understanding.

Installation
------------

The installation process is:

- Run ```$ git clone https://github.com/Shishir-Ashok/Words-Verbose.git``` to obtain the latest project source code
- Run ```$ cd Words-Verbose``` to enter the source directory
- Run ```$ pip install -r requirements.txt``` to install the necessary modules to run the program


Documentation
---------------
```
Usage: $ python image.py [options]

Options:

  -h, --help                          output usage information
  -i, --image [IMAGE]                 path to the input image
  -p, --preprocessing [PERPROCESSING] mode of processing the image
  -v, --verbose                       verbose mode
  -q, --quiet                         Test to see if arp-scan is installed
  -s, --show                          Output original and processed image

```

Examples
--------

```
$ python image.py --image img1.png --preprocess blur --verbose --show
```

```
$ python image.py --i /Desktop/images/img1.png -p thresh -q 
```
