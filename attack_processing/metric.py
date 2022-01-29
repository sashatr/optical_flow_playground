import os
import argparse
import cv2
import numpy as np
import torch
import torch.nn.functional as F



def images_dir_to_tensor(path):
    # TODO: remove patch value from loss
    flow_names = os.listdir(path)
    flow_arr = np.array([cv2.imread(f"{path}/{img_name}") for img_name in flow_names])
    return torch.from_numpy(flow_arr)


def process(args):
    flow_origin_tensor = images_dir_to_tensor(args.flow_origin).float()
    flow_attacked_tensor = images_dir_to_tensor(args.flow_attacked).float()

    loss = F.mse_loss(flow_origin_tensor, flow_attacked_tensor)
    print(loss)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--flow_origin', help="restore checkpoint")
    parser.add_argument('--flow_attacked', help="restore checkpoint")

    args = parser.parse_args()

    process(args)
