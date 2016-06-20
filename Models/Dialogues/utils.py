
# utils
import datetime

def read_csv(file,delimiter):
    f=open(file,'r')
    lines = f.readlines()
    return([s.replace('\n','').split(delimiter) for s in lines])

# export dico key -> array as csv
def export_dico_ts_csv(dico,fileprefix):
    outfile=open(fileprefix+str(datetime.datetime.now())+'.csv','w')
    for k in dico.keys():
        #print(len(dico[k]))
        outfile.write(k+";")
        for i in range(len(dico[k])-1):
            outfile.write(str(dico[k][i])+";")
        outfile.write(str(dico[k][len(dico[k])-1]))
        outfile.write('\n')

# export array of arrays as csv
def export_csv(m,f,sep):
    outfile=open(f,'w')
    for row in m :
        for i in range(len(row)-1):
            outfile.write(str(row[i])+sep)
        outfile.write(str(row[len(row)-1])+'\n')


# dirty simple array parsing
def parse_json_array(s):
    return(s.replace('[','').replace(']','').replace('\'','').replace(' ','').split(','))

#test={}
#for i in range(10) :
#    test[str(i)]=[]
#    for j in range(10) :
#       test[str(i)].append(str(j))

#export_dico_ts_csv(test,'res/test')
