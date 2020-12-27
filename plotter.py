#!/usr/bin/python3
#Box Plotter
#Wrapper around Matplotlib and Numpy for easy generation of box-and-whisker diagrams -- mainly designed to make graphing in Abertay CMP201 quick and easy
#AG | MuirlandOracle
#12/20

#### Imports ####
import sys, warnings, os, argparse, csv, matplotlib as mpl, numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

class Graph():
	def __init__(self):
		self.colours = self.Colours(self)
		self.data = [] 
		self.labels = False
	

	#### Handle Colour operations ####
	class Colours():
		red = "\033[91m"
		green = "\033[92m"
		blue = "\033[34m"
		orange = "\033[33m"
		purple = "\033[35m"
		end = "\033[0m"

		def __init__(self, outer):
			self.parent = outer

		def print(self, msgType, text, die=True):
			if msgType == "fail":
				if not self.parent.args.accessible:
					print(f"{self.red}[-] {text}{self.end}")
				else:
					print(f"Failure: {text}")
				if die:
					sys.exit(0)
			elif msgType == "success":
				if not self.parent.args.accessible:
					print(f"{self.green}[+] {text}{self.end}")
				else:
					print(f"Success: {text}")
			elif msgType == "warn":
				if not self.parent.args.accessible:
					print(f"{self.orange}[*] {text}{self.end}")
				else:
					print(f"Warning: {text}")
			elif msgType == "info":
				if not self.parent.args.accessible:
					print(f"{self.blue}[*] {text}{self.end}")
				else:
					print(f"Info: {text}")
			else:
				raise ValueError("Invalid colour function selected")

	#### Parse CLI Arguments ####
	def parse(self):
		parser = argparse.ArgumentParser(description="Program to generate box plots based on CSV input files")
		parser.add_argument("files", help="CSV files to plot", nargs="+")
		parser.add_argument("-t", "--title", default="Graph", help="Set a title for the graph")
		parser.add_argument("-x", "--xaxis", default="X-Axis", help="Set the x-axis for the graph")
		parser.add_argument("-y", "--yaxis", default="Y-Axis", help="Set the y-axis for the graph")
		parser.add_argument("-l", "--labels", default=False, help="Add labels to the boxplots -- should be placed in a text file, one per line. Specify the filename here. There should be one for each box plot")
		parser.add_argument("-o", "--outfile", default=False, help="Output results to a PNG file")
		parser.add_argument("-d", "--delimiter", default=",", help="Input file delimiter (default is ',')")
		parser.add_argument("-q", "--quiet", default=False, action="store_true", help="Don't show the output graph (useful with -o)")
		parser.add_argument("--accessible", default=False, action="store_true", help="Activate accessibility mode")
		self.args = parser.parse_args()

		for i in self.args.files:
			if not os.path.exists(i):
				self.colours.print("fail", f"File: {i} does not exist")
			else:
				try:
					with open(i) as csvfile:
						data = list(csv.reader(csvfile, delimiter=self.args.delimiter, quoting=csv.QUOTE_NONNUMERIC))
						for i in data:
							while "" in i:
								i.remove("")
							self.data.append(i)
				except ValueError:
					self.colours.print("fail", f"File: {i} contains non-numeric characters")

		if self.args.labels:
			if not os.path.exists(self.args.labels):
				self.colours.print("fail", f"Label file ({self.args.labels}) does not exist")

			with open(self.args.labels) as labelFile:
				self.labels = [i.strip("\n") for i in labelFile.readlines()]

			if len(self.labels) != len(self.data):
				self.colours.print("fail", f"Number of labels does not match the number of boxplots")



	
	def plot(self):
		fig, ax = plt.subplots()
		ax.set_title(self.args.title)
		ax.set_xlabel(self.args.xaxis)
		ax.set_ylabel(self.args.yaxis)
		
		if self.labels:
			ax.set_xticklabels(self.labels)
		
		ax.boxplot(self.data)
		if not self.args.quiet:
			plt.show()
		if(self.args.outfile):
			mpl.use("agg")
			fig.savefig(self.args.outfile, bbox_inches='tight')	

if __name__ == "__main__":
	graph = Graph()
	graph.parse()
	graph.plot()
