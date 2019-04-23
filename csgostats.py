from steam import WebAPI

import pandas as pd



try:
    vanity = str(input()) #example input https://steamcommunity.com/id/aashaBiceps, enter the text after the 'id/',i.e in this case enter aashaBiceps
    key = 'CDB0C25EF9CF6CC515B0731EDD678129'


    api = WebAPI(key,auto_load_interfaces=True)


    name = api.ISteamUser.ResolveVanityURL_v1(vanityurl=vanity)
    url_id = name['response']['steamid']
    print('getting stats for steamid :'+ str(url_id))


    f =api.ISteamUserStats.GetUserStatsForGame(appid=730,steamid=url_id,format='json')


    data = pd.DataFrame.from_dict(f['playerstats']['stats'],orient='columns')
    stats_file = 'stats_'+vanity+'.xlsx'
    data.to_excel(stats_file)
    print('The file '+ stats_file+ ' contains all your stats! Cheers')
except:
    print('Could not retrieve stats for: \n' + str(url_id) + ' / ' +vanity)
    print('Maybe your profile or game stats are set to  "Private"')
    print('Set either to "Public" to be able to grab your stats' )