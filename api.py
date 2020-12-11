import cx_Oracle
from flask import Flask, request,jsonify,render_template
import json
from flask_restful import Resource, Api


# using flask_restful

app =  Flask(__name__)
api = Api(app)
res=[]


@app.route("/")
def getConnection():


    import cx_Oracle
    import json
    from itertools import zip_longest
        
    host = 'localhost/orcl'  # hostaddr:port
    uname = 'RAVI'
    pw = '9833504978'
    constr=uname+'/'+pw+'@'+host   
    con= cx_Oracle.connect(constr,encoding = "UTF-8", nencoding = "UTF-8")
    cur=con.cursor()
    cur.execute('select * from NEWS_VIEW ')
    data=cur.fetchall()
    news_list=[]
    for index, row in enumerate(data):
        news_list.append(row)


    lenght = len(news_list)
    keys=['Category: ','Title: ','Description: ','Date: ','Read More: ']
    

    for i in range (lenght):
        a = dict(zip(keys,news_list[i]))
        res.append(a)
        
        final=json.dumps(res)
        
        

    return jsonify(final)


@app.route("/news",methods=['GET'])
def id():
    final=json.dumps(res)
    if 'news_id' in request.args:
        news_id = int(request.args['news_id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results=[]
    for book in final:
         if book[news_id] == news_id:
            results.append(book)
         
    return (results)

if __name__ == '__main__':
    app.run(debug=True)