#!/usr/local/bin/python3

import cgi,json
import os


def main():
    print("Content-Type: application/json\n\n")

    # form = cgi.FieldStorage()
    # counts_file = form.getvalue('raw_counts_csv')
    # counts_file = './Resources/'+counts_file
    # design_file = form.getvalue('design_file_csv')
    # design_file = './Resources/'+design_file
    # design = str(form.getvalue('study_design_factor'))
    # control = str(form.getvalue('control_group_subfactor'))
    # exp = str(form.getvalue('exp_group_subfactor'))


    # print([counts_file, design_file, design, control, exp])
    print(json.dumps(output_results))

if __name__ == '__main__':
    main()