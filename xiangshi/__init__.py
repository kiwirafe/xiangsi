from .main import calculator
from .formats import FormatFuncs as fmt
from development import calculator as dev
from .weight import calculator as ext

calculator = calculator()

cossim = calculator.cossim
minhash = calculator.minhash
simhash = calculator.simhash

noweight = ext()
noweight.weight = None

tfweight = ext()
tfweight.weight = "TF"

__all__ = [
    'calculator',
    'fmt',
    'dev',
    'noweight',
    'tfweight'
]
