class Bool:
    def __init__(self) -> None:
        self.true = lambda x: lambda y: x
        self.false = lambda x: lambda y: y


    def lam_not(self, boolean):
        no = lambda n: (n)(self.false)(self.true)
        return no(boolean)


    def lam_and(self, sig1, sig2):
        an = lambda x: lambda y: (x)(y(self.true)(self.false))(self.false)
        # an = lambda x, y: (x)(y(self.true)(self.false))(self.false)
        return an(sig1)(sig2)


    def lam_or(self, sig1, sig2):
        l_or = lambda x: lambda y: x(self.true)(y(self.true)(self.false))
        return l_or(sig1)(sig2)


b = Bool()

# print(b.lam_not(b.false)(1)(0))

# Printing Truth Table for and
print("Logical And truth table\n------")
print("1) False, False", b.lam_and(b.false, b.false)(1)(0))
print("2) False, True", b.lam_and(b.false, b.true)(1)(0))
print("3) True, False", b.lam_and(b.true, b.false)(1)(0))
print("4) True, True",b.lam_and(b.true, b.true)(1)(0))

# Printing Truth table for or
print("Truth Table for or\n------")
print("1) False, False", b.lam_or(b.false, b.false)(1)(0))
print("2) False, True", b.lam_or(b.false, b.true)(1)(0))
print("3) True, False", b.lam_or(b.true, b.false)(1)(0))
print("4) True, True", b.lam_or(b.true, b.true)(1)(0))