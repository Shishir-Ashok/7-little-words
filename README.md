# 7-little-words

7 Little Words is a puzzle that is printed on The Economic Times newspaper where a person is required to find
7 words that match the 7 clues given. The number of parentheses er==represent the number of letters in each
solution. Each letter combination can be used only one, but all letter combinations will be necessary to 
complete the puzzle.

Take a clear photo of the puzzle and save it. 
Provide the path to that image file during the execution of this code. See #Examples for better understanding.

Installation
------------

arp-scan uses the standard GNU automake and autoconf tools, so the typical installation process is:

- Run ```$ git clone https://github.com/Shishir-Ashok/7-little-words.git``` to obtain the latest project source code
- Run ```$ cd 7-little-words``` to enter the source directory
- Run ```$ pip install -r requirements.txt``` to install the necessary modules to run the program


Documentation
---------------
```
Usage: arpscan [options]

Options:

  -h, --help  output usage information
  -i, --image [IMAGE]   path to the input image
  -p, --preprocessing [PERPROCESSING] mode of processing the image
  -v, --verbose   verbose mode
  -q, --quiet   Test to see if arp-scan is installed
  -s, --show  Output original and processed image

```

Examples
--------

```
$ python image.py --image img1.png --preprocess blur --verbose --show
```

```
$ python image.py --i /Desktop/images/img1.png --p thresh -q 
```
