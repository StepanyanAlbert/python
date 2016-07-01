import sys,hashlib

def get_hash_word(filename=sys.argv[1:2]):
		"""Function returns filename where hash word is located.
		Gets only one argument filename"""
		try:
				f_n=''.join(filename)
				f=open(f_n)
		except IOError:
				print ('Couldn\'t find the path to %s' % filename)
				sys.exit()
		else:
				hash_word=f.read()
				return ''.join(hash_word).replace('\n','')

def check(wordlist_file=sys.argv[2:3]):
		"""Takes one arguments wordlist path"""
		try:
				w_l=''.join(wordlist_file)
				w=open(w_l)
		except IOError:
				print ('Couldn\'t find the path to %s' % worlist_file)
		else:
					
				for word in w.readlines():
						wor=word.rstrip()
						cr=hashlib.sha512() # change the way of hashing as you wish (sha512,md5,.....)
						cr.update(wor)
						e=cr.hexdigest()
						cracked_pass=e
						if cracked_pass==get_hash_word():
								print 'Password cracked + %s' % word
								sys.exit()	
				print('Couldn\'t crack password for %s '% cracked_pass )
						
if __name__=='__main__':
		check()

