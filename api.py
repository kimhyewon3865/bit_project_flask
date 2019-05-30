from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL

# konlpy
from collections import Counter
from konlpy.tag import Twitter

# logging
import logging


app = Flask(__name__)

# MySQL 연결
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'bituser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bituser'
app.config['MYSQL_DATABASE_DB'] = 'bit_project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getSongs')
def get_songs():
    return 'Hello World!'

    
@app.route('/test')
def test():
    try:
        # JSON parameter 
        parser = reqparse.RequestParser()
        parser.add_argument('sotryNo', type=str)
        parser.add_argument('title', type=str)
        parser.add_argument('storyContent', type=str)
        args = parser.parse_args()

        _sotryNo = args['sotryNo']
        _title = args['title']
        _storyContent = args['storyContent']
        
        # 사연 fre1~5 변수 얻기
        nlp = Twitter() 
        nouns = nlp.nouns(_storyContent)
        count = Counter(nouns)

        result = [] 

        # 사연 fre1~5 result 배열에 저장
        for letter, i in count.most_common(5):
            result.append(str(letter))
            # logging.warning("type: ", type(letter))
        

        # logging.warning("hyewon result: ", result, type(result[0]))


        # DB 설정1
        conn = mysql.connect()
        cursor = conn.cursor()

        # TODO: 노래 추천 알고리즘

        # 사연 fre1~5 가 속한 노래DB 데이터 얻기
        sql = ' select songid, fre1, fre2, fre3, fre4, fre5 from song WHERE (FRE5 or FRE4 or FRE3 or FRE2 or FRE1) IN (%s, %s, %s, %s, %s)'
        cursor.execute(sql, (result[0],result[1],result[2],result[3],result[4]))
        rows = cursor.fetchall()
            
        # logging.warning('rows: ', rows) #logging



        newRows = []


        for row in rows:
            l = list(row)
            l.append(0)
            newRows.append(l)

        # logging.warning(newRows)
       
        for row in newRows:
            for i in range(1,6):
                if result[0] == row[i]:
                    row[-1] += ((6-i) * 4)
                if result[1] == row[i]:
                    row[-1] += ((6-i) * 4)
                if result[2] == row[i]:
                    row[-1] += ((6-i) * 4)
                if result[3] == row[i]:
                    row[-1] += ((6-i) * 4)
                if result[4] == row[i]:
                    row[-1] += ((6-i) * 4)
        # logging.warning("newRows: ", newRows)      

        # 노래 3곡 songid get
        newRows.sort(key=lambda x:x[6] , reverse=True)
          
        for i in range(0,3):
            print("song_id :",newRows[i][0], "score : ", newRows[i][6])
        
        a="A"
        

        #업데이트
        # conn = mysql.connect()
        # cursor = conn.cursor()
        sql = 'update story set songid1 = %s, songid2 = %s, songid3 = %s where storyno = %s'
        cursor.execute(sql, (newRows[0][0],newRows[1][0],newRows[2][0], str(_sotryNo)))
        data = cursor.fetchall()
        conn.commit()

        if len(data) is 0:
            conn.commit()
            return {'StatusCode': '200', 'Message': 'User creation success'}
        else:
            return {'StatusCode': '1000', 'Message': str(data[0])}

    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)