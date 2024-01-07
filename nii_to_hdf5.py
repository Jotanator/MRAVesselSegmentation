import nibabel as nib
import numpy as np 
import h5py
import os
import glob

base_path = "/Users/armaantewary/development/trial_mra_dataset"
output_path = base_path + "/outputs"

def convert_all_nii_to_hdf5(base_nii_file_path, output_folder):
    # Load the raw and label NIfTI files

    raw_nii_file_path = base_nii_file_path + "/raw"
    label_nii_file_path = base_nii_file_path + "/label/"

    for raw_img_file_path in glob.glob(raw_nii_file_path + '/*.nii'):
        print(f'Raw image path {raw_img_file_path}')

        file_name_with_extension = os.path.basename(raw_img_file_path)
        file_name_without_extension, _ = os.path.splitext(file_name_with_extension)
        
        label_img_file_path = label_nii_file_path + file_name_without_extension + "_mask.nii"
        print(f'Raw label_img_file_path {label_img_file_path}')

        raw_image = nib.load(raw_img_file_path)
        label_image = nib.load(label_img_file_path)

        raw_data = raw_image.get_fdata()
        label_data = label_image.get_fdata()

        raw_array = np.array(raw_data)
        label_array = np.array(label_data)


    # Filename for the HDF5 file
        hdf5_filename = os.path.join(output_folder, os.path.basename(file_name_without_extension) + '.hdf5')

    # Create an HDF5 file in the specified output folder
        with h5py.File(hdf5_filename, 'w') as f:
        # Create datasets in the file
            f.create_dataset("raw", data=raw_array)
            f.create_dataset("label", data=label_array)

        print(f"File saved as {hdf5_filename}")

convert_all_nii_to_hdf5(base_path, output_path)
