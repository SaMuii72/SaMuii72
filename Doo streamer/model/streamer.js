const mongoose = require("mongoose")
const streamerSchema =  mongoose.Schema({
    Name: {
        type: String,
    },
    Description:{
        type: String,
    },
    Profile:{
        type: String,
    },
    Img:{
        type: String,
    },
    Follower:{
        type: String,
    },
    Game:{
        type: String,
    },
    Platform:{
        type: String,
    },
    Stream:{
        type: String,
    },
    Facebook:{
        type: String,
    },
    Tiktok:{
        type: String,
    },
    Youtube:{
        type: String,
    },
    Instargram:{
        type: String,
    },
});

exports.Streamer = mongoose.model("streamer",streamerSchema)