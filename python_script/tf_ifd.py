import data_twitter_collect as data
import operator
import savedict_xlsj_json as Save
import math
import sys


def start(time,theme,sql,excel,json):
    """
        DataView(result): {'key':[tf,idf,tf-idf],...}
        :param time: The time to complete the task
        :type time: int
        :param theme: The theme of tweets search
        :type theme: str
        :param sql: If an SQL file is wanted 
        :type sql: bool
        :param excel: If an Excel file is wanted
        :type excel: bool
        :param json: If an JSON file is wanted
        :type json: bool
 
        :Example:
 
        >>> start(10,'instagood',True,True,True)
        >>> start(120,'israelBigData',True,True,True)
 
        .. seealso:: computeTF(),computeIDF(),computeTFIDF()
    """
    hasthtag=data.TweetExtract(time,theme).get_hasthtags()
    tf,idf,result=dict(),dict(),dict()
    def computeTF():
        """ 
        Term Frequency (tf): gives us the frequency of the word in each document in the corpus. 
        It is the ratio of number of times the word appears in a document compared to the total number of words in that document. 
        It increases as the number of occurrences of that word within the document increases. Each document has its own tf.
        tf(i,j)=(n(i,j)/SUMk(n(i,j)))
        """
        nonlocal tf
        nonlocal result
        for element in hasthtag['hasthtag']:
                if element not in tf:
                            tf[element]=hasthtag['hasthtag'].count(element)/float(len(hasthtag['hasthtag']))
                            result[element]=list()
                            result[element].append(tf[element])
    def computeIDF():
        """
        Inverse Data Frequency (idf): used to calculate the weight of rare words across all documents in the corpus.
        The words that occur rarely in the corpus have a high IDF score. It is given by the equation below.
        idf(w)=log10(N/df(t))
        """
        nonlocal idf
        nonlocal result
        for element in hasthtag['hasthtag']:
                if element not in idf:
                            idf[element]=math.log10(hasthtag['count_tweet']/float(hasthtag['hasthtag'].count(element)))
                            result[element].append(idf[element])
                            #result[element].append(idf[element]*tf[element])
    
    def computeTFIDF():
        """
        Combining these two we come up with the TF-IDF score (w) for a word in a document in the corpus. 
        It is the product of tf and idf:
        w(i,j)=tf*idf
        """
        for element in result.keys():
            result[element].append(result[element][0]*result[element][1])
    
    computeTF()
    computeIDF()
    computeTFIDF()

    if json:
        Save.save_to_json2(result)
        print('json ok')
        
    if excel:
        Save.save_to_xlsx(result)
        print('xlsx ok')
    if sql:
        Save.save_to_sql(result)
        print('sql ok')


if (__name__ == '__main__'):
    if(len(sys.argv)>1):
        json,xlsx,sql,argv_sys=False,False,False,sys.argv
        if 'xlsx' in argv_sys:
            xlsx=True
        if 'json' in argv_sys:
            json=True
        if 'sql' in argv_sys:
            sql=True
        start(int(argv_sys[1]),argv_sys[2],sql,xlsx,json)
    else:
        start(60,'instagood',True,True,True)



