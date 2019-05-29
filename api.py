# from flask import Flask
# from flask_restful import Resource, Api
# from flask_restful import reqparse
# from flaskext.mysql import MySQL

# app = Flask(__name__)
# api = Api(app)

# # MySQL 연결
# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'bituser'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'bituser'
# app.config['MYSQL_DATABASE_DB'] = 'bamboo'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

# class CreateUser(Resource):
#     def post(self):
#         try:
#             parser = reqparse.RequestParser()
#             parser.add_argument('email', type=str)
#             parser.add_argument('user_name', type=str)
#             parser.add_argument('password', type=str)
#             args = parser.parse_args()

#             _userEmail = args['email']
#             _userName = args['user_name']
#             _userPassword = args['password']

#             conn = mysql.connect()
#             cursor = conn.cursor()
#             cursor.callproc('sp_create_user', (_userEmail, _userName, _userPassword))
#             data = cursor.fetchall()

#             if len(data) is 0:
#                 conn.commit()
#                 return {'StatusCode': '200', 'Message': 'User creation success'}
#             else:
#                 return {'StatusCode': '1000', 'Message': str(data[0])}
#         except Exception as e:
#             return {'error': str(e)}





# # class setStory(Resource):
# #     def post(self):
# #         try:
# #             parser = reqparse.RequestParser()
# #             # TODO: storyNO
# #             parser.add_argument('storyCONTENT', type=str)
# #             # TODO: REGDATE
# #             parser.add_argument('USERID', type=str)
# #             # TODO: parser.add_argument('SONGID1', type=str)
# #             # TODO: parser.add_argument('SONGID2', type=str)
# #             # TODO: parser.add_argument('SONGID3', type=str)
# #             parser.add_argument('TITLE', type=str)

# #             args = parser.parse_args()

# #             # _storyNO = args['storyNO']
# #             _sotryContent = args['storyCONTENT']
# #             # _REGDATE = args['REGDATE']
# #             _USERID = args['USERID']
# #             # _SONGID1 = args['SONGID1']
# #             # _SONGID2 = args['SONGID2']
# #             # _SONGID3 = args['SONGID3']
# #             _TITLE = args['TITLE']
 
# class index(Resource):
#     def hello_world():
#         return 'Hello World!'
 


# #             conn = mysql.connect()
# #             cursor = conn.cursor()
# #             # TODO: create stored procedures 
# #             # cursor.callproc('sp_create_user', (_userEmail, _userName, _userPassword))
# #             data = cursor.fetchall()

# #             if len(data) is 0:
# #                 conn.commit()
# #                 return {'StatusCode': '200', 'Message': 'story creation success'}
# #             else:
# #                 return {'StatusCode': '1000', 'Message': str(data[0])}
# #         except Exception as e:
# #             return {'error': str(e)}






# api.add_resource(CreateUser, '/user')

# api.add_resource(index, '/')
# # api.add_resource(setStory, '/setStory')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)