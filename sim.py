"""Entry at pre-AI wages, NOT equilibrium with AI. See extensions.md.
Uniform baseline adapted from ai-05-ide (MIT), Belén Vásquez, 2026.
"""
import csv
import json
import math
from pathlib import Path


def baseline(h):
    if not 0 < h < .75:
        raise ValueError('Uniform benchmark requires 0 < h < .75')
    b = 2 / (1 + h + math.sqrt(1 + h*h))
    C = (1 - h*b*(1-b)) / (1 + h*(1-b))
    return b, C, b-h*C


def wage0(z, h=.5):
    if not 0 <= z <= 1:
        raise ValueError('z outside [0,1]')
    b, C, w00 = baseline(h)
    if z <= b:
        return w00 + h*C*z + h*z*z/2
    return C + 1 - math.sqrt(max(0, 1-2*(z-b)/h))


def cost(z, k=.53):
    if k < 0:
        raise ValueError('negative cost parameter')
    return k*(1-z)


def delta(z, a=.88, h=.5, k=.53):
    if not 0 <= z <= a < 1:
        raise ValueError('requires 0 <= z <= a < 1')
    return a-cost(z,k)-wage0(z,h)


def profit(z, a, h, r, wage, verification):
    if not (0 <= z <= a < 1 and h > 0):
        raise ValueError('invalid firm domain')
    return (a-wage(z)-verification(z))/(h*(1-z))-r


def profit_derivative(z, a, h, wage, dwage, verification, dcost):
    n = 1/(h*(1-z))
    return n/(1-z)*(a-wage(z)-verification(z))-n*(dwage(z)+dcost(z))


def crossings(a=.88, h=.5, k=.53, steps=2000):
    """Sign-changing roots on [0,a]; not a detector of tangential zeros."""
    roots=[]
    lo=0.; flo=delta(lo,a,h,k)
    for i in range(1,steps+1):
        hi=a*i/steps; fhi=delta(hi,a,h,k)
        if flo*fhi < 0:
            left,right=lo,hi
            for _ in range(55):
                mid=(left+right)/2
                if delta(left,a,h,k)*delta(mid,a,h,k)<=0: right=mid
                else: left=mid
            roots.append((left+right)/2)
        lo,flo=hi,fhi
    return roots


def main():
    folder=Path(__file__).resolve().parent/'extra/results';folder.mkdir(parents=True,exist_ok=True)
    a,h,k=.88,.5,.53
    rows=[dict(z=z,cost=cost(z,k),baseline_wage=wage0(z,h),ai_offer=a-cost(z,k),entry_gap=delta(z,a,h,k)) for z in [0,.25,.6]]
    result=dict(scope='Illustrative entry at pre-AI wages; not extended equilibrium',parameters=dict(a=a,h=h,kappa=k),baseline=dict(zip(['b','C','w00'],baseline(h))),rows=rows,sign_changing_roots=crossings())
    (folder/'example.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    with (folder/'entry_grid.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['z','baseline_wage','zero_cost_offer','constant_cost_offer','heterogeneous_offer','heterogeneous_entry_gap'])
        # Constant equals the heterogeneous cost averaged uniformly over eligible types.
        for i in range(441):
            z=a*i/440
            writer.writerow([format(v,'.10f') for v in [z,wage0(z,h),a,a-k*(1-a/2),a-cost(z,k),delta(z,a,h,k)]])
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
