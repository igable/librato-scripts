Author: Ian Gable <igable@uvic.ca>

## librato-imap

A python script that will watch an imap server, get the number of unread
messages and push that information to [Librato Metrics](http://librato.com/).
In order to use this script you need a Librato account and API key.

### Usage


    $ librato-imap --help
    $ librato-imap --username joe --imap-server imap.domain.com --librato-user "joe@domain.com" --api-key 1234561234sdf5345


### Installation

The install requires the python librato package from PyPI. You can install this with pip. If you don't have pip install that first.

Basic steps:

    $ pip install librato
    $ git clone git://github.com/igable/librato-scripts.git
    $ cd librato-scripts
    $ python setup.py install
 
Hopefully this will get better.

## License

This program is free software; you can redistribute it and/or modify
it under the terms of either:

a) the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any
later version, or

b) the Apache v2 License.
