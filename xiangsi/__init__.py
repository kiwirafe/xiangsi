from .func import Functions
from .main import Calculator

fun = Functions()
cal = Calculator()

lang = fun.lang
weight = fun.weight
construct = fun.construct
update_stopwords = fun.update_stopwords
cossim = cal.cossim
minhash = cal.minhash
simhash = cal.simhash
jaccard = cal.jaccard

__all__ = [
    'Calculator',
]
