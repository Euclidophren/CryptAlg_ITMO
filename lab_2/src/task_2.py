def get_uv(cont_frac):
    u_start, u_prev, v_start, v_prev = 1, 0, 0, 1
    us, vs = [], []
    for i in range(len(cont_frac)):
        us.append(cont_frac[i] * u_start + u_prev)
        vs.append(cont_frac[i] * v_start + v_prev)
        u_prev, u_start = u_start, us[i]
        v_prev, v_start = v_start, vs[i]
    return us, vs


def get_potential_phi(e, u, v):
    return (e * v - 1) / u


def solve_equation(us, vs):
    for i in range(1, len(us)):
        b = n - get_potential_phi(e, us[i], vs[i]) + 1
        x_dict = solve([x ^ 2 - b * x + n == 0], x, solution_dict=True)
        print(x_dict)
