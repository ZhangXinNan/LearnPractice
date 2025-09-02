// 引入express 库
const express = require("express");
// 创建服务器实例
const app = express();
// const post = require("./routes/post");
const routes = require("./routes");
// 监听端口
const port = 3000;

// 让express能够解析json格式请求体
app.use(express.json());
// app.use(post);
routes(app);

// 使用listen来启动服务，并监听接口
app.listen(port, () => {
    console.log(`Express server listening at http://localhost:${port}`);
});

app.get("/", (req, res) => {
    res.send("Hello World!");
});

app.post("/", (req, res) => {
    console.log("收到请求体：", req.body);
    res.status(201).send();
});

app.put("/:id", (req, res) => {
    console.log("收到请求参数，id为：", req.params.id);
    console.log("收到请求体：", req.body);

    res.send();
});

app.delete("/:id", (req, res) => {
    console.log("收到请求参数，id为：", req.params.id);

    res.status(204).send();
});