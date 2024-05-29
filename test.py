from bech32py import bech32

# decode
addr = "bc1qkg62ae0wwntkzhq8td87s87c4nj5zdlj2ga8j7"
(ver, data) = bech32.decode("bc", addr)
assert ver == 0
assert bytes(data).hex() == "b234aee5ee74d7615c075b4fe81fd8ace54137f2"

# encode
public_key_hash = bytes.fromhex("8bf743f3fd7f46804c39711af735b121747ef6b4")
assert bech32.encode('bc', 0, public_key_hash) == "bc1q30m58ula0argqnpewyd0wdd3y968aa457pksa3"

print("OK")
