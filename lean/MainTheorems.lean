import Mathlib

/- Algebraic implications only: no derivative or equilibrium existence theorem. -/
namespace HeterogeneousVerification

def offer (a c r h z : ℝ) : ℝ := a - c - h * (1-z) * r

theorem zeroRentOffer (a c h z : ℝ) : offer a c 0 h z = a-c := by
  simp [offer]

theorem linearCostOffer (a k z : ℝ) :
    a-k*(1-z) = a-k+k*z := by ring

theorem slopeAtZeroRent (wp cp h r : ℝ)
    (foc : wp+cp=h*r) (idle : r=0) : wp = -cp := by
  rw [idle] at foc
  linarith

theorem positiveCostLowersOffer (a c : ℝ) (hc : 0 ≤ c) : a-c ≤ a := by
  linarith

theorem entryIffPositiveProfit (n a c w : ℝ) (hn : 0 < n) :
    0 < n*(a-c-w) ↔ w < a-c := by
  constructor
  · intro hp
    nlinarith
  · intro he
    apply mul_pos hn
    linarith

#print axioms zeroRentOffer
#print axioms linearCostOffer
#print axioms slopeAtZeroRent
#print axioms positiveCostLowersOffer
#print axioms entryIffPositiveProfit
end HeterogeneousVerification
