import os
import argparse
import cv2


def process(args):
    image_names = os.listdir(args.imgs_i)

    for img_name in image_names:
        img = cv2.imread(f"{args.imgs_i}/{img_name}")

        patch = cv2.imread(args.patch_path)
        img[
            args.patch_y_offset:args.patch_y_offset+patch.shape[0], 
            args.patch_x_offset:args.patch_x_offset+patch.shape[1]
        ] = patch

        cv2.imwrite(f"{args.imgs_o}/{img_name}", img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgs_i', help="restore checkpoint")
    parser.add_argument('--imgs_o', help="restore checkpoint")
    parser.add_argument('--patch_path', help="restore checkpoint")

    parser.add_argument('--patch_x_offset', help="restore checkpoint", default=500)
    parser.add_argument('--patch_y_offset', help="restore checkpoint", default=300)

    args = parser.parse_args()

    process(args)
