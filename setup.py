#!/usr/bin/env python
import glob
import os.path
import re
from setuptools import Command, find_packages, setup

class PyTest(Command):
	user_options = []
	def initialize_options(self):
		pass
	def finalize_options(self):
		pass
	def run(self):
		import sys, subprocess
		errno = subprocess.call([sys.executable, "runtests.py"])
		raise SystemExit(errno)

def parse_requirements(file_name):
	"""Taken from http://cburgmer.posterous.com/pip-requirementstxt-and-setuppy"""
	requirements = []
	for line in open(
			os.path.join(os.path.dirname(__file__), "config", file_name), "r"):
		line = line.strip()
		# comments and blank lines
		if re.match(r"(^#)|(^$)", line):
			continue
		if line.startswith("git+"):
			parts = line.split('#')
			package = parts.pop().split('=').pop()
			parts = '#'.join(parts).split('@')
			if len(parts) == 3:
				version = parts.pop()
				if version.find('v') > -1:
					version = version.replace('v', '')
				line = "%s==%s" % (package, version)
			else:
				line = package
		requirements.append(line)
	return requirements

def parse_dependency_links(file_name):
	dependency_links = []
	for line in open(
			os.path.join(os.path.dirname(__file__), "config", file_name), "r"):
		line = line.strip()
		# comments and blank lines
		if re.match(r"(^#)|(^$)", line):
			continue
		if line.startswith("git+"):
			parts = line.split('#')
			url_parts = parts.pop(0).split('@')
			if len(url_parts) == 3:
				tag = url_parts.pop()
				version = tag.replace('v', '')
				url = "%s/archive/%s.tar.gz#%s-%s" % (
					'@'.join(url_parts)[4:], tag, '#'.join(parts), version)
			else:
				url = "%s#%s" % ('@'.join(url_parts)[4:], '#'.join(parts))
			dependency_links.append(url)
	return dependency_links

setup(
	name = "kaws",
	version = "1.0.6",
	url = "https://wiki.knewton.net/index.php/Tech",
	author = "Devon Jones",
	author_email = "devon.jones@gmail.com",
	license = "Apache 2.0",
	scripts = [
		"bin/asg-change-key",
		"bin/asg-from-instance",
		"bin/asg-report-unused-configs",
		"bin/aws-env",
		"bin/aws-env-aliases.sh",
		"bin/aws-tool-setup",
		"bin/ec2-describe-snapshots",
		"bin/ec2-instance-count",
		"bin/ec2-list-groups",
		"bin/ec2-list-instances",
		"bin/ec2-list-tags",
		"bin/elb-cull-dead-instances",
		"bin/elb-dns-from-ids",
		"bin/elbs-from-instance-id",
		"bin/find-cfn-resource",
		"bin/gzip-respooler",
		"bin/iam-list-users",
		"bin/rds-list",
		"bin/s3-backup-schedule",
		"bin/s3-clean",
		"bin/s3-compare-listings",
		"bin/s3-copy-bucket",
		"bin/s3-copy-key",
		"bin/s3-create-bucket",
		"bin/s3-delete",
		"bin/s3-delete-bucket",
		"bin/s3-describe-bucket",
		"bin/s3-destroy-bucket",
		"bin/s3-get",
		"bin/s3-list",
		"bin/s3-list-buckets",
		"bin/s3-owners",
		"bin/s3-put",
		"bin/s3-readme",
		"bin/s3-set-acl",
		"bin/s3-spooling-sender",
		"bin/s3-sync",
		"bin/s3-sync-local",
		"bin/sdb-backup",
		"bin/sdb-create-domain",
		"bin/sdb-create-item",
		"bin/sdb-delete-item",
		"bin/sdb-get-item",
		"bin/sdb-list-domains",
		"bin/sdb-query",
		"bin/sdb-update-item",
		"bin/sqs-get-message",
		"bin/sqs-list-queues",
		"bin/sqs-post-message",
		"bin/asg-change-key",
		"bin/asg-from-instance",
	],
	packages = find_packages(),
	cmdclass = {"test": PyTest},
	package_data = {"config": ["requirements.txt"]},
	install_requires = parse_requirements("requirements.txt"),
	tests_require = parse_requirements("requirements.txt"),
	dependency_links=parse_dependency_links("requirements.txt"),
	description = "Knewton libraries for dealing with Amazon Web Services.",
	long_description = "\n" + open("README.md").read(),
)
