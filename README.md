# THUMBTACK

A example of getting a questions and answers from thumbtack.com.

  - Takes all URLs to thumbtack works
  - Returns all questions + answers

# Uses:

  - Python3 selenium web driver
  - Multiprocessing module
  - Approximately 1 gigabyte of RAM

# Returns:
  - result.txt with the results of data parsing

# Installation

Requires [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). But for Windows it is present!

Install dependencies and starting the parser.

```sh
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

# Good luck!