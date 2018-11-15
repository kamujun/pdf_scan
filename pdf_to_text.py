import subprocess as sb
import re

input_file = './data/raw_pdf/***.pdf'
output_dir = './data/raw_txt/'
command = ['pdf2txt.py', '-p', '10', '-o', '1.txt', input_file]

command_stdout = ['pdf2txt.py', '-p', '10', input_file]
command_check_file_size = ['find', '1.txt', '-size', '+0']

max_pages = 1000

result_stdout = []

def pdf_to_text():
    for i in range(max_pages):

        # output file
        command[2] = str(i+1)
        command[4] = output_dir + str(i+1) + '.txt'

        # stdout
        # command_stdout[2] = str(i+1)

        # Run
        sb.run(command)

        # Check output file size
        command_check_file_size[1] = output_dir + str(i+1) + '.txt'

        # CAUTION -- 'stdout' parameter is python3.6. Later version need use 'capture_output' option.
        result = sb.run(command_check_file_size, stdout=sb.PIPE)

        # Check output file size by find command.
        if re.search(r"b'(.*)'", str(result)).group(1) == '':
            break

def preprocess():
    path_input = './data/extract_txt/4.txt'
    path_output = './data/preprocess'



    with open(path_input, 'r') as f_in:
        doc = f_in.read()

        print(''.join(doc.replace('\u3000', '').split('\n')))


        # with open(path_output, 'w') as f_out:
        #     f_out.write(doc.replace('\n\n', '\n'))


if __name__ == '__main__':
    # pdf_to_text()

    preprocess()