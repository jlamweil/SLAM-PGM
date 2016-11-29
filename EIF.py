import numpy as np
from numpy import dot

#Information matrix H_t
# TODO : Initialize ?
infoMatrix = np.array()

# Information vector b_t
#TODO : initialize ?
infoVector = np.array()

# Observed yi


#sensorMeasure = z_t
def updateInformation(infoMatrix, infoVector):
    #N = number of known landmarks

    # hGrad = C_t
    hGrad = np.zeros(N + 1)
    hGrad[0] = #dh/dx -> h(xt) - h(xt-1)/xt-xt-1 ???
    hGrad[i] = #dh/dyi
    identity = np.eye(N + 1)

    #TODO: soft code
    Sx = np.zeros(3 + N * 2)
    Sx[:3,:3] = np.eye(3)

    # g motion model, a vector-valued function which is non-zero only for the robot pose
    # coordinates, as feature locations are static in SLAM
    #gGrad = A_t
    gGrad = np.zeros(N + 1)
    gGrad[0] =


    covariance = np.inv(infoMatrix)

    infoVectorBar = dot(dot(identity + gGrad, covariance), (identity + gGrad).T) + dot(dot(Sx,Ut),Sx.T)
    infoVectorBar = np.inv(infoVectorBar)

    zInvC = dot(np.inv(Z), hGrad.T)
    newInfoMatrix = infoMatrixBar +  dot(hGrad,zInvC)
    newInfoVector = infoVectorBar +  dot(sensorMeasure - h(mu) + dot(hGrad.T, mu.T) ,zInvC)
    return(newInfoMatrix, newInfoVector)
