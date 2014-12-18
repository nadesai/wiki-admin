import graphlab as gl

location = 'data/wikiUserTalk_revisions.txt'
output = 'data/wikiUserTalk_revisions.csv'

revisions = gl.SFrame.read_csv(location,delimiter=' ',header=False)

columns = ['X1','X2','X3','X4','X5','X6','X7']
newcolumns = ['REVISION', 'article_id', 'rev_id', 'article_title', 'timestamp', 'username', 'user_id']
renaming_dict = dict(zip(columns,newcolumns))

revisions.rename(renaming_dict)
revisions = revisions[['article_title','timestamp','username','user_id']]
revisions.rename({'article_title':'target_user','username':'source_user','user_id':'source_id'})

def process_id(strid):
    split_id = strid.split(':')
    if len(split_id) > 1:
        return -1
    else:
        return int(split_id[0])

revisions['source_id'] = revisions['source_id'].apply(process_id)
revisions = revisions.filter_by(values=[-1],column_name='source_id',exclude=True)

revisions['target_user'] = revisions['target_user'].apply(lambda s: s.split('/')[0])

p = len('User_talk:')
revisions['target_user'] = revisions['target_user'].apply(lambda s: s[p:])

revisions.save(output)
