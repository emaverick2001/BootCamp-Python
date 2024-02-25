# Maverick Espinosa
# mespin11

# Problem A

# Task 1

# Please write your own class for fractions in a file named frac.py.

class Frac:
    
    """ class for performing fraction operations"""
    
    def __init__(self,num,den):
        
        """
        Parameters
        ----------
        num : numerator of fraction
        den : denominator of fraction
        Raises
        ------
        ValueError
            if denominator is 0

        Returns
        -------
        None.
        """
        
        self.num = num
        if den == 0 :
            raise ValueError("Denominator can't be 0")
        self.den = den
        self.simplify()
        return
    
    def gcd(self,a,b):
        
        """
        Parameters
        ----------
        a : largest of the two values
        b : smallest of the two values

        Returns
        -------
        temp_a : greatest common factor of the two values a and b
        """
        
        temp_a = a if a > b else b
        temp_b = b if a > b else a
        while temp_b != 0:
            remainder = temp_a % temp_b
            temp_a = temp_b
            temp_b = remainder
        return temp_a
    
    def simplify (self):
        
        """
        Returns
        -------
        None. Simplifies a Frac object by dividing num and den by gcd
        """
        
        common_factor = self.gcd(self.num,self.den)
        
        self.num //= common_factor
        self.den //= common_factor
        return
    
    def __add__(self,other):
        
        """
        Parameters
        ----------
        other : Frac fraction to add to self fraction

        Returns
        -------
        result : resulting fraction from adding two fractions
        """
        
        result_num = self.num * other.den + other.num * self.den
        result_den = self.den * other.den
        result = Frac(result_num,result_den)
        result.simplify()
        return result
    
    def __iadd__(self, other):
        """
        Parameters
        ----------
        other : Frac
            Fraction to be added to self.

        Returns
        -------
        None.
        """
        # Perform addition in-place
        result_num = self.num * other.den + other.num * self.den
        result_den = self.den * other.den

        self.num = result_num
        self.den = result_den
        self.simplify()
        return self
        
    def __sub__(self,other):
        
        """
        Parameters
        ----------
        other : Frac fraction to be subtracted from self fraction

        Returns
        -------
        result : resulting fraction from subtracting two fractions
        """
        
        result_num = self.num * other.den - other.num * self.den
        result_den = self.den * other.den
        result = Frac(result_num,result_den)
        result.simplify()
        return result
    
    def __isub__(self, other):
        """
        Parameters
        ----------
        other : Frac
            The other Frac object to subtract.

        Returns
        -------
        Frac
            Result of the subtraction (self - other).
        """

        result_num = self.num * other.den - other.num * self.den
        result_den = self.den * other.den

        self.num = result_num
        self.den = result_den
        self.simplify()
        return self
        
        
    def __mul__(self,other):
        
        """
        Parameters
        ----------
        other : Frac fraction to be multiplied to self fraction

        Returns
        -------
        result : resulting fraction from multiplying two fractions
        """
        
        result_num = self.num * other.num
        result_den = self.den * other.den
        result = Frac(result_num,result_den)
        result.simplify()
        return result
    
    def __truediv__(self,other):
        
        """
        Parameters
        ----------
        other : Frac fraction to divide from self fraction

        Returns
        -------
        result : resulting fraction from dividing two fractions
        """
        
        result_num = self.num * other.den
        result_den = self.den * other.num
        result = Frac(result_num,result_den)
        result.simplify()
        return result
        
    def __le__(self, other):
        
        """
        Parameters
        ----------
        other : Frac
            The other Frac object to compare.

        Returns
        -------
        bool
            True if self <= other, False otherwise.
        """

        common_denominator = self.den * other.den
        num_self = self.num * (common_denominator // self.den)
        num_other = other.num * (common_denominator // other.den)

        return num_self <= num_other
        
    
    def __str__(self):
        return f"{self.num}/{self.den}"
