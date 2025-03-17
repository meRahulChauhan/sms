from django.db import models
from django.db import models
from django.utils import timezone
class Choice(models.Model):
    class_choice={'P':'pre-nursury','N':'nursery','KG':'kg','1':'Class-1','2':'Class-2','3':'Class-3',
                '4':'Class-4','5':'Class-5','6':'Class-6','7':'Class-7','8':'Class-8','9':'Class-9','10':'Class-10',
                '11':'Class-11','12':'Class-12'}
    gender_choice={
        'm':'male',
        'f':'female',
        'x':'other'
        }
    subject_choice={'Hi1':'Hindi-I','Hi2':'Hindi-II','En1':'English-Literature','En2':'English-Grammar','M1':'Math-I','M2':'Math-II',
                    'Sci1':'Science-I','Sci2':'Science-II','Soc':'Social Social','Comp':'Computer','Geo':'Geography','GK':'General-Konwledge',
                    'Phy1':'Physics','Phy2':'Physics-II','Chem1':'Chemistry-I','Chem1':'Chemistry-II'}
    specialization_choice={'hi':'Hindi','en':'English','math':'Mathematcis','Bio':'Biology','Chem':'Chemistry',
                            'phy':'physics','Comp':'Computer','Art':'Art','Com':'Commerce','Geo':'Geography','PSci':'Political Sciecne',
                            'Env':'Environment','Soc':'Social','Hs':'History'}
    types={'Q':'Query','C':'Complain','Help':'Help','R':'Report a problem'}
    attendance={
        'a':'absent',
        'p':'present',
        'ol':'on_leave'
        }
    

    subject_list = {
        "P": {
            "base": ["Rhymes", "Storytelling", "Playtime", "Drawing", "Games"],
            "elective": [],
            "optional": []
        },
        "N": {
            "base": ["Rhymes", "Storytelling", "Alphabets", "Numbers", "Playtime", "Drawing", "Games"],
            "elective": [],
            "optional": []
        },
        "KG": {
            "base": ["Hindi", "English", "Mathematics", "Environmental Studies", "Art and Craft", "Physical Education"],
            "elective": [],
            "optional": []
        },
        "1": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "2": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "3": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "4": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "5": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "6": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "7": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "8": {
            "base": ["Hindi-literature", "Hindi_Grammar", "English-Literature", "English-Grammar", "Mathematics-I", "Mathematics-II", "Science", "Social-Studies", "General-Knowledge", "Drawing"],
            "elective": [],
            "optional": []
        },
        "9": {
            "base": ["Hindi", "English", "Mathematics", "Science", "Social Science"],
            "elective": [],
            "optional": ["Computer Applications", "Art Education", "Health and Physical Education"]
        },
        "10": {
            "base": ["Hindi", "English", "Mathematics", "Science", "Social Science"],
            "elective": [],
            "optional": ["Computer Applications", "Art Education", "Health and Physical Education"]
        },
        "11": {
            "base": ["Hindi", "English", "Physics", "Chemistry"],
            "elective": ["Mathematics", "Biology"],
            "optional": ["Computer Science", "Economics", "Physical Education", "Fine Arts", "Psychology", "Sociology"]
        },
        "12": {
            "base": ["Hindi", "English", "Physics", "Chemistry"],
            "elective": ["Mathematics", "Biology"],
            "optional": ["Computer Science", "Economics", "Physical Education", "Fine Arts", "Psychology", "Sociology"]
        }
    }


    class status(models.TextChoices):
        DRAFT='DF','DRAFT'
        PUBLISHED='PB','PUBLISHED'
class Newsletter(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    time=models.DateTimeField(default=timezone.now)
    class Meta:
        db_table='newsletter'

