from xlwt import Workbook
import json



def save_to_xlsx(args):
           """
        Save the result as an excel file (xlsx)
 
       the type of dictionary received must be written in the form {'test':[1,2,3]}
 
        :param a: the dictionary contains all hashtags with the result tf idf
        :type a: dict
 
        :Example:
 
        >>> save_to_xlsx({'test':[1,2,3]})
 
        """
           
           # création 
           book = Workbook()
            
           # création de la feuille 1
           feuil1 = book.add_sheet('sheet1')
           # ajout des en-têtes
           feuil1.write(0,0,'name')
           feuil1.write(0,1,'tf')
           feuil1.write(0,2,'idf')
           feuil1.write(0,3,'tf-idf')
           i=1
           # ajout des valeurs dans la ligne suivante
           for x, y in args.items():
                      ligne1 = feuil1.row(i)
                      i+=1
                      ligne1.write(0,x)
                      for k,element in enumerate(y,1):
                                 ligne1.write(k,element)
           # ajustement éventuel de la largeur d'une colonne
           feuil1.col(0).width = 10000
           book.save('result/result.xls')
                      

def save_to_json(args):
           """
        Save the result as an json file (.json)
 
        The type of dictionary received must be written in the form {'test':[1,2,3]}
 
        :param a: the dictionary contains all hashtags with the result tf idf
        :type a: dict
 
        :Example:
 
        >>> save_to_json({'test':[1,2,3]})
 
        """
           with open('result/result.json', 'w') as outfile:
                      json.dump(args, outfile)

def save_to_sql(args):
           fichier = open("result/result.sql", "w",encoding="utf-8")
           create_data="""
DROP TABLE IF EXISTS Tweet;
CREATE TABLE Tweet(
		Name VARCHAR(20) NOT NULL,
		IDF FLOAT(11) NOT NULL,
		TF FLOAT(11) NOT NULL,
		TF_IDF FLOAT(11) NOT NULL,
		PRIMARY KEY(Name));

TRUNCATE TABLE Tweet;           
           \n"""
           
           fichier.write(create_data)
           for k,v in args.items():
                    fichier.write("INSERT INTO Tweet (Name, IDF, TF, TF_IDF) VALUES('{}', {},{} ,{} );\n".format(k,v[0],v[1],v[2]))
           fichier.write("SELECT* FROM Tweet ORDER BY TF_IDF ASC;")
           fichier.close() 

def save_to_json2(args):
           li=[]
           for k,v in args.items():
                      li.append({'name':k,'value':{'tf':v[0] ,'idf':v[1],'tfidf':v[2] }})
           with open('result/result.json', 'w') as outfile:
                      json.dump(li, outfile)  
