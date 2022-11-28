import pandas
import argparse
import numpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='adj_converter',
        description='Converts an xlsx with an adjacency diagram to a proper adjacency matrix',
        epilog='')
    parser.add_argument('file_in')
    parser.add_argument('file_out')
    args = parser.parse_args()
    file_path = args.file_in
    excel_contents = pandas.read_excel(file_path)
    excel_table = excel_contents.values
    dim = excel_table.shape[0] +1
    matrix = numpy.empty(shape=(dim, dim),dtype=object)

    for i in range(dim-1):
        for j in range(dim-1):
            if j == i:
                matrix[i][j] = 'self'
            elif j > i:
                # in the top-right part
                matrix[j][i] = round(excel_table[i][j+1])
            else:
                # in the bottom-left part
                matrix[j][i] = round(excel_table[j][i+1])
    matrix = numpy.delete(matrix, -1, axis=1)
    matrix = numpy.delete(matrix, -1, axis=0)
    pandas.DataFrame(matrix).to_csv(args.file_out, header=None, index=None)
