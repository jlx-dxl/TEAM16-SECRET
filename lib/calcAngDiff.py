
import numpy as np


def calcAngDiff(R_des, R_curr):
    """
    Helper function for the End Effector Orientation Task. Computes the axis of rotation 
    from the current orientation to the target orientation

    This data can also be interpreted as an end effector velocity which will
    bring the end effector closer to the target orientation.

    INPUTS:
    R_des - 3x3 numpy array representing the desired orientation from
    end effector to world
    R_curr - 3x3 numpy array representing the "current" end effector orientation

    OUTPUTS:
    omega - 0x3 a 3-element numpy array containing the axis of the rotation from
    the current frame to the end effector frame. The magnitude of this vector
    must be sin(angle), where angle is the angle of rotation around this axis
    """
    omega = np.zeros(3)
    ## STUDENT CODE STARTS HERE
    assert R_curr.shape == (3,3)
    assert R_des.shape == (3,3)

    R = np.matmul(R_des, R_curr.T)

    S = (R - R.T) / 2

    assert S[2,1] == -S[1,2]
    assert S[0,2] == -S[2,0]
    assert S[1,0] == -S[0,1]

    omega = np.array([S[2,1], S[0,2], S[1,0]])

    return omega