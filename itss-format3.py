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
                
                lineStr2 = lineStr
                
                rpos = lineStr.rfind(")")
                lpos = lineStr.rfind("(")
                if rpos>lpos and lpos!=-1:
                    rightmost = lineStr[rpos+1:].strip()
                    mid2 = lineStr[lpos+1:rpos]
                    mid2 = mid2.strip()
                    mid22 = "("+mid2+")"+rightmost;
                    lineStr = lineStr[0:lpos]+mid22;
                    rpos = lineStr.rfind(")", 0, lpos);
                    lpos = lineStr.rfind("(", 0, lpos);
                    if lpos<rpos and lpos!=-1:
                        mid2 = lineStr[lpos+1:rpos]
                        mid2 = mid2.strip();
                        if mid2=="T" or mid2=="F":
                           lineStr = lineStr[0:lpos]+"("+mid2+")" +mid22
                        
                    #question
                    lineStr2 = lineStr
                    if len(lineStr)>5  and lineStr.endswith("(T)(1)"):
                        lineStr2 = lineStr.replace("(T)(1)", "~@[T](1)");
                    elif len(lineStr)>5 and lineStr.endswith("(F)(1)"):
                        lineStr2 = lineStr.replace("(F)(1)", "~@[F](1)");
                    elif len(lineStr)>5 and lineStr.endswith("(T)(2)"):
                        lineStr2 = lineStr.replace("(T)(2)", "~@[T](2)");
                    elif len(lineStr)>5 and lineStr.endswith("(F)(2)"):
                        lineStr2 = lineStr.replace("(F)(2)", "~@[F](2)");
                    elif len(lineStr)>5 and lineStr.endswith("(F)"):
                        lineStr2 = lineStr.replace("(F)", "~@[F](1)");
                    elif len(lineStr)>5 and lineStr.endswith("(T)"):
                        lineStr2 = lineStr.replace("(T)", "~@[T](1)");
                    elif len(lineStr)>5 and lineStr.endswith("()T"):
                        lineStr2 = lineStr.replace("()T", "~@[T](1)");
                    elif len(lineStr)>5 and lineStr.endswith("()F"):
                        lineStr2 = lineStr.replace("()F", "~@[F](1)");
                elif lineStr.endswith(" T"):
                    lineStr2=lineStr[0:-2]+"~@[T](1)";
                elif lineStr.endswith(" F"):
                    lineStr2=lineStr[0:-2]+"~@[F](1)";
                nf.write(lineStr2+"\n")
        nf.close()
        of.close()
        print(newfn)
        #break;