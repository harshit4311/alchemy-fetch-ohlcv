from eth_abi import decode_abi

encoded = bytes.fromhex("00000000000000000000000000000000000000000000000000000000000003e8")
decoded = decode_abi(["uint256"], encoded)

print(decoded)  # Should print: (1000,)
