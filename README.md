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

### Examples:
Both results from one file:
```
./plotter.py results.csv -t "My Graph" -x Algorithm -y "Time (m/s)" -l labelFile.txt
```
Results from separate files:
```
./plotter.py results1.csv results2.csv -t "My Graph" -x Algorithm -y "Time (m/s)" -l labelFile.txt
```

The plotter will create a new entry for each new line it receives -- this includes across numerous files.
For example, if `results.csv` looks like this:
```
2,3,4,5
6,7,8,9
```
Then two boxes will be plotted, one for each line.

If the same input is given in two files:
results1.csv
```
2,3,4,5
```
results2.csv
```
6,7,8,9
```
This will result in the same result as before.

**Note:** If labels for the x-axis are provided then they must be provided one per line, with the number of labels matching up with the number of results to be plotted (e.g. two boxes must have two labels provided, etc).
