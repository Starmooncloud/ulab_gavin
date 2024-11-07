#File name: Lagrangian
import numpy as np

def findForces(potentialEnergy):
    """
    Calculates potential function based off of Potential Energy

    Parameter: potentialEnergy -  a function of potential energy
    #Output: Based off formula -del(V) = F, we can calculate the forces
    """
    potentialEnergy = np.array(potentialEnergy)
    fx = np.gradient(potentialEnergy)  
    fy = np.gradient(potentialEnergy)  
    fz = np.gradient(potentialEnergy)  

    force_array = np.array([fx, fy, fz]).T  # Combine into a 3D gradient matrix

    return force_array

def findKineticEnergy(mass, velocity):
    """
    Calculates kinetic energies based off of list of masses and velocityies

    Parameter: mass - list of masses of each object
               velocity - instantenous velocities of each object
    #Output: Based off formula K = 1/2 mv^2, we can calculate kinetic energy
    """
    K = []
    for i in range(0, len(mass)):
        if i < len(velocity):
            K.append(0)
            K[i] += (1/2 * mass[i] * velocity[i] ** 2)
    return K
    

def findLagrangian(velocity, mass, potentialEnergy):
    """
    Calculates Lagrangian function based off of mass, velocity, and potentialEnergy of the on objecct

    Parameter: nass -  mass of the object
               velocity - instantenous velocity of the object
               potentialEnergy - potential energy of the object
    #Output: Based off formula L = K - U, we can find Lagrangian
    """
    L = []
    for i in range(0, len(mass)):
        L.append(0)
        L[i] += (findKineticEnergy(mass, velocity)[i] - potentialEnergy)
    return L

