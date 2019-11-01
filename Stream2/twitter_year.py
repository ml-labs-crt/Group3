import subprocess

with open("keywords.txt", "r") as text: 
        keywords = [] 
        for line in text:
            line = line.split("\n")[0]
            #keywords.append(line)
            keywords.append(line.lower())
            #keywords.append(line.upper())

for word in keywords:
	location = "53.058004,-8.110000"
	radius = "200km"
	language = "en"
	print(word)
	bashCommand = "python Exporter.py --querysearch "+"\""+word+"\""+" --near "+"\""+location+"\""+" --within "+"\""+radius+"\""+" --since 2018-10-01 --until 2019-10-01 --maxtweets 0 --lang "+"\""+language+"\""
	move = "mv output_got.csv Datasets/"+word+".csv"
	print(bashCommand)

	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	process2 = subprocess.Popen(move.split(), stdout=subprocess.PIPE)
	output2, error2 = process2.communicate()