import pandas as pd

person = pd.read_csv('data/survey_person.csv')
site = pd.read_csv('data/survey_site.csv')
survey = pd.read_csv('data/survey_survey.csv')
visited = pd.read_csv('data/survey_visited.csv')

visited_subset = visited.loc[[0,2,6],]
print(visited_subset)
merge = site.merge(visited_subset, left_on='name', right_on='site')
print(merge)
merge_all = site.merge(visited, left_on='name', right_on='site')
print(merge_all)

ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')
print(ps)
print(vs)

ps_vs = ps.merge(vs, left_on=['ident', 'taken', 'quant', 'reading'], right_on=['person', 'ident', 'quant', 'reading'])
print(ps_vs)
