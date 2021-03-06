import json_lines
import codecs

negFile = codecs.open('rt-polarity.neg', 'w', 'utf-8')
posFile = codecs.open('rt-polarity.pos', 'w', 'utf-8')
gameReview = ['Arma_3', 'Counter_Strike', 'Counter_Strike_Global_Offensive', 'Dota_2', 'Football_Manager_2015',
              'Garrys_Mod', 'Grand_Theft_Auto_V', 'Sid_Meiers_Civilization_5', 'Team_Fortress_2', 'The_Elder_Scrolls_V', 'Warframe']
for game in gameReview:
    currReview = game + '.jsonlines'
    with open(currReview, 'rb') as f:
        for item in json_lines.reader(f):
            if item['rating'] == 'Recommended':
                posFile.write(item['review']+'\n')
            else:
                negFile.write(item['review']+'\n')
negFile.close()
negFile.close()
                