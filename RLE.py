import sys

def encode(mess):
    if not mess : return ''

    old = mess[0]
    i = 1
    res = []

    for c in mess[1:]:
        if c != old:
            res.append((i,old))
            i = 1
            old = c
        else:
            i += 1
    res.append((i,old))

    return res


def decode(mess):
	#return ''.join([n*c for n,c in mess])
	
	#my first approach is down below. The above is condensed.
	# #in case of no input. Don't do anything
	if not mess : return ''
	
	res = []
	
	for t in mess:
		
		#The number of times the character occurs 
		n=t[0]
		
		#the character that needs to be printed n number of times is
		#in the second spot in the variable
		char=t[1]
		
		#write the desired number of chars
		res.append(n*char)	
			
	#return a string that is equal to the list 
	#with no seperation between the elements.  	
	return ''.join(res)

# def main(argv):
	# if  len(sys.argv)==3:
		# if sys.argv[1]=='-e':
			# with open(sys.argv[2],'r') as f:
				# mess=f.read()
				# print(encode(mess))
		# elif sys.argv[1]=='-d':
			# with open(sys.argv[2],'r') as f:
				# mess=f.read()
				# print(decode(mess))
	# else:
		# print ("RLE.py <coding> <file>")
		# sys.exit(2)
	
	
# if __name__ == "__main__":
   # main(sys.argv[1:])	

print("Input is 'KKK'\n");
k=encode("KKK");
print("Encoded version is: ");
print(k);

k=decode(encode("KKK"));
print("Decoded version is: ");
print (k);
