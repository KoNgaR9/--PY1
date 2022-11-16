from pprint import pprint
list_comp = [{'bin': bin(nom), 'dec': nom, 'hex': hex(nom), 'oct': oct(nom)} for nom in range(16)]
pprint(list_comp)
