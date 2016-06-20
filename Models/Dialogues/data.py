
import nltk,json
import utils



def load_data(lines_file,conversations_file) :
    # construct dico lineID -> {characterid,charactername,movieid,text}
    lines_dico={}
    for line in utils.read_csv(lines_file,' +++$+++ ') :
        lines_dico[line[0]]={'characterid':line[1],'charactername':line[3],'movieid':line[2],'text':line[4]}
    # construct the film dico : id -> [dialogues = [text1,text2...]]
    films={}
    for dialogue in utils.read_csv(conversations_file,' +++$+++ ') :
        filmid=dialogue[2]
        if filmid not in films : films[filmid]=[]
        #print dialogue[3]
        #lineids = json.loads(dialogue[3])# issue with json string ?
        lineids = utils.parse_json_array(dialogue[3])
        films[filmid].append([lines_dico[lineid]['text'] for lineid in lineids])
    return films

def load_filmmetadata(f):
    res= {}
    #years=set()
    years={}
    types=set()
    for line in utils.read_csv(f,' +++$+++ ') :
        filmid=line[0]
        res[filmid]={'title':line[1],'year':line[2]}
        if line[2] not in years:
            years[line[2]]=1
        else :
            years[line[2]]=years[line[2]]+1
        # get film types
        filmtypes = utils.parse_json_array(line[5])
        for t in filmtypes : types.add(t)
    #print(years)
    print(types)
    return res

def convert_metadata(f,t):
    res=[]
    for line in utils.read_csv(f,' +++$+++ ') :
        filmid=line[0];filmtitle=line[1];filmyear=line[2][:4];filmrating=line[3];filmratingnum=line[4]
        for filmtype in utils.parse_json_array(line[5]):
            res.append([filmid,filmtitle,filmyear,filmrating,filmratingnum,filmtype])
    utils.export_csv(res,t,';')

# test
#films = load_data('/Users/Juste/Documents/ComplexSystems/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_lines.txt','/Users/Juste/Documents/ComplexSystems/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_conversations.txt')

#for d in films[films.keys()[0]]:
#    print d

#load_filmmetadata('/Users/Juste/Documents/ComplexSystems/FilmsMining/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_titles_metadata.txt')
convert_metadata('/Users/Juste/Documents/ComplexSystems/FilmsMining/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_titles_metadata.txt','/Users/Juste/Documents/ComplexSystems/FilmsMining/FilmsMining/Data/processed/metadata.csv')
