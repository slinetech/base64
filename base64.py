import pybase64 as b64
import argparse as args

parser = args.ArgumentParser()
parser.add_argument("-e", "--encode", help="To encode base64")
parser.add_argument("-d", "--decode", help="To decode base64")
valArgs = parser.parse_args()
if valArgs.encode:
    msg = valArgs.encode
    msg_bytes = msg.encode('ascii')
    b64_bytes = b64.b64encode(msg_bytes)
    b64_msg = b64_bytes.decode('ascii')
    print(b64_msg)
if valArgs.decode:
    b64_msg = valArgs.decode
    b64_bytes = b64_msg.encode('ascii')
    msg_bytes = b64.b64decode(b64_bytes)
    msg = msg_bytes.decode('ascii')
    print(msg)
