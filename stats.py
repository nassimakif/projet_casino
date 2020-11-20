import json
from json.decoder import JSONDecodeError
from os import path
import os.path
class Stats:
    def __init__(self, gain, meilleure_gain, pire_gain, mise, meilleur_mise, pire_mise, name_user):
        self.gain = gain
        self.meilleure_gain = meilleure_gain
        self.pire_gain = pire_gain
        self.mise = mise
        self.meilleur_mise = meilleur_mise
        self.pire_mise = pire_mise
        self.name_user = name_user
    # retourne les meilleures gains (meilleures gains) pour les stats joueurs
    def meilleureGain(gain, meilleure_gain):
        if gain > meilleure_gain:
            return gain
        else:
            return meilleure_gain
    # retourne les meilleures mises (meilleures mises) pour les stats joueurs
    def meilleureMise(mise, meilleure_mise):
        if mise > meilleure_mise:
            return mise
        else:
            return meilleure_mise
    # retourne les pire mises (mises les plus faibles) pour les stats joueurs
    def pireMise(mise, pire_mise):
        if pire_mise < mise:
            return pire_mise
        else:
            return mise
    # retourne les pire gains (gains les plus faibles) pour les stats joueurs
    def pireGain(gain, pire_gain):
        if pire_gain < gain:
            return pire_gain
        else:
            return gain
    def save_stats(meilleure_gain, pire_gain, meilleure_mise, pire_mise, name_user, date):
        donnees = { name_user : {
        'meilleure gain':[meilleure_gain],
        'pire gain': [pire_gain],
        'meilleure mise': [meilleure_mise],
        'pire mise': [pire_mise],
        'date' : [date]
        }
        }
        with open("stats.json", "r") as file:
            data_json = json.load(file)
            file.close()
            with open("stats.json", "w") as file:
                if name_user in data_json["list_pseudo"]:  
                    data_json[name_user]['meilleure gain'].append(meilleure_gain)
                    data_json[name_user]['pire gain'].append(pire_gain)
                    data_json[name_user]['meilleure mise'].append(meilleure_mise)
                    data_json[name_user]['pire mise'].append(pire_mise)
                    data_json[name_user]['date'].append(date)
                    json.dump(data_json, file)
                else:
                    data_json["list_pseudo"].append(name_user)
                    data_json.update(donnees)
                    json.dump(data_json, file)
    
    def dataJson(JsonFile):
        with open("stats.json", "r") as file:
            data_json = json.load(file)
            file.close()
            return data_json
    def creation_stats():
        stat = {
                "list_pseudo" : []
            }
        if not path.exists("stats.json"):
            with open("stats.json", "w") as file:
                json.dump(stat, file)
                file.close()