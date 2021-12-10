from PIL import Image
from ita_core_computations import format_image_and_get_lab_patches, compute_ita_from_lab


def get_structured_patches_ita_list(image: Image):
    """
    For the structure patches approach the first row, the last row, first column and last column will be
    sampled for the ITA values. When taking the boarder we need ot make sure the corners are not double counted
    """
    patches = format_image_and_get_lab_patches(image)

    selected_ita_values = []

    row_count = len(patches)
    col_count = len(patches[0])

    indices = []
    # First row
    for i, patch in enumerate(patches[0]):
        selected_ita_values.append(compute_ita_from_lab(patch[0]))
        indices.append([0, i])
    # last row
    for i, patch in enumerate(patches[-1]):
        selected_ita_values.append(compute_ita_from_lab(patch[0]))
        indices.append([row_count - 1, i])
    # First column
    # Not index zero and last index is a corner and already accounted for on the rows
    for i in range(1, row_count - 1):
        patch = patches[i][0]
        selected_ita_values.append(compute_ita_from_lab(patch[0]))
        indices.append([i, 0])

    # Last column
    # Not index zero and last index is a corner and already accounted for on the rows
    for i in range(1, row_count - 1):
        patch = patches[i][-1]
        selected_ita_values.append(compute_ita_from_lab(patch[0]))
        indices.append([i, col_count - 1])

    return selected_ita_values, indices