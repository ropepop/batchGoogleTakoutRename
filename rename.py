# // rename the initial files to the new names
   

from dataclasses import dataclass
import os
import re
from shlex import join
import time
from typing import List

path = input("Enter the path to the directory: ")

# Validate the user's input
if not os.path.exists(path):
    print("The directory does not exist.")
    exit()
    
files = os.listdir(path)
listoffiles = []
bareFileNames = []
totalLengthOfFileName: List[int] = []


amountOfSymbolsBeforeDuplicateNumber: List[int] = []
amountOfSymbolsBeforeDuplicateNumberEnd: List[int] = []
amountOfSymbolsFromTheEndOfStringTillTheEndOfDuplicateNumberEnd: List[int] = []
lengthOfDuplicateNumber: List[int] = []

amountOfSymbolsBeforeFileExtension: List[int] = []
amountOfSymbolsBeforeFileExtensionEnd: List[int] = []
amountOfSymbolsFromTheEndOfStringTillTheEndOfFileExtensionEnd: List[int] = []
lengthOfFileExtension: List[int] = []

amountOfSyombolsBeforeDotInBareName: List[int] = []
justBareName = []

duplicateNumber: List[int] = []
fileExtension: List[str] = []

newName: List[str]= []

# print('printing all files in program')
# for filename in os.listdir(path):
#     print(filename)
    

print('printing all files in program with .json extension')
for i, filename in enumerate(files):
    if filename.endswith(').json'):
        bareFileNames.append(filename)
        listoffiles.append(path + filename)
        totalLengthOfFileName.append(len(filename + path))
        # print(f'{totalLengthOfFileName[i]}')
        # print(f'{listoffiles[i]}')
        # print(f'{bareFileNames[i]}')
       

    
pattern = r"^(.*?)\("
patternEnd = r"^(.*?)\)"

for files in listoffiles:
    match = re.search(pattern, files)
    num_symbols = len(match.group(1))+1
    print(f"The number of symbols before the duplicate number is: {num_symbols}")
    amountOfSymbolsBeforeDuplicateNumber.append(num_symbols)
    matchEnd = re.search(patternEnd, files)
    num_symbolsEnd = len(matchEnd.group(1))
    print(f"The number of symbols with the duplicate number is: {num_symbolsEnd}")
    amountOfSymbolsBeforeDuplicateNumberEnd.append(num_symbolsEnd)
    

for i, item in enumerate(listoffiles):
    lengthOfDuplicateNumber.append([amountOfSymbolsBeforeDuplicateNumberEnd[i] - amountOfSymbolsBeforeDuplicateNumber[i]])
    print(f'Length of duplicate number inside the {item} is {lengthOfDuplicateNumber[i]}')

for i, item in enumerate(listoffiles):
    amountOfSymbolsFromTheEndOfStringTillTheEndOfDuplicateNumberEnd.append([totalLengthOfFileName[i] - amountOfSymbolsBeforeDuplicateNumberEnd[i]])
    print(f'Amount of symbols from the end of the string till the end of the duplicate number inside the {item} is {amountOfSymbolsFromTheEndOfStringTillTheEndOfDuplicateNumberEnd[i]}')
    
for i, item in enumerate(listoffiles):
    duplicateNumber.append([item[amountOfSymbolsBeforeDuplicateNumber[i]:amountOfSymbolsBeforeDuplicateNumberEnd[i]]])
    print(f'duplicate number inside the {item} is {duplicateNumber[i]}')
    
print('SPLITTING THE FILE EXTENSION')
    
patternFirstDot = r"\."
patternOpeningBracket = pattern

for i, files in enumerate(listoffiles):
    matchFirstDot = re.search(patternFirstDot, files)
    num_symbolsFirstDot = matchFirstDot.end()
    print(f"The number of symbols before the file extension is: {num_symbolsFirstDot}")
    amountOfSymbolsBeforeFileExtension.append(num_symbolsFirstDot)
    matchOpeningBracket = re.search(patternOpeningBracket, files)
    num_OpeningBracket = matchOpeningBracket.end() - 1
    print(f"The number of symbols with the file extension is: {num_OpeningBracket}")
    amountOfSymbolsBeforeFileExtensionEnd.append(num_OpeningBracket)
    
for i, item in enumerate(listoffiles):
     calculatingLengthOfFileExtension = amountOfSymbolsBeforeFileExtensionEnd[i] - amountOfSymbolsBeforeFileExtension[i]
     print(f'Length of file extension inside the {item} is {calculatingLengthOfFileExtension}')
     lengthOfFileExtension.append(calculatingLengthOfFileExtension)
        
for i, item in enumerate(listoffiles):
    amountOfSymbolsFromTheEndOfStringTillTheEndOfFileExtensionEnd.append([totalLengthOfFileName[i] - amountOfSymbolsBeforeFileExtensionEnd[i]])
    print(f'Amount of symbols from the end of the string till the end of the file extension inside the {item} is {amountOfSymbolsFromTheEndOfStringTillTheEndOfFileExtensionEnd[i]}')
    
for i, item in enumerate(listoffiles):
    fileExtension.append([item[amountOfSymbolsBeforeFileExtension[i]:amountOfSymbolsBeforeFileExtensionEnd[i]]])
    print(f'file extension inside the {item} is {fileExtension[i]}')
    

for i, item in enumerate(bareFileNames):
    print(f'The Position is: {i}')
    print(f'The bare file name is: {item}')


for i, item in enumerate(bareFileNames):
    matchFirstDot = re.search(patternFirstDot, item)
    num_symbolsFirstDot = matchFirstDot.start() 
    print(f"The number of symbols before the file extension is: {num_symbolsFirstDot}")
    amountOfSyombolsBeforeDotInBareName.append(num_symbolsFirstDot)
    
    
for i, item in enumerate(bareFileNames):
    justBareName.append([item[0:amountOfSyombolsBeforeDotInBareName[i]]])
    print(f'The bare name is: {justBareName[i]}')
    
for i, item in enumerate(bareFileNames):
    forName = str(justBareName[i])
    forOpeningParenthesis = '('
    forDuplicateNumber = str(duplicateNumber[i])
    forClosingParenthesis = ')'
    forDot = '.'
    forFileExtension = str(fileExtension[i])
    forJson = '.json'
    beforeNewName = forName + forOpeningParenthesis + forDuplicateNumber + forClosingParenthesis + forDot + forFileExtension + forJson
    beforeNewName1 = re.sub(r"\[|\]|'", "", beforeNewName)
    print(f'The new name is: {str(beforeNewName1)}')
    newName.append(beforeNewName1)
    
backslash = "\\"
for i, item in enumerate(bareFileNames):
    print(f'The old name is: {bareFileNames[i]}')
    print(f'The new name is: {newName[i]}')
    os.rename(path + backslash + bareFileNames[i], path + backslash + newName[i])
    print(f'File renamed from {bareFileNames[i]} to {newName[i]}')
    print('--------------------------------------')
    




    


        



