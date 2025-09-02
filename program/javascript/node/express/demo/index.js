const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/datas', (req, res)=>{
    console.log("get---");
    console.log(req.query);
    res.send("响应内容");
});

app.post('/datas', (req, res)=>{
    console.log("post---");
    console.log(req.body);
    res.send("响应内容");
});

app.listen(PORT, ()=>{
    console.log(`Server running at http://localhost:${PORT}`);
});


