
const express = require("express");
var route = express.Router();


route.get("/", (req, res) => {
    res.send("Hello World!");
});

route.post("/", (req, res) => {
    console.log("收到请求体：", req.body);
    res.status(201).send();
});

route.put("/:id", (req, res) => {
    console.log("收到请求参数，id为：", req.params.id);
    console.log("收到请求体：", req.body);

    res.send();
});

route.delete("/:id", (req, res) => {
    console.log("收到请求参数，id为：", req.params.id);

    res.status(204).send();
});

module.exports = route;
