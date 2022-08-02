# sciencntists =[
#    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
#    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
#     ]
    
# sciencntists

# >>> sciencntists =[
# ...    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
# ...    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
# ...     ]
# >>>     
# >>> sciencntists
# [{'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False}, {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False}]
# >>> sciencntists[0]['name'] = 'Ngounse'
# >>> sciencntists
# [{'name': 'Ngounse', 'field': 'math', 'born': 1815, 'nobel': False}, {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False}]
# >>> import collections
# >>> Scientist = collections.namedtuple('Scientist', ['name','field','born','nobel'])
# >>> Scientist
# <class '__main__.Scientist'>
# >>> Scientist(name='Ada Locelance', field='math', born=1812, nobel=false')
#   File "<stdin>", line 1
#     Scientist(name='Ada Locelance', field='math', born=1812, nobel=false')
#                                                                          ^
# SyntaxError: EOL while scanning string literal
# >>> Scientist(name='Ada Locelance', field='math', born=1812, nobel=false)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'false' is not defined
# >>> Scientist(name='Ada Locelance', field='math', born=1812, nobel=False)
# Scientist(name='Ada Locelance', field='math', born=1812, nobel=False)
# >>> ada = Scientist(name='Ada Locelance', field='math', born=1812, nobel=False)
# >>> ada.name
# 'Ada Locelance'
# >>> 
