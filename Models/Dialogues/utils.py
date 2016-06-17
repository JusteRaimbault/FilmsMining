
# utils
import datetime

def read_csv(file,delimiter):
    f=open(file,'r')
    lines = f.readlines()
    return([s.replace('\n','').split(delimiter) for s in lines])


def export_dico_ts_csv(dico,fileprefix):
    outfile=open(fileprefix+str(datetime.datetime.now())+'.csv','w')
    for k in dico.keys():
        outfile.write(k+";")
        for i in range(len(dico[k])-1):
            outfile.write(str(dico[k][i])+";")
        outfile.write(str(dico[k][len(dico[k])-1]))
        outfile.write('\n')