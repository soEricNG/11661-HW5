import os
import argparse
import spacy
import lorem
from lorem.text import TextLorem
NUM_SENTENCES_PER_FILE = 2000


def generate_train_random(output_path):
    filename = 'lorem'
    # lorem = TextLorem(srange=(2, 3), words="A B C D E F".split())
    for file_count in range(6,11):
        with open(f'{output_path}/{filename}_{file_count}', 'w+') as f_out:
            for _ in range(NUM_SENTENCES_PER_FILE):
                f_out.write(lorem.sentence()+'\n')


def generate_train_from_english_corpus(input_filename, output_path):
    nlp = spacy.load("en_core_web_sm")
    filename = os.path.splitext(os.path.basename(input_filename))[0]
    line = 0
    file_count = 1
    f_out = open(f'{output_path}/{filename}_{file_count}', 'w+')
    with open(input_filename, 'r') as f:
        data = f.read().replace('\n', '')
        doc = nlp(data)
        for sent in list(doc.sents):
            # if len(sent) < 5:
            #     continue
            if line >= NUM_SENTENCES_PER_FILE:
                f_out.close()
                line = 0
                file_count += 1
                f_out = open(f'{output_path}/{filename}_{file_count}', 'w+')
            f_out.write(f'{sent.text}\n')
            line += 1
        if line >= NUM_SENTENCES_PER_FILE:
            f_out.close()


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
    # generate_train('','')
    generate_train_random('data/train')
    # parser = argparse.ArgumentParser(description='Generate training and test data')
    # parser.add_argument('--input_dir', type=str, required=True, help='Input directory')
    # parser.add_argument('--output_dir', type=str, required=True, help='Output directory')
    # parser.add_argument('--method', type=int, default=0, help='0 for 80/20 split, 1 for random regeneration')
    # args = parser.parse_args()
    # method = args.method
    # input_path = args.input_dir
    # for file in os.listdir(input_path):
    #     input_filename = f'{input_path}/{file}'
    #     output_path = args.output_dir
    #     if method == 0:  # 80/20 split
    #         eighty_twenty_split(input_filename, output_path)
    #     elif method == 1:
    #         pass
    #     elif method == 2:
    #         generate_train_from_english_corpus(input_filename, output_path)
    #     else:
    #         raise Exception('Illegal method!')
