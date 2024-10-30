import numpy as np
import matplotlib.pyplot as plt

import choclo

G = 6.6743e-11  # gravitational constant
assert G == choclo.constants.GRAVITATIONAL_CONST


def kernel_z(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    result = -(x * np.log(y + r) + y * np.log(x + r) - z * np.arctan(x * y / z / r))
    return result


def evaluate_kernel(coordinates, prism, kernel):
    # Extract the coordinates of the observation point
    easting, northing, upward = coordinates

    # Initialize a result value equal to zero
    result = 0.0

    # Iterate over the vertices of the prism
    for i in range(2):
        for j in range(2):
            for k in range(2):
                # Compute shifted coordinates
                shift_east = prism[1 - i] - easting
                shift_north = prism[3 - j] - northing
                shift_upward = prism[5 - k] - upward
                # Evaluate kernel. Use the right sign.
                result += (-1) ** (i + j + k) * kernel(
                    shift_east, shift_north, shift_upward
                )

    return result


def gravity_z(coordinates, prism, density):
    u_z = evaluate_kernel(coordinates, prism, kernel_z)
    return G * density * u_z


coordinates = (0.0, 0.0, 2.0)

west, east = -10.0, 10.0
south, north = -12.0, 12.0
bottom, top = -15.0, -5.0
prism = [west, east, south, north, bottom, top]
density = 2900

gz = gravity_z(coordinates, prism, density)
print(f"{gz} m/s2")


assert choclo.prism.gravity_u(*coordinates, *prism, density) == gz


easting = np.linspace(-30.0, 30.0, 121)
northing = np.linspace(-30.0, 30.0, 121)
easting, northing = np.meshgrid(easting, northing)
upward = 2.0 * np.ones_like(easting)
coordinates = (easting.ravel(), northing.ravel(), upward.ravel())


def gravity_z(coordinates, prism, density):
    easting, northing, upward = coordinates
    # Initialize an array of results
    n_data = easting.size
    result = np.empty(n_data)
    # Iterate over the observation points
    for i in range(n_data):
        # Evaluate the kernel for the current observation point
        u_z = evaluate_kernel((easting[i], northing[i], upward[i]), prism, kernel_z)
        # Add result to the array
        result[i] = G * density * u_z
    return result


gz = gravity_z(coordinates, prism, density)


plt.pcolormesh(easting, northing, gz.reshape(easting.shape))
plt.gca().set_aspect("equal")
plt.xlabel("easting [m]")
plt.ylabel("northing [m]")
plt.colorbar(label="m/s2")
plt.title("$g_z$ due to single prism")
plt.savefig("images/gz-single-prism.png")
plt.show()
