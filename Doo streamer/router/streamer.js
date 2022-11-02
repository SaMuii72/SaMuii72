const express = require("express");
const router = express.Router();
const {Streamer} = require("../model/streamer")


//creat all todo
router.post("/streamer", async (req, res) => {
    let streamer = new Streamer(req.body);
    streamer = await streamer.save();
    res.status(200).send("Success");
  });

//get all todo
router.get("/streamer", async (req, res) => {
  const allStreamer = await Streamer.find();
  res.send(allStreamer);
});

//update todo
router.put("/streamer/:id", async (req, res) => {
  const streamer = await Streamer.findByIdAndUpdate(req.params.id, req.body, {
    new: true,
  });
  res.send("Update Success");
}); 

router.get("/streamer/:id", async (req, res) => {
    const streamer = await Streamer.findById(req.params.id);
    res.send(streamer);
  }); 
  


//delete todo
router.delete("/streamer/:id", async (req, res) => {
  const streamer = await Streamer.findByIdAndDelete(req.params.id);
  res.send("Delete Success");
});

module.exports = router;

