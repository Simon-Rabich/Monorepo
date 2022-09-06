import binascii

# External packages
from Cryptodome.Hash import MD4


def ntlm_over_ntlm(pwd: str):
    h = MD4.new(pwd.encode("utf-16le")).digest()
    ntlm = binascii.hexlify(h).decode("utf8")
    ntlm_over_ntlm_hash = MD4.new(ntlm.encode("utf-16le")).digest()
    return binascii.hexlify(ntlm_over_ntlm_hash).decode("utf8")
