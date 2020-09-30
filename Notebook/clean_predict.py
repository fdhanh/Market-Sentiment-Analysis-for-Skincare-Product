import sys
import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory 
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def clean_predict(sentence):
    stop = list(set(stopwords.words('indonesian'))) 
    stop.extend('read aku awal beberapa banya apa akhir more muncul pake pakai banget yg sudah udah gitu nya nggak gak tp aja ga night cream day creamnya ngga ya sih kulit muka beli bikin produk emang wajah bangun bgt coba dipake hasil karna krim langsung minggu pagi sampe tekstur tidur asa kali make malam nyata tau gk series temen jd kalo ku rangkai skincare so habis malem benar jg krn liat nyoba tube tuh trs sebenernya kayak lihat sm utk harap no paket pas sayang'.split())
    word_replace = {
        'basic': 'basic',
        'bbr': 'beberapa',
        'beber': 'beberapa',
        'banya': 'banyak',
        'bangu': 'bangun',
        'bange':'banget',
        'balancing': 'balance',
        'bekas': 'bekas',
        'belang': 'belang',
        'benefi': 'benefit',
        'bener': 'benar',
        'benar': 'benar',
        'awet': 'awet',
        'aroma': 'aroma',
        'awal': 'awal',
        'apa': 'apa',
        'ancur': 'hancur',
        'aneh': 'aneh',
        'antiok': 'antioksidan',
        'antiox': 'antioksidan',
        'antiag': 'antiaging',
        'ampoul': 'ampoule',
        'aku': 'aku',
        'alhamd': 'alhamdulillah',
        'allhamd': 'alhamdulillah',
        'abis': 'habis',
        'absor': 'absorb',
        'acne': 'acne',
        'alcohol': 'alkohol',
        'allerg': 'alergi',
        'alfa': 'alfamart',
        'alus': 'halus',
        'agingnya': 'aging',
        'ampu': 'ampuh',
        'arbuti': 'arbutin',
        'bagu': 'bagus',
        'bau': 'bau',
        'beli': 'beli',
        'berjerawat': 'jerawat',
        'berminya': 'minyak',
        'berminyak': 'minyak',
        'bersi': 'bersih',
        'berunt': 'beruntusan',
        'besok': 'besok',
        'breakou': 'breakout',
        'bright': 'bright',
        'bruntu': 'beruntusan',
        'calm': 'calm',
        'cepe': 'cepat',
        'cera': 'cerah',
        'cinta': 'cinta',
        'coco': 'cocok',
        'cuco': 'cocok',
        'dingi': 'dingin',
        'efek': 'efek', 
        'effe': 'efek',
        'ena': 'enak',
        'favo': 'favorit',
        'gatal': 'gatal',
        'gatel': 'gatal',
        'gila': 'gila',
        'glow': 'glow',
        'good': 'good',
        'greas': 'greasy',
        'halu': 'halus',
        'hasil': 'hasil',
        'hema': 'hemat',
        'hitam': 'hitam',
        'hrg': 'harga',
        'hydrat': 'hydrate',
        'jerawa': 'jerawat',
        'kelembab': 'lembab',
        'kelembut': 'lembut',
        'kenya': 'kenyal',
        'kenye': 'kenyal',
        'kental': 'kental',
        'kerii': 'kering',
        'kerin': 'kering',
        'kombi': 'kombinasi',
        'komedo': 'komedo',
        'kusem': 'kusam',
        'kusam': 'kusam',
        'lama': 'lambat',
        'lemba': 'lembab',
        'lembu': 'lembut',
        'lengket': 'lengket',
        'lightening' : 'light',
        'love': 'love',
        'lumay': 'lumayan',
        'mahal': 'mahal',
        'mahaa': 'mahal',
        'manta': 'mantap',
        'mante': 'mantap',
        'manto': 'mantul',
        'mantu': 'mantul',
        'matt': 'matte',
        'melemba': 'lembab',
        'mencerahk': 'cerah',
        'minyak': 'minyak',
        'moist': 'moist',
        'mulus': 'mulus',
        'muluu': 'mulus',
        'nglembab': 'lembab',
        'ngelembab': 'lembab',
        'oily': 'oily',
        'normal': 'normal',
        'panas': 'panas',
        'parah': 'parah',
        'perfect': 'perfect',
        'recco': 'recommend',
        'recomm': 'recommend',
        'rednes': 'redness',
        'rejuve': 'rejuve',
        'repurch': 'repurchase',
        'ringa': 'ringan',
        'sebagus': 'bagus',
        'segaa': 'segar',
        'segar': 'segar',
        'segee': 'segar',
        'seger': 'segar',
        'sensit': 'sensitif', 
        'shope': 'shopee',
        'suka': 'suka',
        'syuka': 'suka',
        'whiten': 'white',
        'wangi': 'wangi',
        'amaz': 'amaze',
        'aman': 'aman',
        'textur': 'tekstur',
        'akhir': 'akhir',
        'packaging': 'package'}
        
    kal_3 = {}
    kal_4 = {}
    kal_5 = {}
    kal_6 = {}
    kal_7 = {}
    kal_8 = {}
    kal_9 = {}
    kal_10 = {}

    for i,j in list(zip(word_replace.keys(), word_replace.values())):
        if len(i) == 10:
            kal_10[i] = j
        elif len(i) == 9:
            kal_9[i] = j
        elif len(i) == 8:
            kal_8[i] = j
        elif len(i) == 7:
            kal_7[i] = j
        elif len(i) == 6:
            kal_6[i] = j
        elif len(i) == 5:
            kal_5[i] = j
        elif len(i) == 4:
            kal_4[i] = j
        else:
            kal_3[i] = j
    
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("","",string.punctuation)) 
    sentence = sentence.split()
    sentence = [stemmer.stem(word) for word in sentence]
    temp = []
    for i in sentence:
        if i[:3] in kal_3.keys(): 
            temp.append(kal_3[i[:3]])
        elif i[:4] in kal_4.keys(): 
            temp.append(kal_4[i[:4]])
        elif i[:5] in kal_5.keys(): 
            temp.append(kal_5[i[:5]]) 
        elif i[:6] in kal_6.keys(): 
            temp.append(kal_6[i[:6]]) 
        elif i[:7] in kal_7.keys(): 
            temp.append(kal_7[i[:7]])    
        elif i[:8] in kal_8.keys(): 
            temp.append(kal_8[i[:8]])   
        elif i[:9] in kal_9.keys(): 
            temp.append(kal_9[i[:9]])   
        elif i[:10] in kal_10.keys(): 
            temp.append(kal_10[i[:10]])       
        else:
            temp.append(i) 
    temp = [word for word in temp if word not in stop]
    return ' '.join(temp)

sys.modules[__name__] = clean_predict    