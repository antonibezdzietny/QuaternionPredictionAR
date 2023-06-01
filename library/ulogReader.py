"""
Module 
"""

import numpy as np
import quaternion as qt

from pyulog import ULog



def readAttitude(ulog: ULog):
    """
    Function extract vehicle attitude from ulogs to quaternion.

    Args:
        ulg (pyulog.ULog): PyUlog object to read

    Returns:
        attitude (np.array(qt.quaternion)): Array of quaternions value (n,)
        timestamp (np.array): Array of timestamp (n,)
    """
    
    att_logs = ulog.get_dataset('vehicle_attitude') # Get vehicle_attitude dataset
    n_logs   = att_logs.data['q[0]'].shape[0] # N_logs
    att_quat  = np.zeros((n_logs,4)) # Allocate memory

    att_quat[:,0] = att_logs.data['q[0]']
    att_quat[:,1] = att_logs.data['q[1]']
    att_quat[:,2] = att_logs.data['q[2]']
    att_quat[:,3] = att_logs.data['q[3]']

    return qt.from_float_array(att_quat), att_logs.data['timestamp']


def readNavigator(ulg: ULog):
    """
    Read navigator signal from ulg file as euler angles in radians `(Roll, Pitch,  Yaw)`.
    Args:
        ulg (pyulog.ULog): PyUlog object to read.

    Returns:
        nav_euler (np.ndarray): Array of euler value (n, 3)
        time_stamp (np.array): Array of timestamp (n,)
    """   
    pass