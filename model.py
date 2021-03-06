from main import db,Example,Correction
import numpy as np

db.drop_all()
db.create_all()

tseries=[['0.70','1.14','1.41','2.23','3.01','3.56','4.24','4.6','5.25','5.69','6.48','6.68'],['0.34','0.64','1.25','1.86','2.56','2.94','3.53','4.19','4.29'],['0.51','1.12','1.59','2.09','2.70','3.08','3.33','4.26','4.52','5.18','5.68','6.25','6.51'],['0.35','1.12','1.74','2.29','2.79','3.45','3.80','4.40','5.10','5.33','5.97','6.34','6.75','7.28','7.98','8.13'],['0.42', '1.12', '1.81', '2.37', '2.91', '3.28', '3.76', '4.41', '4.82', '5.49', '6.29', '6.73', '7.11', '7.85', '8.58', '8.94', '9.22', '9.81', '10.48', '10.98', '11.74', '12.17', '12.49', '12.6']]

txt=["गेल्या ५ जुलैला स्वता सिद्धु यांनी आपल्या राजीनाम्याची घोषणा ट्विटरवर केली होती","काही बाबतीत प्रसूतीपूर्व जीवनसत्त्वे घेणे अत्यंत अनिष्ट आहे म्हणतात","मात्र पंधरा नोक्हेंबर अठराशे सतरा मध्ये मराठयांचे आणि इंग्रजांमध्ये खडकीचे अखेरचे युद्ध झाले","आमदार कार्लूस आल्मेडा यांनी पणजीतील जाहीर सभेत वास्कोतून एक हजाराहून अधिक नागरिक उपस्थित राहणार असल्याचे सांगितले","स्लॅमडान्स एकोणीशे सत्याऐंशी ह्या आधुनिक न्वार चित्रपटाचा कला दिग्दर्शक युगेनियो झारेटी म्हणतो न्वारचे आकर्षण कालातीत आहे कारण न्वारच्या नायकाला सुटकेचा मार्ग नसतो पर्याय नसतात"]
print(len(tseries))
audio_array = ['mr_m_education_01704.wav', 'mr_m_health_02910.wav', 'mr_m_other_02008.wav','mr_m_politics_01159.wav','mr_m_general_00163.wav']


for i in np.arange(5):
    eg=Example(title=audio_array[i],txt=txt[i],iscorrect=True)
    db.session.add(eg)
    db.session.commit()
    count=1
    txt1=txt[i]
    txtsplit=txt1.split(" ")
    print(len(txtsplit))
    print(len(tseries[i]))
    for j in tseries[i]:
        tt=Correction(time=j,txt=txtsplit[count-1],id1=count,Correct=True,example=eg)
        db.session.add(tt)
        db.session.commit()
        count=count+1


