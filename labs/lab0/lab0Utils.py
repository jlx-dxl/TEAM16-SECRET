import numpy as np


def linear_solver(A, b):
    """
    Solve for x Ax=b. Assume A is invertible.
    Args:
        A: nxn numpy array
        b: 0xn numpy array

    Returns:
        x: 0xn numpy array
    """
    # Insert student code here
    # Since A is invertible: x = A_inv x b
    A_inv = np.linalg.inv(A)
    x = np.matmul(A_inv,b)
    return x


def angle_solver(v1, v2):
    """
    Solves for the magnitude of the angle between v1 and v2
    Args:
        v1: 0xn numpy array
        v2: 0xn numpy array

    Returns:
        theta = scalar >= 0 = angle in radians
    """
    # Insert student code here
    cos_theta = np.matmul(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    # print(cos_theta)
    theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    return theta

def linear_euler_integration(A, x0, dt, nSteps):
    """
    Integrate the ode x'=Ax using euler integration where:
    x_{k+1} = dt (A x_k) + x_k
    Args:
        A: nxn np array describing linear differential equation
        x0: 0xn np array Initial condition
        dt: scalar, time step
        nSteps: scalar, number of time steps

    Returns:
        x: state after nSteps time steps (np array)
    """
    # Insert student code here
    x = x0
    for k in range(nSteps):
        # print(k)
        x = dt * (np.matmul(A,x)) + x
        # print(x)
    return x


if __name__ == '__main__':
    # Example call for linear solver
    A = np.array([[1, 2], [3, 4]])
    b = np.array([1, 2])
    print(linear_solver(A, b))

    # Example call for angles between vectors
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])
    print(angle_solver(v1, v2))

    # Example call for euler integration
    # np.random.seed(1)
    A = np.random.rand(3, 3)
    x0 = np.array([1, 1, 1])
    dt = 0.01
    nSteps = 100
    print(linear_euler_integration(A, x0, dt, nSteps))
