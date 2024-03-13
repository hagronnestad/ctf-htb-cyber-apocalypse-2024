from Crypto.Cipher import AES
import base64

# Provided data
AES_KEY = "Y1dwaHJOVGs5d2dXWjkzdDE5amF5cW5sYUR1SWVGS2k="
MODE = "CBC"
BLOCK_SIZE = 128
KEY_SIZE = 256
PAYLOAD = "bEG+rGcRyYKeqlzXb0QVVRvFp5E9vmlSSG3pvDTAGoba05Uxvepwv++0uWe1Mn4LiIInZiNC/ES1tS7Smzmbc99Vcd9h51KgA5Rs1t8T55Er5ic4FloBzQ7tpinw99kC380WRaWcq1Cc8iQ6lZBP/yqJuLsfLTpSY3yIeSwq8Z9tusv5uWvd9E9V0Hh2Bwk5LDMYnywZw64hsH8yuE/u/lMvP4gb+OsHHBPcWXqdb4DliwhWwblDhJB4022UC2eEMI0fcHe1xBzBSNyY8xqpoyaAaRHiTxTZaLkrfhDUgm+c0zOEN8byhOifZhCJqS7tfoTHUL4Vh+1AeBTTUTprtdbmq3YUhX6ADTrEBi5gXQbSI5r1wz3r37A71Z4pHHnAoJTO0urqIChpBihFWfYsdoMmO77vZmdNPDo1Ug2jynZzQ/NkrcoNArBNIfboiBnbmCvFc1xwHFGL4JPdje8s3cM2KP2EDL3799VqJw3lWoFX0oBgkFi+DRKfom20XdECpIzW9idJ0eurxLxeGS4JI3n3jl4fIVDzwvdYr+h6uiBUReApqRe1BasR8enV4aNo+IvsdnhzRih+rpqdtCTWTjlzUXE0YSTknxiRiBfYttRulO6zx4SvJNpZ1qOkS1UW20/2xUO3yy76Wh9JPDCV7OMvIhEHDFh/F/jvR2yt9RTFId+zRt12Bfyjbi8ret7QN07dlpIcppKKI8yNzqB4FA=="

# Decode the key and payload from Base64
key = base64.b64decode(AES_KEY)
payload = base64.b64decode(PAYLOAD)

# [byte[]] $fullData = $aesManaged.IV + $encryptedData
iv = payload[:16]
encrypted_message = payload[16:]

# Initialize AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the payload
decrypted_message = cipher.decrypt(encrypted_message)

# Remove padding
unpadded_message = decrypted_message[:-decrypted_message[-1]]

# Convert bytes to string (assuming UTF-8 encoding)
decrypted_string = unpadded_message.decode('utf-8')

print("Decrypted message:", decrypted_string)