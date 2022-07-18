import numpy as np
import math


def get_calc_vec(base, a):
    rad = math.radians(a)
    x = np.array([[math.cos(rad), -math.sin(rad)],
                  [math.sin(rad), math.cos(rad)]])
    ans = np.dot(x, base)
    return ans


def main():
    A, B, H, M = map(int, input().split())
    sum_time = H * 60 + M

    # それぞれの角度
    a_H = sum_time / 720 * 360
    a_M = M / 60 * 360
    #print(a_H, a_M)

    base_H_vec = np.array([0, A])
    base_M_vec = np.array([0, B])
    #print(base_H_vec, base_M_vec)
    vec_H = get_calc_vec(base_H_vec, a_H)
    vec_M = get_calc_vec(base_M_vec, a_M)

    ans_vec = vec_H - vec_M
    print(np.linalg.norm(ans_vec, ord=2))


main()