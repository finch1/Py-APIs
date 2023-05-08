# https://www.youtube.com/watch?v=GMppyAPbLYk
# https://www.ti.com/product/BQ769142
from importlib.metadata import requires
from flask import Flask 
from flask_restful import Api, Resource, reqparse # request is n object which can give us data sent by the client

app = Flask(__name__)
api = Api(app)

names = {
            "tim":{"age":19, "gender":"male"},
            "mik":{"age":20, "gender":"male"}
}
class HelloWorld(Resource): # inherets resource class
    '''
    def get(self, name, testnum):
        return {"data" : "Hello Worlds", "string" : name, "test" : testnum} # serializable data

    def post(self):
        return {"data" : "Posted"}
    '''
    def get(self, name):
        return names[name]
    
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required = True)
video_put_args.add_argument("views", type=int, help="Views of the video", required = True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required = True)

videos = { 
            1:{"name":"kids", "views":None, "likes":10}
}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    # def put(self, video_id):
    #     args = video_put_args.parse_args()# if set arguments are missing, a message is sent
    #     return {video_id:args}

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

# api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:testnum>") # add resource, <parameters>
# api.add_resource(HelloWorld, "/helloworld")
# api.add_resource(HelloWorld, "/helloworld/<string:name>")

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
