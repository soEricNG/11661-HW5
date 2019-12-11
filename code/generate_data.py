import os
import argparse


def eighty_twenty_split(input_filename, output_path):
    filename = os.path.splitext(os.path.basename(input_filename))[0]
    all_lines = [line for line in open(input_filename, 'r')]
    total_len = len(all_lines)
    num_lines_in_train = round(total_len * 0.8)
    # generate train data
    train_filename = f'{output_path}/{filename}_train.txt'
    test_filename = f'{output_path}/{filename}_test.txt'

    train_f = open(train_filename, 'w+')
    test_f = open(test_filename, 'w+')
    for i, line in enumerate(all_lines):
        if i < num_lines_in_train:
            train_f.write(line)
        else:
            test_f.write(line)
    train_f.close()
    test_f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate training and test data')
    parser.add_argument('--input_dir', type=str, required=True, help='Input directory')
    parser.add_argument('--output_dir', type=str, required=True, help='Output directory')
    parser.add_argument('--method', type=int, default=0, help='0 for 80/20 split, 1 for random regeneration')
    args = parser.parse_args()
    method = args.method
    input_path = args.input_dir
    for file in os.listdir(input_path):
        if method == 0:  # 80/20 split
            eighty_twenty_split(f'{input_path}/{file}', args.output_dir)
        elif method == 1:
            pass
        else:
            raise Exception('Illegal method!')
