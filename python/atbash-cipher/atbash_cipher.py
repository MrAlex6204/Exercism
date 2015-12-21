import string

def encode(message,spaced=True,lenght=5):
	plain = list(string.lowercase)
	cipher = list(reversed(list(string.lowercase)))
	normalized_msg  = [lettler for lettler in message.lower() if lettler.isalnum()]		
	encode_msg = "".join([cipher[plain.index(lettler)] if not lettler.isdigit() else lettler for lettler in normalized_msg ])
	return (" " if spaced else "").join([encode_msg[i:(i+lenght)] for i in range(0,len(encode_msg),lenght) ])
									
def decode(message):return encode(message,False)


	
		
	
	
		