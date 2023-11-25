name = 'marie moreau' # this is a string Marie Moreau
# print(name.capitalize()) # Marie moreau

# print(name.title())

"""
We want: To store all addresses in uppercase, but if the already uppercased,
then don't convert it.

-- Is the address uppercased?
-- If it is, then do nothing.
-- If it is not uppercased, then convert it.
"pseudo code"
"""

address = '221 baker street' # 221 BAKER STREET

if (address.isupper()):
	pass
else:
	print(address.upper())

# print(address)
