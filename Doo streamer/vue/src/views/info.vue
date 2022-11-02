<template>
    <div class="information"> <br> 
    <img src="" alt="">
    <h1 class="h2" id="Name">  {{streamer.Name}} </h1> 
    <h2 class="Followers">  {{streamer.Follower}} </h2> 
    <p class="Discription"> {{streamer.Description}} </p>
    <p class="Gameplay"> {{streamer.Game}} </p>
    <div class="info"> <br> <br>
      <img src="" alt="">
      <h1 class="h2" id="Live stream/Video"> Live stream/Video </h1> 
      <h1 class="Follow"> ช่องทางการติดตาม </h1> 
      <iframe src="https://player.twitch.tv/?channel=edwin_live&parent=www.example.com" frameborder="0" allowfullscreen="true"  height="378" width="620"></iframe>
      <a  id="twitchbutton" href="https://www.twitch.tv/edwin_live">Twitch</a> <br>
      <a  id="facebutton" href="https://www.facebook.com/OfficialEdwins">Facebook</a>
   
    </div> 
</div> 
</template>

<script>
  import axios from "axios";
  export default {
    data(){
      return{
        streamer:[]
      }
    },
    methods:{
      async getStreamer(){
        const id = this.$route.params.id
        const response = await axios.get("http://localhost:3000/streamer/" + id);
        console.log(response);
        this.streamer = response.data;
      }
    },
    mounted(){
      this.getStreamer();  
    }
  }
</script>
<style scoped>
.Discription{
    font-family: 'Mitr', sans-serif;
    font-size: 20px;
}

.Gameplay{
    font-family: 'Mitr', sans-serif;
    font-size: 20px;
}

.information{
    background-color: #ddd;
    border: 2px solid #ddd;
    padding: 10px;
    border-radius: 1rem;  
    width: 1600px;
    height: 800px;
    margin-left: 150px;
}
.information .info .h2{
  text-align: left;
  position: absolute;
  margin-left: 10%;
}

.information .info .Follow{
  text-align: right;
  position: absolute;
  margin-left: 55%;
}

.information .info .Follow{
  font-family: 'Mitr', sans-serif;
    font-size: 20px;
}
.information .info a#twitchbutton{
  padding: 6px 16px;
  font-size: 16px;
  position: absolute;
  margin-top: 60px;
  margin-left: 16%;
  border: none;
  border-radius: 18px;
  background-color: #6441a5;
  text-decoration: none;
  color: black;
}
.information .info a#facebutton{
  padding: 6px 16px;
  font-size: 16px;
  position: absolute;
  margin-top: 80px;
  margin-left: 15.5%;
  border: none;
  border-radius: 18px;
  background-color: dodgerblue;
  text-decoration: none;
  color: black;
}

.information .info iframe{
  text-align: left;
  position: fixed;
  right: 55%;
  margin-right: 50px;
  margin-top: 75px;
}
</style>
