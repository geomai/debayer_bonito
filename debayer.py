# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:37:42 2016

@author: ma
"""

import cv2
import argparse
import os
import glob

# constant color correction factors
color_factors = [1.14, 0.95, 1.3]

def demosaic(im, mode = cv2.COLOR_BayerGB2BGR):
    new_im = cv2.cvtColor(im, mode)
    
    b, g, r = cv2.split(new_im)
    b = b * color_factors[0]
    g = g * color_factors[1]
    r = r * color_factors[2]
    
    return cv2.merge((b, g, r))

def demosaic_file(f_input, f_output, ext):
    if os.path.isdir(f_input):
        files = glob.glob(f_input + '/*.' + ext)

        for file in files:
            file = file.replace('\\', '/')
            print('Processing ' + file + '...')
            im = cv2.imread(file, 0)
            converted = demosaic(im)
            output_file = file.replace('.' + ext, '_debayer.png')
            print('Writing ' + output_file + '...')
            cv2.imwrite(output_file, converted)
        
    else:
        im = cv2.imread(f_input, 0)
        converted = demosaic(im)
        cv2.imwrite(f_output, converted)

def main():
    print('Parsing command line...')
    parser = argparse.ArgumentParser(description="""Demosaic frames from Bonito camera.
        Either provide a single file, or a directory as input.
        If a directory is given, all files within the directory with the target extension will be processed.
        Output files are then stored in the same folder as input with a _debayer suffix.""")

    parser.add_argument('-i', type=str, help='input image file', required=True)
    parser.add_argument('-o', type=str, help='output image file', required=True)
    parser.add_argument('-e', type=str, help='input file extension', required=False, default='png')
    
    args = parser.parse_args()
    
    print('Input file: ' + args.i) 
    print('Output file: ' + args.o)
    print('Input file extension: ' + args.e)
    print('Processing...')
    
    demosaic_file(args.i, args.o, args.e)    
    
    print('Done.')    


if __name__ == "__main__":
    main()  