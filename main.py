import os
import cv2
import numpy as np
import scipy.io as sio


def get_keypoints(input_folder, fname, output_folder):
    # Prepare filenames
    impath = os.path.join(input_folder, fname)
    base_name = os.path.splitext(fname)[0]
    outim_path = os.path.join(output_folder, fname)
    outkp_path = os.path.join(output_folder, f"{base_name}.mat")

    # Load image
    im = cv2.imread(impath)
    imrgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    # Initiate SIFT detector
    sift = cv2.SIFT_create()

    # Find the keypoints and descriptors with SIFT
    kp, des = sift.detectAndCompute(imrgb, None)
    for k in kp:
        cx, cy = int(k.pt[0]), int(k.pt[1])
        cv2.circle(im, (cx, cy), 2, (0, 0, 255), -1)
    cv2.imwrite(outim_path, im)

    combined = np.concatenate((np.array([k.pt for k in kp], dtype=np.float32).T, des.T), axis=0)
    sio.savemat(outkp_path, {'kp': combined})


def process_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Supported image extensions
    exts = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    # Iterate over all images in folder
    for fname in os.listdir(input_folder):
        if fname.lower().endswith(exts):
            try:
                combined = get_keypoints(input_folder, fname, output_folder)
            except Exception as e:
                print(f"Failed to process {fname}: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run SIFT keypoint extraction on all images in a folder.")
    parser.add_argument("--input_folder", default="images", help="Path to folder containing images")
    parser.add_argument("--output_folder", default="output", help="Folder to save .mat files (default: ./output)")

    args = parser.parse_args()

    process_folder(args.input_folder, args.output_folder)