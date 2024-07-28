"""
Index file hash tool for qrm-resources
---

Copyright (c) 2020, MiaowWare
Released under the terms of the BSD 3-Clause license.
"""


import binascii
import hashlib
import json
from datetime import datetime, UTC
from pathlib import Path


basedir = Path("resources/")
index_file = basedir / "index.json"
backup = basedir / ("~" + index_file.name)


print("Reading the index file...")
with index_file.open("r") as file:
    index = json.load(file)

    # Creating a backup
    with backup.open("w") as bkfile:
        file.seek(0)
        bkfile.write(file.read())


print("Getting the hashes...")
for resource, versions in index["resources"].items():
    for version, files in versions.items():
        for file_idx, file in enumerate(files):
            filepath = basedir / file["filename"]
            with filepath.open("rb") as file:
                hashed = hashlib.md5(file.read())
            index["resources"][resource][version][file_idx]["hash"] = str(binascii.hexlify(hashed.digest()), "utf-8")


index["last_updated"] = datetime.now(UTC).isoformat()


print("Writing the hashes...")
with index_file.open("w", newline="\n") as file:
    json.dump(index, file, indent=4)
    file.write("\n")


# Everything ran fine, remove the backup
backup.unlink()
