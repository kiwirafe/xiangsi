from .func import Functions
from .main import Calculator

fun = Functions()
cal = Calculator()

construct = fun.construct
cossim = cal.cossim
minhash = cal.minhash
simhash = cal.simhash
jaccard = cal.jaccard

__all__ = [
    'calculator',
]
