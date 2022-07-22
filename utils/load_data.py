import logging
import os
import numpy as np
logger = logging.getLogger(__name__)
from glob import glob
from scipy.io.matlab import loadmat
import numpy as np
import pandas as pd
import re

class ABCDDataset: 
    def __init__(self, data_dir):
        self.data_root = data_dir
        self.ds_root   = os.path.join(data_dir, "external", "Julich")
        self.ds_external = os.path.join(data_dir, "external")
        
        
    def list_subjects(self):
        d = os.path.join(self.ds_root)
        return [subj for subj in os.listdir(d) if not subj.startswith(".")]

    
    def load_sc(self, subj, log10=False):
        
        d = os.path.join(self.ds_root)
        
        separator          = ''
        file_julich        = separator.join([d,'/',subj,'/ses-1/SC/',subj,'_SC_Schaefer_7NW100p.txt']) 
        file_julich_no_log = separator.join([d,'/',subj,'/ses-1/SC/',subj,'_SC_Schaefer7NW100p_nolog10.txt']) 
        SC                 = np.loadtxt(file_julich)
        SC_nolog           = np.loadtxt(file_julich_no_log)
        
        if log10:
            return SC
        else:
            return SC_nolog

    #def get_connectivity(self, subject, scaling_factor=124538.470647693):
    #    SC = self.load_sc(subject)
    #    SC = SC / scaling_factor
    #    conn = connectivity.Connectivity(
    #            weights = SC,
    #            tract_lengths=np.ones_like(SC),
    #            centres = np.zeros(np.shape(SC)[0]),
    #            speed = np.r_[np.Inf]
    #    )
    #    conn.compute_region_labels()
    #    logger.warning("Placeholder region names!")
    #    return conn


