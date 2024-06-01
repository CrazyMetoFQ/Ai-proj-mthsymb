import os
import shutil

mpath = "C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/data/htmlsynthdata_sym_raw/"

fls = os.listdir(mpath)
fls.remove("sorter.py")
flsd = [i for i in fls]

for f in flsd:
    if not os.path.isfile(mpath+f):
        fls.remove(f)


pfls = [i.replace(".png","").replace("img_","").replace(" (1)","").split("_") for i in fls]

# print(pfls)


def find_dest(s:str):

    # si = s.replace(".png","").replace("img_","").replace(" (1)","").split("_")[0]

    si = s
    if si.isnumeric():
        return si
    elif si.islower():
        return si+"-l"
    elif si.isupper():
        return si+"-u"

for f,p in zip(fls,pfls):
    print(f, " | ",find_dest(p[0]))
    shutil.copy(mpath+f, mpath+find_dest(p[0])+f"/img_{p[1]}.png")
