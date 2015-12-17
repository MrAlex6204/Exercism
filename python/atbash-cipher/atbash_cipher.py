import string
ALPHABET = [chr(L) for L in range(ord("a"),ord("z")+1)]
CIPHER = [chr(L) for L in reversed(range(ord("a"),ord("z")+1))]

def encode(message):
	normalized_msg  = [L for L in message.lower() if not L in (string.punctuation+" ") ]
	print (normalized_msg)
	encode_msg = "".join([CIPHER[ALPHABET.index(str(L))] for L in normalized_msg ])
	return " ".join([encode_msg[i::5] for i in range(5)])								
	# return encode_msg
	
if __name__=="__main__":
	print (encode("Truth is fiction."))