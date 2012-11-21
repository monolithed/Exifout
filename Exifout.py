# -*- coding: utf-8; indent-tabs-mode: nil; tab-width: 4; c-basic-offset: 4; -*-

'''
- Exifout - A simple wrapper around the PNGOUT library
-
- Exifout  --path | [ --files ] | [ --name ] | [ --options ] | [--extensions ] | [platform] | [ machine ] | [ pngout ]
-
- @author Alexander Abashkin <monolithed@gmail.com>
- @version 0.0.3
- @license: MIT
- @date: Mon 12 04:33:00 2012
'''

import os
import itertools
from subprocess import call
from datetime import datetime
from re import sub as replace
from configure import parser

__all__ = ['Exifout']


class Exifout:
	def __init__(self, options):
		self.options = options
		self.count = itertools.count()
		self.router()


	def get_binary_file(self):
		'''
		This method provides a way to find the PNGOUT binary file
		'''
		file = '%spngout/pngout-20120530-%s' % (self.options.pngout[0], self.options.platform.lower())

		try:
			machine = [i for i in os.listdir(file) if ~i.find(self.options.machine[0])]

			if file.endswith('darwin'):
				file = '%s/pngout' % file

			elif machine:
				file = '%s/%s/pngout' % (file, machine[0])

			else:
				self.LOG_INFO('fail', 'The machine type could not be determined automatically!')
				return 0

		except OSError, error:
			self.LOG_INFO('fail', error)

		else:
			return file


	def set_file_postfix(self, file, extension):
		'''
		Set the filename postfix
		'''
		postfix = self.options.name[0]

		return postfix and replace('.%s$' % extension, '%s.%s' % (postfix, extension), file)


	def get_options(self):
		return ' '.join('-' + option for option in self.options.options if option)


	def execute(self, file, extension):
		'''
		Execute shell command
		'''
		binary  = self.get_binary_file()

		if binary:
			command = ' '.join([binary, self.get_options(), file, self.set_file_postfix(file, extension)])

			self.LOG_INFO('ok', '[ %s ]' % next(self.count))
			call(command, shell = True)


	def router(self):
		'''
		Finds files
		'''
		get_path, check_path = itertools.tee(os.walk(self.options.path[0]))

		if not sum(1 for _ in check_path):
			self.LOG_INFO('fail', 'Directory invalid or specified files not found!')

		for root, dirs, files in get_path:
			for name in files:
				image = os.path.join(root, name)

				for extension in self.options.extensions:
					if image.endswith('.%s' % extension):
						if self.options.files:
							for file in self.options.files:
								if '%s' % file == name:
									self.execute(image, extension)
						else:
							self.execute(image, extension)


	def LOG_INFO(self, name, text = None):
		'''
		Output stream
		'''
		print(text and '{0}{1}m{2}{0}0m'.format('\033[', {'fail' : 91, 'ok': 92}[name], text) or name)

if __name__ == '__main__':
	name = '{:^63}\n'.format('Exifout')
	info = '{0}\nAlexander Guinness, <monolithed@gmail.com>, 2012\n{0}\n'.format('-' * 63)

	print(name + info)
	Exifout(parser.parse_args())
	print('\nThe last updated: {:%Y-%m-%d %H:%M:%S}'.format(datetime.today()))
