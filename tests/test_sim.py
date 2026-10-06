import unittest
from sim import baseline, wage0, cost, delta, profit, profit_derivative, crossings

class ModelChecks(unittest.TestCase):
    def test_baseline_matching_and_continuity(self):
        b,C,w00=baseline(.5)
        self.assertAlmostEqual(wage0(b),C,places=12)
        self.assertAlmostEqual(wage0(b-1e-8),wage0(b+1e-8),places=6)
        self.assertTrue(all(wage0(i/100)>=i/100-1e-10 for i in range(101)))
    def test_derivative_independent_finite_difference(self):
        w=lambda z:.35+.2*z+.1*z*z
        dw=lambda z:.2+.2*z
        c=lambda z:.53*(1-z)
        for z in [.1,.3,.7]:
            eps=1e-6
            numerical=(profit(z+eps,.88,.5,.1,w,c)-profit(z-eps,.88,.5,.1,w,c))/(2*eps)
            self.assertAlmostEqual(numerical,profit_derivative(z,.88,.5,w,dw,c,lambda z:-.53),places=7)
    def test_zero_profit_and_foc_with_positive_rent(self):
        a,h,r=.88,.5,.2
        c=lambda z:cost(z)
        w=lambda z:a-c(z)-h*(1-z)*r
        for z in [.1,.3,.7]:
            self.assertAlmostEqual(profit(z,a,h,r,w,c),0)
            self.assertAlmostEqual(profit_derivative(z,a,h,w,lambda z:.53+h*r,c,lambda z:-.53),0)
    def test_middle_entry(self):
        self.assertLess(delta(0),0);self.assertGreater(delta(.25),0);self.assertLess(delta(.6),0)
        roots=crossings();self.assertEqual(len(roots),2)
        for z in roots:self.assertAlmostEqual(delta(z),0,places=12)
    def test_zero_cost_and_domains(self):
        self.assertAlmostEqual(delta(.2,k=0),.88-wage0(.2))
        with self.assertRaises(ValueError):delta(.9)
        with self.assertRaises(ValueError):baseline(0)
        with self.assertRaises(ValueError):cost(.2,-1)

if __name__=='__main__':unittest.main()
