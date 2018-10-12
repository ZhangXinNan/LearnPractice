import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def test(self):
        self.write('<form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form>')
    def get(self):
        self.test()
    def post(self):
        self.test()
    	self.write("post -----")
        #self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
