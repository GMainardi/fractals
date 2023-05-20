import colorsys
from numpy import array
import sympy as sym
import tqdm

class ComplexFunction:

    def __init__(self, function) -> None:
        self.function = function

    def applies(self, value: complex) -> complex:
        '''
        Apply a complex function in a value

        `value`: input complex number

        return: the function aplied to `value`
        '''
        return self.function(value)

    def color(self, i):
        color_of_the_set = 255 * array(colorsys.hsv_to_rgb(i / 245.0, 0.8, 0.9))
        return tuple(color_of_the_set.astype(int))[::-1]
    
    def converges(self, max_it: int = 1000) -> bool:
        '''
        Check if `self.funciton` converges starting in z = 0

        `max_it`: the max numbers of times the function will be applied to its self

        return: `True` if the function converges before `max_it` times, and `False` otherwise
        '''
        z = self.z

        for it in range(max_it):
            z = self.applies(z)

            if abs(z) > 2:
                return self.color(it)
            
        return 0


    

class MandelBrotFunc(ComplexFunction):

    def __init__(self, c: complex) -> None:
        self.z = 0+0j
        def func(z: complex) -> complex:
            return z**2 + c
        
        super().__init__(func)

    

class JuliaSetFunc(ComplexFunction):

    def __init__(self, z) -> None:
        self.z = z
        def func(z: complex) -> complex:
            return z**2 + complex(0.30, 0.5)
        
        super().__init__(func)
   
class HiddinMandel(ComplexFunction):

    def __init__(self, l: complex) -> None:
        z = sym.Symbol('z')

        f = (z-1)*(z+1)*(z-l)

        diff_f = sym.diff(f)

        self.f_func = sym.lambdify(z,f,'numpy')
        self.diff_f_func=sym.lambdify(z,diff_f,'numpy') 
        self.roots = [1, -1, l]

    def resolves_newton(self, x):

        return x - self.f_func(x)/self.diff_f_func(x)
    
    def converges(self, max_it: int = 100) -> bool:
        '''
        Check if `self.funciton` converges starting in z = 0

        `max_it`: the max numbers of times the function will be applied to its self

        return: `True` if the function converges before `max_it` times, and `False` otherwise
        '''
        z = sum(self.roots)/3

        for _ in range(max_it):
            z = self.resolves_newton(z)

            for idx, root in enumerate(self.roots):
                if abs(z-root) < 0.00001:
                    return self.color(idx)
                
        return (0, 0, 0)
    
    def color(self, i):
        t = [50, 50, 50]
        t[i] = 200
        return tuple(t)