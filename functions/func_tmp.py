# matrix = []
def matrix(n_l=1, m_l=0, value_l=0):
    if n_l == 1:
        for _ in range(n_l):
            matrix_l = [[value_l] * n_l for _ in range(n_l)]
    if n_l != 1 and m_l == 0:
        for _ in range(n_l):
            matrix_l = [[value_l] * n_l for _ in range(n_l)]
    if n_l != 1 and m_l != 0:
        for _ in range(n_l):
            matrix_l = [[value_l] * m_l for _ in range(n_l)]
    return matrix_l



print(matrix())
