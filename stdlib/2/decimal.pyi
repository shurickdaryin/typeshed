# Stubs for decimal (Python 2)

from typing import (
    Any, Dict, NamedTuple, Optional, Sequence, Tuple, Union,
    SupportsAbs, SupportsFloat, SupportsInt,
)

_Decimal = Union[Decimal, int]
_ComparableNum = Union[Decimal, int, float]

DecimalTuple = NamedTuple('DecimalTuple',
                          [('sign', int),
                           ('digits', Sequence[int]), # TODO: Use Tuple[int, ...]
                           ('exponent', int)])

ROUND_DOWN = ...  # type: str
ROUND_HALF_UP = ...  # type: str
ROUND_HALF_EVEN = ...  # type: str
ROUND_CEILING = ...  # type: str
ROUND_FLOOR = ...  # type: str
ROUND_UP = ...  # type: str
ROUND_HALF_DOWN = ...  # type: str
ROUND_05UP = ...  # type: str

class DecimalException(ArithmeticError):
    def handle(self, context, *args): ...

class Clamped(DecimalException): ...

class InvalidOperation(DecimalException): ...

class ConversionSyntax(InvalidOperation): ...

class DivisionByZero(DecimalException, ZeroDivisionError): ...

class DivisionImpossible(InvalidOperation): ...

class DivisionUndefined(InvalidOperation, ZeroDivisionError): ...

class Inexact(DecimalException): ...

class InvalidContext(InvalidOperation): ...

class Rounded(DecimalException): ...

class Subnormal(DecimalException): ...

class Overflow(Inexact, Rounded): ...

class Underflow(Inexact, Rounded, Subnormal): ...

def setcontext(context: Context): ...
def getcontext() -> Context: ...
def localcontext(ctx: Optional[Context] = None) -> _ContextManager: ...

class Decimal(SupportsAbs[Decimal], SupportsFloat, SupportsInt):
    def __init__(cls, value: Union[_Decimal, float, str,
                                   Tuple[int, Sequence[int], int]] = ...,
                 context: Context = ...) -> None: ...
    @classmethod
    def from_float(cls, f: float) -> Decimal: ...
    def __nonzero__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __lt__(self, other: _ComparableNum) -> bool: ...
    def __le__(self, other: _ComparableNum) -> bool: ...
    def __gt__(self, other: _ComparableNum) -> bool: ...
    def __ge__(self, other: _ComparableNum) -> bool: ...
    def compare(self, other: _Decimal) -> Decimal: ...
    def __hash__(self) -> int: ...
    def as_tuple(self) -> DecimalTuple: ...
    def to_eng_string(self, context: Context = ...) -> str: ...
    def __neg__(self) -> Decimal: ...
    def __pos__(self) -> Decimal: ...
    def __abs__(self, round: bool = True) -> Decimal: ...
    def __add__(self, other: _Decimal) -> Decimal: ...
    def __radd__(self, other: int) -> Decimal: ...
    def __sub__(self, other: _Decimal) -> Decimal: ...
    def __rsub__(self, other: int) -> Decimal: ...
    def __mul__(self, other: _Decimal) -> Decimal: ...
    def __rmul__(self, other: int) -> Decimal: ...
    def __truediv__(self, other: _Decimal) -> Decimal: ...
    def __rtruediv__(self, other: int) -> Decimal: ...
    def __div__(self, other: _Decimal) -> Decimal: ...
    def __rdiv__(self, other: int) -> Decimal: ...
    def __divmod__(self, other: _Decimal) -> Tuple[Decimal, Decimal]: ...
    def __rdivmod__(self, other: int) -> Tuple[Decimal, Decimal]: ...
    def __mod__(self, other: _Decimal) -> Decimal: ...
    def __rmod__(self, other: int) -> Decimal: ...
    def remainder_near(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def __floordiv__(self, other: _Decimal) -> Decimal: ...
    def __rfloordiv__(self, other: int) -> Decimal: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __trunc__(self) -> int: ...
    @property
    def imag(self) -> Decimal: ...
    @property
    def real(self) -> Decimal: ...
    def conjugate(self) -> Decimal: ...
    def __complex__(self) -> complex: ...
    def __long__(self) -> long: ...
    def fma(self, other: _Decimal, third: _Decimal, context: Context = ...) -> Decimal: ...
    def __pow__(self, other: _Decimal) -> Decimal: ...
    def __rpow__(self, other: int) -> Decimal: ...
    def normalize(self, context: Context = ...) -> Decimal: ...
    def quantize(self, exp: _Decimal, rounding: str = ...,
                 context: Context = ...) -> Decimal: ...
    def same_quantum(self, other: Decimal) -> bool: ...
    def to_integral(self, rounding: str = ..., context: Context = ...) -> Decimal: ...
    def to_integral_exact(self, rounding: str = ..., context: Context = ...) -> Decimal: ...
    def to_integral_value(self, rounding: str = ..., context: Context = ...) -> Decimal: ...
    def sqrt(self, context: Context = ...) -> Decimal: ...
    def max(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def min(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def adjusted(self) -> int: ...
    def canonical(self, context: Context = ...) -> Decimal: ...
    def compare_signal(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def compare_total(self, other: _Decimal) -> Decimal: ...
    def compare_total_mag(self, other: _Decimal) -> Decimal: ...
    def copy_abs(self) -> Decimal: ...
    def copy_negate(self) -> Decimal: ...
    def copy_sign(self, other: _Decimal) -> Decimal: ...
    def exp(self, context: Context = ...) -> Decimal: ...
    def is_canonical(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def is_infinite(self) -> bool: ...
    def is_nan(self) -> bool: ...
    def is_normal(self, context: Context = ...) -> bool: ...
    def is_qnan(self) -> bool: ...
    def is_signed(self) -> bool: ...
    def is_snan(self) -> bool: ...
    def is_subnormal(self, context: Context = ...) -> bool: ...
    def is_zero(self) -> bool: ...
    def ln(self, context: Context = ...) -> Decimal: ...
    def log10(self, context: Context = ...) -> Decimal: ...
    def logb(self, context: Context = ...) -> Decimal: ...
    def logical_and(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def logical_invert(self, context: Context = ...) -> Decimal: ...
    def logical_or(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def logical_xor(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def max_mag(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def min_mag(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def next_minus(self, context: Context = ...) -> Decimal: ...
    def next_plus(self, context: Context = ...) -> Decimal: ...
    def next_toward(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def number_class(self, context: Context = ...) -> str: ...
    def radix(self) -> Decimal: ...
    def rotate(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def scaleb(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def shift(self, other: _Decimal, context: Context = ...) -> Decimal: ...
    def __reduce__(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __format__(self, specifier, context=None, _localeconv=None) -> str: ...

class _ContextManager:
    new_context = ...  # type: Context
    saved_context = ...  # type: Context
    def __init__(self, new_context: Context) -> None: ...
    def __enter__(self): ...
    def __exit__(self, t, v, tb): ...

class Context:
    prec = ...  # type: int
    rounding = ...  # type: str
    Emin = ...  # type: int
    Emax = ...  # type: int
    capitals = ...  # type: int
    traps = ...  # type: Dict[type, bool]
    flags = ...  # type: Any
    def __init__(self, prec=None, rounding=None, traps=None, flags=None, Emin=None, Emax=None, capitals=None, _clamp=0, _ignored_flags=None): ...
    def clear_flags(self): ...
    def copy(self): ...
    __copy__ = ...  # type: Any
    __hash__ = ...  # type: Any
    def Etiny(self): ...
    def Etop(self): ...
    def create_decimal(self, num=...): ...
    def create_decimal_from_float(self, f): ...
    def abs(self, a): ...
    def add(self, a, b): ...
    def canonical(self, a): ...
    def compare(self, a, b): ...
    def compare_signal(self, a, b): ...
    def compare_total(self, a, b): ...
    def compare_total_mag(self, a, b): ...
    def copy_abs(self, a): ...
    def copy_decimal(self, a): ...
    def copy_negate(self, a): ...
    def copy_sign(self, a, b): ...
    def divide(self, a, b): ...
    def divide_int(self, a, b): ...
    def divmod(self, a, b): ...
    def exp(self, a): ...
    def fma(self, a, b, c): ...
    def is_canonical(self, a): ...
    def is_finite(self, a): ...
    def is_infinite(self, a): ...
    def is_nan(self, a): ...
    def is_normal(self, a): ...
    def is_qnan(self, a): ...
    def is_signed(self, a): ...
    def is_snan(self, a): ...
    def is_subnormal(self, a): ...
    def is_zero(self, a): ...
    def ln(self, a): ...
    def log10(self, a): ...
    def logb(self, a): ...
    def logical_and(self, a, b): ...
    def logical_invert(self, a): ...
    def logical_or(self, a, b): ...
    def logical_xor(self, a, b): ...
    def max(self, a, b): ...
    def max_mag(self, a, b): ...
    def min(self, a, b): ...
    def min_mag(self, a, b): ...
    def minus(self, a): ...
    def multiply(self, a, b): ...
    def next_minus(self, a): ...
    def next_plus(self, a): ...
    def next_toward(self, a, b): ...
    def normalize(self, a): ...
    def number_class(self, a): ...
    def plus(self, a): ...
    def power(self, a, b, modulo=None): ...
    def quantize(self, a, b): ...
    def radix(self): ...
    def remainder(self, a, b): ...
    def remainder_near(self, a, b): ...
    def rotate(self, a, b): ...
    def same_quantum(self, a, b): ...
    def scaleb(self, a, b): ...
    def shift(self, a, b): ...
    def sqrt(self, a): ...
    def subtract(self, a, b): ...
    def to_eng_string(self, a): ...
    def to_sci_string(self, a): ...
    def to_integral_exact(self, a): ...
    def to_integral_value(self, a): ...
    def to_integral(self, a): ...

DefaultContext = ...  # type: Context
BasicContext = ...  # type: Context
ExtendedContext = ...  # type: Context
