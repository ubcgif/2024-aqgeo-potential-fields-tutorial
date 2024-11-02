import numpy as np
import matplotlib.pyplot as plt

y, z = 1e-5, 0.0
x = np.linspace(-500, 0, 501)

r = np.sqrt(x**2 + y**2 + z**2)
log = np.log(x + r)

plt.plot(x, log)
plt.ylabel("$\ln(x + r)$")
plt.xlabel("$x$")
plt.title(f"y={y:.1e}, z={z:.1f}")
plt.savefig("images/log_small_values_issue.png", dpi=600)
plt.show()

log_new = np.log((y**2 + z**2) / (r - x))
plt.plot(x, log, label="unstable")
plt.plot(x, log_new, label="fixed")
plt.ylabel("$\ln(x + r)$")
plt.xlabel("$x$")
plt.title(f"y={y:.1e}, z={z:.1f}")
plt.legend()
plt.savefig("images/log_small_values_fixed.png", dpi=600)
plt.show()
