# Box Plotter
## Program to simplify creating box-and-whisker diagrams.
### Made primarily for Abertay CMP201 DS&Alg

Program is a wrapper around matplotlib and numpy to simplify the creation of numerous box diagrams quickly and easily.
Required arguments are CSV files containing the output data.

Program makes a boxplot out of each line in each file specified, so you could create two boxplots by either specifying a single, multi-line file, or by specifying two files with one line each.

Suggested arguments are `-t` for the graph title, `-x` for the x-axis label and `-y` for the y-axis label at minimum.

Help menu:
```
usage: plotter.py [-h] [-t TITLE] [-x XAXIS] [-y YAXIS] [-l LABELS] [-o OUTFILE] [-d DELIMITER] [-q] [--accessible] files [files ...]

Program to generate box plots based on CSV input files

positional arguments:
  files                 CSV files to plot

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        Set a title for the graph
  -x XAXIS, --xaxis XAXIS
                        Set the x-axis for the graph
  -y YAXIS, --yaxis YAXIS
                        Set the y-axis for the graph
  -l LABELS, --labels LABELS
                        Add labels to the boxplots -- should be placed in a text file, one per line. Specify the filename here. There should be one for each box plot
  -o OUTFILE, --outfile OUTFILE
                        Output results to a PNG file
  -d DELIMITER, --delimiter DELIMITER
                        Input file delimiter (default is ',')
  -q, --quiet           Don't show the output graph (useful with -o)
  --accessible          Activate accessibility mode
```
