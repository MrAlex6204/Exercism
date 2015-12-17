import math
import string

def encode(message):	
	normalized_message = "".join([s for s in message if not s in (string.punctuation+" ") ]).lower()	
	length = int(math.ceil(math.sqrt(len(normalized_message))))
	words = [normalized_message[i::length] for i in range(length)]								
	return " ".join(words)
