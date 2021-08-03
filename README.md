# debayer_bonito

This is a python script to perform debayering for images recorded with Bonito camera model using opencv functions. 

## Usage

python debayer.py -h  
Parsing command line...  
usage: debayer.py [-h] -i I -o O [-e E]

Demosaic frames from Bonito camera. Either provide a single file, or a  
directory as input. If a directory is given, all files within the directory  
with the target extension will be processed. Output files are then stored in  
the same folder as input with a _debayer suffix.  

arguments:  
  * -h, --help  show this help message and exit
  * -i I        input image file
  * -o O        output image file
  * -e E        input file extension
