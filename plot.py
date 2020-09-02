#!/usr/bin/env python3

import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np
import csv

LOGO_IMG = None
RESOLUTION = 300


def add_logo(fig, logopath):
    global LOGO_IMG
    if LOGO_IMG is None:
        LOGO_IMG = image.imread(logopath)
    fig.figimage(LOGO_IMG, 10, 10)


def plot(data, title='No title set', xlabel='No axis label set', logopath=''):
    fig, ax = plt.subplots()
    fig.suptitle(title, fontweight='bold')

    ypos = np.arange(len(data['labels']))
    values = data['values']

    ax.barh(ypos, values, align='center', tick_label=data['labels'])
    ax.set_yticks(ypos)
    ax.invert_yaxis()
    ax.set_xlabel(xlabel)

    ax.set_axisbelow(True)
    ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.4)

    add_logo(fig, logopath=logopath)
    fig.tight_layout()
    matplotlib.pyplot.savefig('plot.png', bbox_inches='tight', format='png', dpi=RESOLUTION)

def parseCSV(filename, delimiter=' ', quotechar='|'):
    labels = []
    values = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in csvreader:
            labels.append(row[0])
            values.append(float(row[1]))
    return {
        'labels': labels,
        'values': values
    }

def main(args):
    data = parseCSV(args.filename, delimiter=args.delimiter, quotechar=args.quotechar)
    plot(data, title=args.title, xlabel=args.xlabel, logopath=args.logopath)
    print('Chart saved in `plot.png`')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot data from csv. First column is the label, second is the value')
    parser.add_argument('filename', help='The CSV file containing the data')
    parser.add_argument('--delimiter', help='Set the delimiter character when parsing the CSV', default=' ')
    parser.add_argument('--quotechar', help='Set the quote character when parsing the CSV', default='|')
    parser.add_argument('--title', help='The title of the chart', default='No title set')
    parser.add_argument('--xlabel', help='The label of the x axis', default='No xlabel set')
    parser.add_argument('--logopath', help='The path of the logo', default='logo.png')

    args = parser.parse_args()

    main(args)
