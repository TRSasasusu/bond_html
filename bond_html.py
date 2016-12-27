# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python bond_html.py hoge.html -o hoge_out.html")
        sys.exit()

    target_file = open(sys.argv[1], 'r', encoding='utf-8')
    target_txt = target_file.read()
    target_file.close()

    output_txt = target_txt
    #for m in re.finditer(r'#BOND_HTML\((.*)\)$', output_txt, re.MULTILINE):
    while True:
        m = re.search(r'#BOND_HTML\((.*)\)$', output_txt, re.MULTILINE)
        if m is None:
            break

        bond_elements = m.groups()[0].split(',')
        bonded_file = open(bond_elements[0].replace("\"", ""), 'r', encoding='utf-8')
        bonded_text = bonded_file.read()
        bonded_file.close()

        for i in range(1, len(bond_elements) // 2 + 1):
            former = bond_elements[i * 2 - 1].replace(' ', '')
            latter = re.search(r' *"(.*)"', bond_elements[i * 2], re.MULTILINE).groups()[0]
            if former[0] == '$':
                bonded_text = bonded_text.replace(former, latter)
            else:
                splited_text = bonded_text.split('\n')
                splited_text[int(former) - 1] = latter
                bonded_text = '\n'.join(splited_text)

        bonded_text = re.sub(r'\${.*}', '', bonded_text)
        output_txt = output_txt[:m.start()] + bonded_text + output_txt[m.end():]

    output_file = open(sys.argv[3], "w", encoding='utf-8')
    output_file.write(output_txt)
    output_file.close()

