name = 'marie moreau' # this is a string Marie Moreau
print(name.capitalize()) # Marie moreau

print(name.title())

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
	upper_cased_address = address.upper()

print(upper_cased_address)

"""
Note: All string methods will give you back a new string
"""

label = f'''
=============================
NAME: {name.title()}
ADDRESS: {upper_cased_address}
PHONE: +256788888888
COMPANY: FEDEX
==============================
'''

print(label)