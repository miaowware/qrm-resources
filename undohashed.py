# Reference implementation of converting the hex-representation
# hashes into a form that hashlib can use.
# TODO: Nuke this when implementing in qrm

import binascii

hexhash = "b9138e4c548d5c6579243d624d751432"

binhash = binascii.unhexlify(hexhash)

print(binhash)
