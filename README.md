```
888888b.
888   Y88b
888    888
888   d88P  888  888   .d8888b  .d8888b  .d88b.
8888888P"   888  888  d88P"    d88P"    d88""88b
888         888  888  888      888      888  888
888         Y88b 888  Y88b.    Y88b.    Y88..88P
888          "Y88888   "Y8888P  "Y8888P  "Y88P"
                 888
            Y8b d88P
             "Y88P"
```

Pycco is a Python port of Docco: the original quick-and-dirty, hundred-line-
long, literate-programming-style documentation generator. 
This is a modified version that uses dycco 
(from https://github.com/rojalator/dycco for Python files and adds a number
of additional flags.

For more information,
see:

https://rojalator.github.io/pycco/main_py.html

Others:-

CoffeeScript (Original) - http://jashkenas.github.com/docco/

Ruby - http://rtomayko.github.com/rocco/

Sh - http://rtomayko.github.com/shocco/

https://pycco-docs.github.io/pycco/


Installation
============

Use `pip` to install::

    pip install git+https://github.com/rojalator/pycco


Usage
=====

Command Line Usage
------------------

Just pass ``pycco`` a list of files and it will generate documentation for each
of them. By default, the generated documentation is put in a ``docs/``
subdirectory::

    $ pycco my_python_file.py

Dycco can generate docs for multiple files at once::

    $ pycco my_package/*

And you can control the output location::

    $ pycco --directory=/path/to/docs my_package/*

All command line options are given below::

    $ pycco --help

Outputs::


    usage: pycco [-h] [-p] [-d OUTDIR] [-w] [-l LANGUAGE] [-i] [-s] [-a] [--escape-html] [-f] [-u] [sources ...]
    
    positional arguments:
      sources
    
    optional arguments:
      -h, --help            show this help message and exit
      -p, --paths           Preserve path structure of original files
      -d OUTDIR, --directory OUTDIR
                            The output directory that the rendered files should go to.
      -w, --watch           Watch original files and re-generate documentation on changes
      -l LANGUAGE, --force-language LANGUAGE
                            Force the language for the given files
      -i, --generate_index  Generate an index.html document with sitemap content
      -s, --skip-bad-files, -e, --ignore-errors
                            Continue processing after hitting a bad file
      -a, --asciidoc3       Process with asciidoc3 instead of markdown (you will have to install asciidoc3, of course)
      --escape-html         Run the documentation through html.escape() before markdown or asciidoc3
      -f, --single-file     Just produce a .md or .adoc file in single-column to be processed externally
      -u, --underlines      Replace dots in file extension with underscores before adding the html extension (e.g. x.txt becomes x_txt.html)
