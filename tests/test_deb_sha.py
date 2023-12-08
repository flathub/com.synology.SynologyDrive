"""Module providing hash functions."""
import hashlib
from urllib.request import urlretrieve
import os
import yaml

def test_deb_sha():
	"""Test that the deb file has the correct sha256 and size as discribed"""

	# Read yaml file
	with open('../com.synology.SynologyDrive.yaml', 'r', encoding="utf-8") as file_yaml:
		app_yaml = yaml.safe_load(file_yaml)

		# Retrieve url and sha
		deb_url = ""
		deb_sha_256 = ""
		deb_size = 0
		sources = app_yaml['modules'][0]["sources"]
		for source in sources:
			if "filename" in source and source["filename"] == "synology-drive.deb":
				deb_url = source["url"]
				deb_sha_256 = source["sha256"]
				deb_size = source["size"]
				break

		# Download deb
		urlretrieve(deb_url, ".synology-drive.deb")

		# Test file size deb
		size = os.path.getsize(".synology-drive.deb")
		assert size == deb_size

		# Test hash deb
		with open('.synology-drive.deb', 'rb') as file_deb:
			b = file_deb.read()
			readable_hash = hashlib.sha256(b).hexdigest()
			assert readable_hash == deb_sha_256
