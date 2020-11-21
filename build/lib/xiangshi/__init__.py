from .main import calculator
from .formats import FormatFuncs as fmt
from .development import calculator as dev
from .weight import calculator as ext

cal = calculator()

cossim = cal.cossim
minhash = cal.minhash
simhash = cal.simhash

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
