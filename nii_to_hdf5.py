import nibabel as nib
import numpy as np 
import h5py
import os
import glob

input_path = "/Users/armaantewary/development/mra_sample_images/"
output_path = "/Users/armaantewary/development/mra_sample_images/outputs"

def convert_nii_to_hdf5(nii_file_path, output_folder):
    # Load the NIfTI file
    nii_image = nib.load(nii_file_path)
    image_data = nii_image.get_fdata()

    # Convert to a regular NumPy array
    regular_array = np.array(image_data)

    # Filename for the HDF5 file
    hdf5_filename = os.path.join(output_folder, os.path.basename(nii_file_path) + '.hdf5')

    # Create an HDF5 file in the specified output folder
    with h5py.File(hdf5_filename, 'w') as f:
        # Create a dataset in the file
        dset = f.create_dataset("init", data=regular_array)

    print(f"File saved as {hdf5_filename}")
    print(type(regular_array))
    print(type(dset))

for nii_file_path in glob.glob(input_path + '/*.nii'):
    convert_nii_to_hdf5(nii_file_path, output_path)

