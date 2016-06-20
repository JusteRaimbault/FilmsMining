
# film sentiment analysis

library(dplyr)
library(ggplot2)

setwd(paste0(Sys.getenv('CS_HOME'),'/FilmsMining/Models/Dialogues'))

file = 'res/sentiment_ts_2016-06-17 08:09:03.634700.csv'

filmdata<-read.csv('../../Data/processed/metadata.csv',header=FALSE,sep=';')

lines <- scan(file=file,what='character')
slines = lapply(lines,function(s){l=strsplit(s,";")[[1]];return(l)})

tbins=100
series=c();times=c();filmids=c();senttypes=c();
negseries=data.frame();neuseries=data.frame();posseries=data.frame();seriesnames=c()
#cseries=data.frame()
for(i in 1:length(slines)){
  currentline=slines[[i]];currentid=currentline[1];currentts=as.numeric(currentline[2:length(currentline)])
  # take the films with more than 100 lines
  if(length(currentts)>=100){
    normalizedts=c()
    for(t in 1:100){normalizedts=append(normalizedts,mean(currentts[(floor((t-1)*length(currentts)/100)):(floor(t*length(currentts)/100))]))}
    filmid=strsplit(currentid,"_")[[1]][1];senttype=strsplit(currentid,"_")[[1]][2]
    series=append(series,normalizedts);times=append(times,1:100)
    filmids=append(filmids,rep(filmid,length(normalizedts)));senttypes=append(senttypes,rep(senttype,length(normalizedts)))
    cseries = rbind(cseries,normalizedts)
    #show(senttype)
    if(senttype=='neg'){negseries = rbind(negseries,normalizedts);seriesnames=append(seriesnames,filmid)}
    if(senttype=='neu'){neuseries = rbind(neuseries,normalizedts)}
    if(senttype=='pos'){posseries = rbind(posseries,normalizedts)}
    
  }
}

series=cbind(negseries,neuseries,posseries)
rownames(series)<-seriesnames

#ccoef=c()
#for(k in 2:25){
#  show(k)

km = kmeans(series,k,iter.max=10000,nstart=10)

#ccoef=append(ccoef,km$tot.withinss/km$totss)
#}
#plot(2:25,ccoef)
#km$centers

# plot ts
times=c();cseries=c();clusters=c();types=c()
for(i in 1:nrow(km$centers)){
  times=append(times,rep(1:tbins,3));
  cseries=append(cseries,km$centers[i,]);
  clusters=append(clusters,rep(as.character(i),3*tbins))
  types=append(types,c(rep('neg',tbins),rep('neu',tbins),rep('pos',tbins)))
}

g=ggplot(data.frame(cluster=clusters,value=cseries,time=times,type=types),aes(x=time,y=value,group=cluster,colour=cluster))
g+geom_line()+geom_smooth(alpha=0.5)+facet_wrap(~type,scales = "free")


# look at positions of film genre in cluster space

# films as vector of distance to cluster centers
filmsclust = t(apply(series,MARGIN = 1,FUN = function(row){
  apply(km$centers,1,function(center){sqrt(sum((center-row)^2))})
}))

# pca
pfilmsclust = prcomp(filmsclust)
coords = filmsclust%*%pfilmsclust$rotation

# plot with cluster
g=ggplot(data.frame(PC1=coords[,1],PC2=coords[,2],cluster=as.character(km$cluster)))
g+geom_point(aes(x=PC1,y=PC2,colour=cluster))

# plot with genre
#rownames(filmdata)<- filmdata[,1]
#duplicate film rows
genres = c();pc1=c();pc2=c();clusters=c()
for(i in 1:nrow(coords)){
  rows = which(filmdata[,1]==rownames(coords)[i])
  genres=append(genres,as.character(filmdata[rows,6]));pc1=append(pc1,rep(coords[i,1],length(rows)));pc2=append(pc2,rep(coords[i,2],length(rows)));
  clusters=append(clusters,rep(km$cluster[i],length(rows)))
}

g=ggplot(data.frame(PC1=jitter(pc1),PC2=jitter(pc2),genre=genres))
g+geom_point(aes(x=PC1,y=PC2,colour=genre))

#
# does not see anything.
#
# look at cluster composition ?
g=ggplot(data.frame(cluster=clusters,genre=genres))
g+geom_bar(aes(x=cluster,fill=genre),position="fill")








