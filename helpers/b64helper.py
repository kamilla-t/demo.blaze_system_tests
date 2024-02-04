import base64


def convert_to_b64(string):    
    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message