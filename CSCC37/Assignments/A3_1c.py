def get_machine_epsilon():
    machine_epsilon = 1
    while 1 + (machine_epsilon / 2.0) != 1:
        machine_epsilon = machine_epsilon / 2.0
    return machine_epsilon

def f(x):
    return x**2 - 0.5

def g(x):
    return x - x**2 + 0.5

eps = get_machine_epsilon()

def fixed_point_iteration(x):
    prev = None
    k = 0
    print("|", "k ", "|", "x_{k-1}           ", "|", "x_k               ", "|")
    print("|----|--------------------|--------------------|")
    print("|", f"{k:02d}", "|", "                  ", "|", f"{x:.16f}", "|")
    while (k == 0 or abs(x-prev) > eps or abs(f(x)) > eps):
        prev = x
        x = g(x)
        k += 1
        print("|", f"{k:02d}", "|", f"{prev:.16f}", "|", f"{x:.16f}", "|")

fixed_point_iteration(0.7071)