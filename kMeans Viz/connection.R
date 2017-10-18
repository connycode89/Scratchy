library(PythonInR)

# connect to Python
conn1 <- pyConnect(pythonExePath = "C:\\Anaconda2\\envs\\tensorflow\\python.exe")
pyIsConnected()
#pyExit()
lines <- readLines("C:\\MyWorkingFolder\\Github Repositories\\Scratchy\\kMeans Clustering.py",encoding="UTF-8")
typeof(str(lines))

lines2 <- ""
for (num in seq(1,length(lines)))
{lines2 <- paste(lines2, lines[num], sep="\n")}

pyExecg(lines2)