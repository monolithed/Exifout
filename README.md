# Exifout

Exifout - A simple wrapper around the PNGOUT library

## Synopsis

```
Exifout  --path | [ --files ] | [ --name ] | [ --options ] | [--extensions ] | [platform] | [ machine ] | [ pngout ]
```

## Dependencies

PNGOUT binary files that are located in pngout directory

## Installation

```
git clone git@github.com:monolithed/Exifout.git

```

## Using

```bash
python ../Exifout.py --path ../test --options s4 c0 --extensions png --pngout ../
```

*NOTE*
All files are searched recursively!

## Supported platforms

```
BSD: Athlon
BSD: i386
BSD: i686
BSD: Pentiun 4

Linux: Athlon
Linux: i386
Linux: i686
Linux: x86-64
Linux: Pentiun 4

Darvin
```

## Links

[PNGOUT Tutorial] (http://advsys.net/ken/util/pngout.htm) <br />
[Linux/BSD/Mac OS X ports of Ken Silverman's Utilities] (http://www.jonof.id.au/kenutils) <br />
[Ken Silverman's Utility Page] (http://advsys.net/ken/utils.htm)


##.

* Exifout library is licensed under the MIT (MIT_LICENSE.txt) license

* Copyright (c) 2012 [Alexander Guinness] (https://github.com/monolithed)
