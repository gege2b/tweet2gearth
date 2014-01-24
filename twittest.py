# -*- coding: utf-8 -*- 
from TwitterAPI import TwitterAPI
import json
from sys import argv
import urllib
import os


consumerKey = ''
consumerSecret = ''
accessToken = ''
accessTokenSecret = ''


"""
Sets default options
"""
opt_screen_name = argv[len(argv)-1] 
opt_trim_user = 0
opt_count = 50
opt_noreplies = 1
opt_rts = 0

opt_save = False
opt_get_profile_img = False


for index in range(len(argv)) :
    if (argv[index] == '-c' or argv[index] == '--count'):
        opt_count = argv[index+1]

    if (argv[index] == '-r' or argv[index] == '--replies'):
        opt_noreplies = 0

    if ((argv[index] == '-t' or argv[index] == '--trim') and not opt_get_profile_img) :
        opt_trim_user = 1

    if argv[index] == '-rts':
        opt_rts = 1
        
    if argv[index] == '-s':
        opt_save = True

    if argv[index] == '-i':
        opt_get_profile_img = True
        opt_trim_user = False


    if argv[index] == '-h':
        print "Utilitaire de tracking sur Twitter"
        print ""
        print "Usage : " + argv[0] + " [options] screen_name"
        print "     -c X : retourne X tweets"
        print "     -r : inclu les réponses aux tweet dans les résultats"
        print "     -t : inclu les données de l'utilisateur dans les résultats"
        print "     -rts : inclus les retweets"
        print "     -s : sauvegarde un fichier KML (du nom de screen_name)"
        print "     -i : récupàre les images de profile"
        print "     screen_name : nom de l'utilisateur à tracker, obligatoire"
        quit()

        
params = {
'screen_name':opt_screen_name,
'trim_user':opt_trim_user,
'count':opt_count,
'exclude_replies':opt_noreplies,
'include_rts':opt_rts
}

print '\n'
print 'Lancement du tracking sur l\'utilisateur ' + opt_screen_name + '\n\n'
print '-----------------------------------------------------\n\n'
got_geo = False

try:
    api = TwitterAPI(consumerKey, consumerSecret, accessToken, accessTokenSecret)


    tweets = api.request('statuses/user_timeline', params )
    kml = "<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n<Document>"

    for item in tweets.get_iterator():
        if item['user']['profile_image_url'] is not None:
            locale_profile_img = opt_screen_name + "_profile"
            profile_img = item['user']['profile_image_url']
            if not os.path.exists(locale_profile_img + '.jpeg'):
                print "Image de profile : " + profile_img
                urllib.urlretrieve(profile_img, locale_profile_img + '.jpeg')
                urllib.urlretrieve(profile_img.replace('_normal', '', 1), locale_profile_img + '_big.jpeg')
        
        if item['coordinates'] is not None:
            print item['coordinates']['coordinates']
            got_geo = True
            kml = kml + "<Placemark><name>" + item['id_str'] + "</name><description>" + item['text'] + "\n" + item['created_at'] + "</description><time>" + item['created_at'] + "</time><Point><coordinates>" + str(item['coordinates']['coordinates'][0]) + ","  + str(item['coordinates']['coordinates'][1]) + "</coordinates></Point></Placemark>\n" 
            
    kml = kml + "</Document></kml>"

    if opt_save and got_geo:
        file = open(opt_screen_name + '.kml', 'w')
        file.write(kml.encode('utf-8'))
        file.close

except Exception as e:
    print(e)
