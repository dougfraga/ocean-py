"""
Run daily operational simumation with MOHID Water Modeling System
Autor: Douglas Fraga Rodrigues
"""
import os
import datetime
from pathlib import Path
from mohid_ops import mohid_postprocessing

###############################################################################
# Define working folder
###############################################################################
BASE_DIR = Path(__file__).resolve().parent

storage_dir = os.path.join(BASE_DIR / 'nc')
boundary_dir = os.path.join(BASE_DIR / 'bc_hdf5')

###############################################################################
# Define simulation dates
###############################################################################
today = datetime.datetime.today()
start_date = today.strftime('%Y-%m-%d')
today_date = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
end_date = (today + datetime.timedelta(days=2)).strftime('%Y-%m-%d')


###############################################################################
# Create surface current maps
###############################################################################
#mohid_postprocessing.surface_current_map(BASE_DIR,today_date)
#print(u'Criação das figuras bem sucedida!')


###############################################################################
# Create json files
###############################################################################
mohid_postprocessing.json_files(BASE_DIR,today_date)
print(u'Criação dos arquivso JSON bem sucedida!')


###############################################################################
# Upload figures
###############################################################################   
#mohid_postprocessing.update_website(BASE_DIR, 'pass.txt')
#print(u'Figuras atualizadas com sucesso!')

