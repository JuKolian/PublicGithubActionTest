import xml.etree.ElementTree as ET
import os
import sys

PACKAGE_XML = os.path.join(os.getcwd(), "package.xml")

try:
    tree = ET.parse(PACKAGE_XML)
    root = tree.getroot()
    version_elem = root.find("version")
    if version_elem is None:
        raise ValueError("No <version> tag found")
    version_full = version_elem.text.strip()
    parts = version_full.split(".")
    version_major = parts[0] if len(parts) > 0 else ""
    version_minor = ".".join(parts[:2]) if len(parts) > 1 else version_major
    version_patch = version_full
except Exception as e:
    print(f"Error extracting version: {e}", file=sys.stderr)
    sys.exit(1)

print("---- Version Extraction ----")
print(f"Full version: {version_patch}")
print(f"Major.Minor: {version_minor}")
print(f"Major only: {version_major}")

# Write outputs for GitHub Actions
github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
    with open(github_output, "a") as f:
        f.write(f"version_full={version_patch}\n")
        f.write(f"version_minor={version_minor}\n")
        f.write(f"version_major={version_major}\n")