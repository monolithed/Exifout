import argparse, platform

parser = argparse.ArgumentParser(description = 'Exifout')

parser.add_argument(
	'--files',
	#'-f',
	dest     = 'files',
	nargs    = '+',
	default  =  None,
	help     = 'Specifies which files to use. '
	           'For example: --files image_1.png image_2.png'
)

parser.add_argument(
	'--path',
	#'-p',
	required = True,
	dest     = 'path',
	nargs    = 1,
	help     = 'Set the target directory'
	           'For example: --path ./images/src/etc'
)

parser.add_argument(
	'--name',
	#'-n',
	dest     = 'name',
	nargs    = 1,
	default  =  [''],
	help     = 'Set the filename postfix'
	           'Note, using this option you will have two versions of the files (un/compressed)'
	           'For example: --name _postfix_name'
)

parser.add_argument(
	'--options',
	#'-o',
	dest     = 'options',
	nargs    = '+',
	default  =  [''],
	help     = 'PNGOUT options.'
	           'For example: --options c6 s4 r1'
)

parser.add_argument(
	'--extensions',
	#'-e',
	dest     = 'extensions',
	nargs    = '+',
	default  =  ['png'],
	help     = 'Set file extensions'
	           'For example: --extensions PNG JPG GIF TGA PCX BMP'
)

parser.add_argument(
	'--platform',
	#'-p',
	dest     = 'platform',
	nargs    = 1,
	default  =  platform.system(),
	help     = 'For example: --platform Linux'
)

parser.add_argument(
	'--machine',
	#'-p',
	dest     = 'machine',
	nargs    = 1,
	default  =  platform.machine(),
	help     = 'For example: --machine x86_64'
)

parser.add_argument(
	'--pngout',
	#'-p',
	dest     = 'pngout',
	nargs    = 1,
	default  =  [''],
	help     = 'For example: --pngout ../'
)
