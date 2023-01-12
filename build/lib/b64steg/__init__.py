from b64steg.B64steger import B64steger

print('> Welcome to use b64steg tool.')
print('> author: Mz1')
print('> You can issue at https://github.com/Mz1z/b64steg\n')


Steg = B64steger # constructor
steg = Steg()


# text使用\n分割
def decry(text):
	return steg.decry(text)


def encry(b):
	return steg.encry(b)

