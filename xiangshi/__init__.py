from .main import calculator
<<<<<<< HEAD
from .formats import FormatFuncs as fmt
from development import calculator as dev
from .weight import calculator as ext
=======
from .formats import formats
from .weight import calculator as extra
>>>>>>> e97ffbae5c3dbae9a07393eba0bfd095d292b62a

calculator = calculator()

cossim = calculator.cossim
minhash = calculator.minhash
simhash = calculator.simhash

<<<<<<< HEAD
noweight = ext()
noweight.weight = None

tfweight = ext()
=======
noweight = extra()
noweight.weight = None

tfweight = extra()
>>>>>>> e97ffbae5c3dbae9a07393eba0bfd095d292b62a
tfweight.weight = "TF"

__all__ = [
    'calculator',
<<<<<<< HEAD
    'fmt',
    'dev',
    'noweight',
    'tfweight'
]
=======
    'formats',
    'noweight',
    'tfweight'
]
>>>>>>> e97ffbae5c3dbae9a07393eba0bfd095d292b62a
