const bodyParser = require("body-parser");
const express = require("express");
const app = express();
const mongoose = require("mongoose")
const cors = require("cors");


// Middleware
app.use(cors());
app.use(bodyParser.json());

mongoose.connect("mongodb+srv://admin:admin123@cluster0.ehri9.mongodb.net/mydb?retryWrites=true&w=majority"
).then(() => {
    console.log("Database Connected");
  });

//import router  

const streamerRouter = require("./router/streamer");
const productRouter = require("./router/product");
const todoRouter = require("./router/td");

//use router  

app.use("/", todoRouter);
app.use("/", streamerRouter);
app.use("/", productRouter);

app.listen("3000",() =>{
    console.log("Listen to port 300");
});

