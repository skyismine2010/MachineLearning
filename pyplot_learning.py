import math
import numpy as np
import matplotlib.pyplot as plt
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.ylabel("some numbers")
# plt.show()


# plt.plot([1,2,3,4], [1,4,9,16])
# plt.ylabel("some numbers")
# plt.axis([0, 10, 0, 10])
# plt.show()

# t = np.arange(0., 5., 0.2)
# plt.axis([0,8, 0, 80])
# plt.plot(t, t, 'r--', t, t**2, 'bs', t**3, 'g^')
# plt.show()

# x = np.arange(0., 10, 0.1)
# line = plt.plot(x, np.sin(x), 'r--')
# plt.setp(line, color='b', linewidth=2.0)
# plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#
# x = np.arange(0.0, 10.0, 0.1)
# plt.figure(2)
# plt.plot(x, x)
# plt.show()


def sig_mod(x_vec):
    return  1 / (1 + math.e ** (-1 * x_vec))


if __name__ == '__main__':
    x = np.arange(-2.0, 2.0, 0.1)

    plt.plot(x, sig_mod(x), "r--")
    plt.show()
