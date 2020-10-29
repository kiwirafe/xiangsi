from .main import calculator
from .formats import formats
from .weight import calculator as extra

calculator = calculator()

cossim = calculator.cossim
minhash = calculator.minhash
simhash = calculator.simhash

noweight = extra()
noweight.weight = None

tfweight = extra()
tfweight.weight = "TF"

__all__ = [
    'calculator',
    'formats',
    'noweight',
    'tfweight'
]
