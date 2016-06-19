
# film sentiment analysis

library(dplyr)

setwd(paste0(Sys.getenv('CS_HOME'),'/FilmsMining/Models/Dialogues'))

file = 'res/sentiment_ts_2016-06-17 08:09:03.634700.csv'

#res <- as.tbl(read.csv('res/sentiment_ts_2016-06-17 08:09:03.634700.csv',header=FALSE,sep=';'))
#rownames(res)<-res$V1

lines <- scan(file=file,what='character')
slines = lapply(lines,function(s){l=strsplit(s,";")[[1]];return(l)})

series=data.frame();#filmids=c();senttypes=c();
for(i in 1:length(slines)){
  currentline=slines[[i]];currentid=currentline[1];currentts=as.numeric(currentline[2:length(currentline)])
  if(length(currentts)>=100){
    normalizedts=c()
    for(t in 1:100){normalizedts=append(normalizedts,mean(currentts[(floor((t-1)*length(currentts)/100)):(floor(t*length(currentts)/100))]))}
    filmid=strsplit(currentid,"_")[[1]][1];senttype=strsplit(currentid,"_")[[1]][2]
    #filmids=append(filmids,filmid);senttypes=append(senttypes,senttype)
    for(t in 1:100){series=rbind(series,c(filmid,senttype,t,normalizedts[t]))}
  }
}

#series=cbind(filmids,senttypes,series)
names(series)<-c("filmids","senttypes",1:100)

g=ggplot(series,aes(x=))



