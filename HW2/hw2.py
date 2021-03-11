import os
import re
import socket

txt_files = []
word_count = 0
txt_dir = "/home/data"
file_words = {}

def get_word_count(fname):
    f = open(os.path.join(txt_dir, fname), "r")
    contents = f.read()
    f_word_count = len(re.findall(r'\w+', contents))
    file_words[fname] = f_word_count
    return f_word_count


def get_file_w_most_words():
    max_words = None
    max_file = None

    for k, v in file_words.items():
        if ((not max_words) or (v > max_words)):
            max_file = k
            max_words = v

    return [max_file, max_words]


def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(('10.255.255.255', 1))
        ip_addr = s.getsockname()[0]
    except Exception:
        ip_addr = '127.0.0.1'
    return ip_addr


def print_results_file(fname='result.txt'):
    f = open(fname, 'r')
    print(f.read())


if __name__ == "__main__":
    for f in os.listdir(txt_dir):
        if f.endswith(".txt"):
            txt_files.append(f)

            word_count += get_word_count(f)

    out = open('result.txt', 'w')

    out.write('File names:\n')
    [out.write('{}\n'.format(i)) for i in txt_files]
    out.write('\n')

    out.write('Total word count: {}\n'.format(word_count))

    max_file, max_words = get_file_w_most_words()
    out.write('File with the most words: {} with {} words\n'.format(max_file, max_words))
    out.write('\n')

    ip = get_ip_addr()
    out.write('IP address of this machine: {}'.format(ip))

    out.close()

    print_results_file()

