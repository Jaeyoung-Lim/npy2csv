import numpy as np
import pandas as pd

import argparse


def start_conversion(path, output_path):
    data = np.load(path, allow_pickle=True)
    df = pd.DataFrame.from_dict(data.item())
    df.to_csv(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert npy files to csv')
    parser.add_argument('path', metavar='path', type=str, help='Path to .npy files')
    parser.add_argument('--output-path', metavar='output-path', type=str, help='Path to output .csv file', default='data.csv')
    arg_list = parser.parse_args()
    start_conversion(**vars(arg_list))