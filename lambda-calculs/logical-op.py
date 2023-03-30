class Bool:
    def __init__(self) -> None:
        self.true = lambda x: lambda y: x
        self.false = lambda x: lambda y: y


    def lam_not(self, boolean):
        l_not = lambda n: (n)(self.false)(self.true)
        return l_not(boolean)


    def lam_and(self, sig1, sig2):
        l_and = lambda x: lambda y: (x)(y(self.true)(self.false))(self.false)
        # an = lambda x, y: (x)(y(self.true)(self.false))(self.false)
        return l_and(sig1)(sig2)


    def lam_or(self, sig1, sig2):
        l_or = lambda x: lambda y: x(self.true)(y(self.true)(self.false))
        return l_or(sig1)(sig2)


b = Bool()


print("\nLogical \"And\" table\n------")
print("1) False, False", b.lam_and(b.false, b.false)(1)(0))
print("2) False, True", b.lam_and(b.false, b.true)(1)(0))
print("3) True, False", b.lam_and(b.true, b.false)(1)(0))
print("4) True, True",b.lam_and(b.true, b.true)(1)(0))

print("\nLogical \"OR\" table\n------")
print("1) False, False", b.lam_or(b.false, b.false)(1)(0))
print("2) False, True", b.lam_or(b.false, b.true)(1)(0))
print("3) True, False", b.lam_or(b.true, b.false)(1)(0))
print("4) True, True", b.lam_or(b.true, b.true)(1)(0))

print("\nLoical \"NOT\" table\n------")
print("NOT Flase", b.lam_not(b.false)(1)(0))
print("NOT True", b.lam_not(b.true)(1)(0))