import mynamespace.b_module as b
from mynamespace.b_module.AI import BLNAnalyzer
print(b.name)

analyzer = BLNAnalyzer()
analyzer.name()


import mynamespace.a_module as a
print(a.name)


"""
(venv) (base) grace@jeonghyeonjeong-ui-MacBookPro python-namespace-package-sample % python3 example.py

b module
common log
b module analyzer
a module
"""