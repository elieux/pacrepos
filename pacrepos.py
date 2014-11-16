#!/usr/bin/env python3

import configparser
import argparse
import shutil

class PacConfParser(configparser.ConfigParser):
	def optionxform(self, option):
		return option

parser = argparse.ArgumentParser(description = 'Manage pacman repositories.')
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument('-I', '--install', action = 'store_true', help = 'install into pacman.conf')
group.add_argument('-A', '--add', action = 'store_true', help = 'add the repository NAME with URL')
group.add_argument('-R', '--remove', action = 'store_true', help = 'remove the repository NAME')
parser.add_argument('--name', help = 'the repository identifier')
parser.add_argument('--url', help = 'the repository server')

PACMAN_FILE = '/etc/pacman.conf'
CONFIG_FILE = '/etc/pacrepos.conf'

args = parser.parse_args()
if args.add and not args.url:
	raise Exception('URL is required when adding a repository.')
if args.add and not args.name:
	raise Exception('Name is required when adding a repository.')
if args.remove and not args.name:
	raise Exception('Name is required when removing a repository.')

if args.install:
	shutil.copyfile(PACMAN_FILE, '{0}.old'.format(PACMAN_FILE))
	with open(PACMAN_FILE, 'a') as file:
		file.write('\n')
		file.write('Include = {0}\n'.format(CONFIG_FILE))
	with open(CONFIG_FILE, 'a+'):
		pass # just create the file
else:
	config = PacConfParser()
	config.read(CONFIG_FILE)

	if args.add and args.name in config:
		raise Exception("Repository '{0}' is already present.".format(args.name))

	if args.remove and args.name not in config:
		raise Exception("Repository '{0}' is not present.".format(args.name))

	if args.add:
		config[args.name] = { 'Server': args.url, 'SigLevel': 'Optional' }

	if args.remove:
		del config[args.name]

	with open(CONFIG_FILE, 'w') as file:
		config.write(file)
