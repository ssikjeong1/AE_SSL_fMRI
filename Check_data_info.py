import os
import nibabel as nib
import numpy as np
import glob
from nilearn.connectome import ConnectivityMeasure
import natsort
import deepdish as ddish
""" For make phenotype summary in Journal """
print('Pause')
SITE = ["Caltech", "CMU", "KKI", "Leuven_1", "Leuven_2",
        "MaxMun", "NYU", "OHSU", "Olin", "Pitt", "SBL", "SDSU", "Stanford",
        "Trinity", "UCLA_1", "UCLA_2", "UM_1", "UM_2", "USM", "Yale"]

for tmp_site in list(SITE):
    file_dir = os.getcwd()+'/Processed_data'
    tmp_file_dir = glob.glob(os.path.join(file_dir,'orig/{}_*_ori.h5').format(tmp_site))[0]

    tmp_file = ddish.io.load(tmp_file_dir)
    print('{}:'.format(tmp_site), len(tmp_file['gender']))
    print('ASD', (tmp_file['label']==1).sum())
    print('Male', (tmp_file['gender'][(tmp_file['label']==1)]==1).sum())
    print('Female', (tmp_file['gender'][(tmp_file['label']==1)]==2).sum())
    print('Age (mean): {:.1f}'.format((tmp_file['age'][(tmp_file['label'] == 1)]).mean()))
    print('Age (std), {:.1f}'.format((tmp_file['age'][(tmp_file['label'] == 1)]).std()))
    print('TC', (tmp_file['label']==0).sum())
    print('Male', (tmp_file['gender'][(tmp_file['label'] == 0)] == 1).sum())
    print('Female', (tmp_file['gender'][(tmp_file['label'] == 0)] == 2).sum())
    print('Age (mean): {:.1f}'.format((tmp_file['age'][(tmp_file['label'] == 0)]).mean()))
    print('Age (std), {:.1f}'.format((tmp_file['age'][(tmp_file['label'] == 0)]).std()))
    print('='*10)
