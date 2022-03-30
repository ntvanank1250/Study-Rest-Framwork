import datetime
from flask import Flask
from flask_restful import Resource, Api
from flask import request
from functools import wraps
from flask_httpauth import HTTPBasicAuth

app =Flask(__name__)
api =Api(app)
auth=HTTPBasicAuth()
USER_DATA={
    "admin":"admin"
}
data=[]

@auth.verify_password
def verify(username, password):
    if not(username and password):
        return False
    return USER_DATA.get(username)== password

def time(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        s= datetime.datetime.now()
        _ = function(*args,**kwargs)
        e=datetime.datetime.now()
        print("Execution Time:{}".format(e-s))
        return _
    return wrapper

def monitor(function=None):
    @wraps(function)
    def wrapper(*args,**kwargs):
        _ =function(*args,**kwargs)
        print("Ip Address:{}".format(request.remote_user))
        print("Cookies:{}".format(request.cookies))
        print(request.user_agent)
        return _
    return wrapper

class People(Resource):
    @time
    @monitor
    @auth.login_required
    def get(self,name):
        for x in data:
            if x['Data']==name:
                return x
            return {'Data':None}
    
    @time
    @monitor
    @auth.login_required

    def post(self, name):
        temp = {'Data': name}
        data.append(temp)
        return temp

    @time
    @monitor
    @auth.login_required

    def delete(self, name):
        for ind,x in enumerate(data):
            if x['Data']==name:
                data.pop(ind)
                return {'note':'Deleted'}

api.add_resource(People,'/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)