import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python bond_html.py hoge.html -o hoge_out.html")
        sys.exit()

    target_file = open(sys.argv[1], 'r')
    target_txt = target_file.read()
    target_file.close()

    i = 0
    output_txt = ''
    while True:
        index = target_txt.find('#BOND_HTML(\"', i)
        if index == -1:
            output_txt += target_txt[i:]
            break
        output_txt += target_txt[i:index]

        index_of_end_of_filename = target_txt.find('\")', index)
        if index_of_end_of_filename == -1:
            print("Error! There is not \".")
            sys.exit()
            break

        filename = target_txt[index + 12:index_of_end_of_filename]
#        for i in range(index_of_end_of_filename - index - 1):
#            filename += target_txt[i + index + 1]

        bonded_file = open(filename, 'r')
        bonded_text = bonded_file.read()
        bonded_file.close()

        output_txt += bonded_text

        i = index_of_end_of_filename + 2

    output_file = open(sys.argv[3], "w")
    output_file.write(output_txt)
    output_file.close()
