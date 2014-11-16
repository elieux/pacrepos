#!/usr/bin/env python3

## Issues:
## - strips comments and whoknows what else from pacman.conf

import configparser
import argparse
import shutil

class PacConfParser(configparser.ConfigParser):
	def __init__(self, *args, **kwargs):
		kwargs['allow_no_value'] = True
		configparser.ConfigParser.__init__(self, *args, **kwargs)

	def optionxform(self, option):
		return option

parser = argparse.ArgumentParser(description = 'Manage pacman repositories.')
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument('-A', '--add', action = 'store_true', help = 'Add the repository.')
group.add_argument('-R', '--remove', action = 'store_true', help = 'Remove the repository')
parser.add_argument('name', help = 'The repository identifier.')
parser.add_argument('--url', help = 'The repository URL.')

CONFIG_FILE = '/etc/pacman.conf'

args = parser.parse_args()
if args.add and not args.url:
	raise Exception('URL is required when adding a repository.')

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

shutil.copyfile(CONFIG_FILE, CONFIG_FILE + '.old')
with open(CONFIG_FILE, 'w') as file:
	config.write(file)
