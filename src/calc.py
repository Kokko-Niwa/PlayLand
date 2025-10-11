import csv, math, sys

EPS = 1e-6
LMB = 1.0

def priority(E, R, D, H, eps=EPS, lmb=LMB):
    return 1.0 / (E + R + D + lmb*H + eps)

def virtue(C, R, E, eps=EPS):
    return (C - R) * (C / (R + E + eps))

def f(x):  # safe float
    try:
        return float(x)
    except:
        return 0.0

def main(path="Data/examples/cases.csv"):
    with open(path, encoding="utf-8") as fp:
        for row in csv.DictReader(fp):
            case = row.get("case_id","(no id)")
            C = f(row.get("C",0)); R = f(row.get("R",0)); E = f(row.get("E",0))
            D = f(row.get("D",0)); H = f(row.get("H",0))
            pr = priority(E,R,D,H)
            vt = virtue(C,R,E)
            print(f"{case}  priority={pr:.4f}  virtue={vt:.4f}")

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "Data/examples/cases.csv"
    main(path)
