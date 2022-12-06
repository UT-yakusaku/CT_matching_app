import os

dicom_file_path = './images/DCMfile'
template_file_path = './images/templates'
image_ref = 136
image_length = 138  

dicom_files = sorted(os.listdir(dicom_file_path))
template_files = sorted(os.listdir(template_file_path))
