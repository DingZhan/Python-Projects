#dzh 2019.10.17 data wash for ITSS 
import os
import shutil

dir = os.getcwd()
filenames = os.listdir()

for fn in filenames:
    if fn.endswith(".txt"):
        newfn = fn[0:-4] + "(new).txt"
        #print(newfn)
        #shutil.copyfile(fn, newfn)
        nf = open(newfn, "w")
        with open(fn, "r") as of:
            for lineStr in of:
                lineStr = lineStr.strip()
                lineStr = lineStr.replace('．', '. ')
                lineStr = lineStr.replace('（',' (')
                lineStr = lineStr.replace('）',') ')
                lineStr = lineStr.replace("\t", "    ")
                lineStr = lineStr.replace("？", "?")
                lineStr = lineStr.replace("．", ".")
                
                #question
                if len(lineStr)>5 and lineStr[0].isdigit() and lineStr[-1]==']' and lineStr[-3]=='[' and lineStr[-2]>='A' and lineStr[-2]<='F' and lineStr[-4]=='@':
                    lineStr2 = lineStr[0:-4] + " " + lineStr[-4:] + "(1)"
                    nf.write(lineStr2+"\n")
                elif len(lineStr)>5 and lineStr[0].isdigit() and lineStr[-2]=='@' and lineStr[-1]>='A' and lineStr[-1]<='F':
                    lineStr2 = lineStr[0:-2] + " @[" + lineStr[-1] + "](1)"
                    nf.write(lineStr2+"\n")
                elif len(lineStr)>5 and lineStr[0].isdigit() and lineStr[-2]=='。' and lineStr[-1]>='A' and lineStr[-1]<='F':
                    lineStr2 = lineStr[0:-1] + " @[" + lineStr[-1] + "](1)"
                    nf.write(lineStr2+"\n")
                elif len(lineStr)>5 and lineStr[0].isdigit() and lineStr[-2]=='?' and lineStr[-1]>='A' and lineStr[-1]<='F':
                    lineStr2 = lineStr[0:-1] + " @[" + lineStr[-1] + "](1)"
                    nf.write(lineStr2+"\n")
                elif len(lineStr)>5 and lineStr[0].isdigit() and (lineStr[-3]=='?' or lineStr[-3]=='。' or lineStr[-3]==')') and lineStr[-2]==' ' and lineStr[-1]>='A' and lineStr[-1]<='F':
                    lineStr2 = lineStr[0:-1] + " @[" + lineStr[-1] + "](1)"
                    nf.write(lineStr2+"\n")
                elif len(lineStr)>2 and lineStr[0]>='A' and lineStr[0]<='F' and lineStr[1]==':':
                    lineStr2 = lineStr[0] + ". " + lineStr[2:];
                    nf.write(lineStr2+"\n")
                elif lineStr.startswith("A."):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("A.") and lineStr2.startswith("A. ")==False:
                        lineStr2 = lineStr2.replace("A.", "A. ");
                    if lineStr2.find(" B.")!=-1:
                        lineStr2 = lineStr2.replace(" B.", "\nB. ");
                    if lineStr2.find(" C.")!=-1:
                        lineStr2 = lineStr2.replace(" C.", "\nC. ");
                    if lineStr2.find(" D.")!=-1:
                        lineStr2 = lineStr2.replace(" D.", "\nD. ");
                    nf.write(lineStr2+"\n")                    
                elif lineStr.startswith("B."):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("B.") and lineStr2.startswith("B. ")==False:
                        lineStr2 = lineStr2.replace("B.", "B. ");
                    if lineStr2.find(" C.")!=-1:
                        lineStr2 = lineStr2.replace(" C.", "\nC. ");
                    if lineStr2.find(" D.")!=-1:
                        lineStr2 = lineStr2.replace(" D.", "\nD. ");
                    nf.write(lineStr2+"\n")      
                elif lineStr.startswith("C."):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("C.") and lineStr2.startswith("C. ")==False:
                        lineStr2 = lineStr2.replace("C.", "C. ");
                    if lineStr2.find(" D.")!=-1:
                        lineStr2 = lineStr2.replace(" D.", "\nD. ");
                    nf.write(lineStr2+"\n")                       
                elif lineStr.startswith("D."):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("D.") and lineStr2.startswith("D. ")==False:
                        lineStr2 = lineStr2.replace("D.", "D. ");
                    nf.write(lineStr2+"\n")       
                #A、
                elif lineStr.startswith("A、"):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("A、"):
                        lineStr2 = "A. "+ lineStr2[2:];
                    if lineStr2.find(" B、")!=-1:
                        lineStr2 = lineStr2.replace(" B、", "\nB. ");
                    if lineStr2.find(" C、")!=-1:
                        lineStr2 = lineStr2.replace(" C、", "\nC. ");
                    if lineStr2.find(" D、")!=-1:
                        lineStr2 = lineStr2.replace(" D、", "\nD. ");
                    nf.write(lineStr2+"\n")                    
                elif lineStr.startswith("B、"):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("B、"):
                        lineStr2 = "B. "+ lineStr2[2:];
                    if lineStr2.find(" C、")!=-1:
                        lineStr2 = lineStr2.replace(" C、", "\nC. ");
                    if lineStr2.find(" D、")!=-1:
                        lineStr2 = lineStr2.replace(" D、", "\nD. ");
                    nf.write(lineStr2+"\n")      
                elif lineStr.startswith("C、"):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("C、"):
                        lineStr2 = "C. "+ lineStr2[2:];                    
                    if lineStr2.find(" D、")!=-1 and lineStr2.find(" D. ")==-1:
                        lineStr2 = lineStr2.replace(" D、", "\nD. ");
                    nf.write(lineStr2+"\n")                       
                elif lineStr.startswith("D、"):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("D、"):
                        lineStr2 = "D. "+ lineStr2[2:];
                    nf.write(lineStr2+"\n")                       
                #A_
                elif lineStr.startswith("A "):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("A "):
                        lineStr2 = "A. "+ lineStr2[2:];
                    if lineStr2.find(" B ")!=-1:
                        lineStr2 = lineStr2.replace(" B ", "\nB. ");
                    if lineStr2.find(" C ")!=-1:
                        lineStr2 = lineStr2.replace(" C ", "\nC. ");
                    if lineStr2.find(" D ")!=-1:
                        lineStr2 = lineStr2.replace(" D ", "\nD. ");
                    nf.write(lineStr2+"\n")                    
                elif lineStr.startswith("B "):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("B "):
                        lineStr2 = "B. "+ lineStr2[2:];
                    if lineStr2.find(" C ")!=-1:
                        lineStr2 = lineStr2.replace(" C ", "\nC. ");
                    if lineStr2.find(" D ")!=-1:
                        lineStr2 = lineStr2.replace(" D ", "\nD. ");
                    nf.write(lineStr2+"\n")      
                elif lineStr.startswith("C "):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("C "):
                        lineStr2 = "C. "+ lineStr2[2:];                    
                    if lineStr2.find(" D ")!=-1 and lineStr2.find(" D. ")==-1:
                        lineStr2 = lineStr2.replace(" D ", "\nD. ");
                    nf.write(lineStr2+"\n")                       
                elif lineStr.startswith("D "):
                    lineStr2 = lineStr;
                    if lineStr2.startswith("D "):
                        lineStr2 = "D. "+ lineStr2[2:];
                    nf.write(lineStr2+"\n")                       
                else:
                    nf.write(lineStr+"\n")
        nf.close()
        of.close()
        print(newfn)
        #break;