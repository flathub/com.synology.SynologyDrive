import hashlib
import yaml
from urllib.request import urlretrieve

def test_deb_sha():
    # Read yaml file
    with open('../com.synology.SynologyDrive.yaml', 'r', encoding="utf-8") as fileYaml:
        appYaml = yaml.safe_load(fileYaml)

        # Retrieve url and sha
        debUrl = ""
        debSha256 = ""
        sources = appYaml['modules'][0]["sources"]
        for source in sources:
            if "filename" in source and source["filename"] == "synology-drive.deb":
                debUrl = source["url"]
                debSha256 = source["sha256"]
                break
        
        # Download deb
        urlretrieve(debUrl, ".synology-drive.deb")

        # Open deb
        with open('.synology-drive.deb', 'rb') as fileDeb:
            b = fileDeb.read()
            readable_hash = hashlib.sha256(b).hexdigest()
            assert readable_hash == debSha256
