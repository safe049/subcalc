W_C = -0.6
W_N = 0.8
W_A = 0.5
W_F = -1.2


def calc_subjective_custom(t, c, n, a, f):
    """
    Parameters c,n,a,f should be in range of 0.0 to 1.0
    The unit could be t seconds, t hours, t days
    """
    k = 1 + W_C*c + W_N*n + W_A * a + W_F*f
    k = max(0.1, min(3.0, k))
    sub_t = t * k
    return sub_t


def calc_subjective_single_unit(c, n, a, f):
    """
    Parameters should be in range of 0.0 to 1.0
    The unit could be 1 second, 1 hour, 1 day
    """
    k = 1 + W_C*c + W_N*n + W_A * a + W_F*f
    k = max(0.1, min(3.0, k))
    sub_t = 1 * k
    return sub_t


# pass in a list like this : [[0.5, 0.3, 0.4, 0.2],[...]] which is the c,n,a,f in each unit of time

def calc_subjective_range(t, seq):
    """
    seq should be a list like this: [[c,n,a,f],[c1,n1,a1,f1]]
    The unit could be t seconds, t hours, t days
    """
    total_sub_t = 0.0
    for state in seq:
        c, n, a, f = state
        k = 1 + W_C*c + W_N*n + W_A * a + W_F*f
        k = max(0.1, min(3.0, k))
        total_sub_t += t * k  # calculate the sub_t for each list and adding to total sub_t
    return total_sub_t
