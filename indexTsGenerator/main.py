import os
import re as rgx


output = ""
outputFile = open("index.ts", "w")

for fileName in os.listdir():
    if rgx.search("^(?!index).*\.tsx?$", fileName) != None:
        newFileName = rgx.split(".tsx?$", fileName)[0]
        output += "export { default as " + newFileName + \
            " } from \"./" + newFileName + "\";\n"

outputFile.write(output)
outputFile.close()

print("success")
