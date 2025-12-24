import xml.etree.ElementTree as ET
import os
import sys

try:
    tree = ET.parse("package.xml")
    root = tree.getroot()
    version_elem = root.find("version")

    if version_elem is None:
        raise ValueError("No <version> tag found")

    version = version_elem.text.strip()

except Exception as e:
    print(f"Error extracting version: {e}", file=sys.stderr)
    sys.exit(1)

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"version={version}\n")
