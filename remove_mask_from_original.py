import nibabel as nib
import numpy as np

# Load the original MRI image
original_image = nib.load('/Users/jorgetapias/Desktop/MRA_DL/skull_stripping_code_SR/brains/BG0002.nii.gz')

# Load the mask
mask = nib.load('/Users/jorgetapias/Desktop/MRA_DL/output/BG0002_mask.nii.gz')

# Extract the ROI by applying the mask
roi_data = original_image.get_fdata() * mask.get_fdata()

# Create a new NIfTI image
roi_nifti = nib.Nifti1Image(roi_data, original_image.affine)

# Save the new NIfTI image with the ROI
nib.save(roi_nifti, 'roi_BETHD_image.nii')