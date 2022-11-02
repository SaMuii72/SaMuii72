<template>
  <div class="hello"> <br>
 <h2 class="h2"> Thai Streamer </h2> <br>

<div class="center">
  <div class="dropdown">
    <div class="scrollbar" id="style-1">
    <button onclick="myFunction()" class="dropbtn">Game</button>
    <div id="myDropdown" class="dropdown-content">

      <div class="search-container">
        <form action="">
          <input type="text" id="myInput" onkeyup="searchFunction()" placeholder="Find Game.." name="search">
          <button type="submit"><i class="fa fa-search"></i></button>
        </form>
      </div> 
<br>
<ul id="myUL">
      <div class="checkboxs">
      <li><label for="01"><input id="01" value="01" class="check" type="checkbox"> GTA </label> 
      </li></div>
      <div class="checkboxs">
        <li><label for="02"><input id="02" value="02" class="check" type="checkbox"> Super People</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="03"><input id="03" value="03" class="check" type="checkbox"> PUBG</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="04"><input id="04" value="04" class="check" type="checkbox"> Overwatch 2</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="05"><input id="05" value="05" class="check" type="checkbox"> VALORANT</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="06"><input id="06" value="06" class="check" type="checkbox"> Rust</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="07"><input id="07" value="07" class="check" type="checkbox"> Call of Duty</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="08"><input id="08" value="08" class="check" type="checkbox"> DEVOUR</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="09"><input id="09" value="09" class="check" type="checkbox">Dota 2</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="10"><input id="10" value="10" class="check" type="checkbox"> FIFA 23</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="11"><input id="11" value="11" class="check" type="checkbox"> Inside the Backrooms</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="12"><input id="12" value="12" class="check" type="checkbox"> Fortnite</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="13"><input id="13" value="13" class="check" type="checkbox">League of Legends</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="14"><input id="14" value="14" class="check" type="checkbox"> Dead by Daylight</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="15"><input id="15" value="15" class="check" type="checkbox"> Grounded</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="16"><input id="16" value="16" class="check" type="checkbox"> Minecraft</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="17"><input id="17" value="17" class="check" type="checkbox"> Lunch Lady</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="18"><input id="18" value="18" class="check" type="checkbox"> Apex Legends</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="19"><input id="19" value="19" class="check" type="checkbox"> Rainbow Six Siege</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="20"><input id="21" value="21" class="check" type="checkbox"> Goose Goose Duck</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="19"><input id="19" value="19" class="check" type="checkbox"> Rainbow Six Siege</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="19"><input id="19" value="19" class="check" type="checkbox"> Rainbow Six Siege</label>
        </li></div>
      <div class="checkboxs">
        <li><label for="19"><input id="19" value="19" class="check" type="checkbox"> Rainbow Six Siege</label>
        </li></div>
    </ul>
    </div> </div>
  </div>  

  <div class="dropdown1">
    <button onclick="myFunction1()" class="dropbtn1">Gender</button>
    <div id="myDropdown1" class="dropdown-content1">
      <div class="checkboxs1">
        <label><input class="check1" type="checkbox"> Male</label> <br>
      </div>
      <div class="checkboxs1">
        <label><input class="check1" type="checkbox"> Female</label>
      </div>
    </div>
  </div>

  <div class="dropdown2">
    <button onclick="myFunction2()" class="dropbtn2">Platform</button>
    <div id="myDropdown2" class="dropdown-content2">
      <div class="checkboxs2">
        <label><input class="check2" type="checkbox"> Youtube</label> 
      </div>
      <div class="checkboxs2">
        <label><input class="check2" type="checkbox"> Facebook</label> <br>
      </div>
      <div class="checkboxs2">
        <label><input class="check2" type="checkbox"> Twitch</label>
      </div>
    </div>
  </div>

  <div class="dropdown3">
    <button onclick="myFunction3()" class="dropbtn3">Customize</button>
    <div id="myDropdown3" class="dropdown-content3">
      <div class="checkboxs3">
        <label><input class="check3" type="checkbox"> Most-Low Followers </label> 
      </div>
      <div class="checkboxs3">
        <label><input class="check3" type="checkbox">  Low-Most Followers </label> <br>
      </div>
      <div class="checkboxs3">
        <label><input class="check3" type="checkbox"> Recommend </label>
      </div>
    </div>
  </div>
</div>  <br>  

<router-link v-for="s in streamer" :key="s._id" :to="'/info/' + s._id" >
<button onclick="buttonFunction()" class="introduce"> <img class="Profilepicture" :src="s.Profile"/>
<br> <p> {{s.Name}} </p>  <p> {{s.Game}} </p>  <p> {{s.Platform}} </p> 
</button> </router-link> <br> <br>
  
<br>
    <div class="page">
        <div class="pagination">
        <a href="#">&laquo;</a>
        <a href="#" class="active">1</a>
        <a href="#">2</a>
        <a href="#">3</a>
        <a href="#">4</a>
        <a href="#">5</a>
        <a href="#">6</a>
        <a href="#">&raquo;</a>
    </div>
</div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
      streamer:[]
    }
  },
  methods:{
    async getStreamer(){
      const response = await axios.get("http://localhost:3000/streamer" );
      console.log(response);
      this.streamer = response.data;
    }
  },
  mounted(){
    this.getStreamer();  
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap');
*{
  margin: 0;
  padding: 0;
  font-family:  'Rubik', sans-serif;
  text-align: center;
  box-sizing: border-box;
}

.Profilepicture{
  width: 90px;
}

.dropbtn {
  background-color: #ddd;
  color: black;
  padding: 10px 20px;
  margin: 4px 2px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  border-radius: 16px;
}

.dropbtn:hover, .dropbtn:focus {
  background-color: #ddd;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  background-color: #f1f1f1;
  width: 260px;
  height: 250px;
  border-radius: 16px;
  overflow: auto;
  position: absolute;
}


.dropdown-content a {
  color: black;
  padding: 10px 20px;
  text-decoration: none;
  display: block;
}

.dropdown a:hover {background-color: #ddd;}

.show {display: block;}

.checkboxs{
  display: flex;
  align-items: center;
}

.checkboxs .check{
  width: 20px;
  height: 20px;
  margin-top: 8px;
  margin-left: 25px;
  vertical-align: bottom;
  position: relative;
}


/* Gender */
.dropbtn1 {
  background-color: #ddd;
  color: black;
  padding: 10px 20px;
  margin: 4px 2px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  border-radius: 16px;
}

.dropbtn1:hover, .dropbtn1:focus {
  background-color: #ddd;
}

.dropdown1 {
  position: relative;
  display: inline-block;
}

.dropdown-content1 {
  display: none;
  background-color: #f1f1f1;
  width: 110px;
  height: 80px;
  border-radius: 16px;
  position: absolute;
}

.dropdown-content1 a {
  color: black;
  padding: 10px 20px;
  text-decoration: none;
  display: block;
}

.dropdown1 a:hover {background-color: #ddd;}

.show {display: block;}

.checkboxs1{
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 8px;
}
.checkboxs1 .check1{
  width: 20px;
  height: 20px;
  margin-top: 5px;
  margin-left: 25px;
  vertical-align: bottom;
  position: relative;
}

label {
  display: block;
  text-indent: -10px;
  font-size: 16px;
}

/* Platform */
.dropbtn2 {
  background-color: #ddd;
  color: black;
  padding: 10px 20px;
  margin: 4px 2px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  border-radius: 16px;
}

.dropbtn2:hover, .dropbtn2:focus {
  background-color: #ddd;
}

.dropdown2 {
  position: relative;
  display: inline-block;
}

.dropdown-content2 {
  display: none;
  background-color: #f1f1f1;
  width: 130px;
  height: 115px;
  border-radius: 16px;
  position: absolute;

}

.dropdown-content2 a {
  color: black;
  padding: 10px 20px;
  text-decoration: none;
  display: block;
}

.dropdown2 a:hover {background-color: #ddd;}

.show {display: block;}

.checkboxs2{
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 8px;
}
.checkboxs2 .check2{
  width: 20px;
  height: 20px;
  margin-top: 5px;
  margin-left: 25px;
  vertical-align: bottom;
  position: relative;
}

label {
  display: block;
  text-indent: -10px;
  font-size: 16px;
}


/* Customize */
.dropbtn3 {
  background-color: #ddd;
  color: black;
  padding: 10px 20px;
  margin: 4px 2px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  border-radius: 16px;
}

.dropbtn3:hover, .dropbtn3:focus {
  background-color: #ddd;
}

.dropdown3 {
  position: relative;
  display: inline-block;
}

.dropdown-content3 {
  display: none;
  background-color: #f1f1f1;
  width: 220px;
  height: 115px;
  border-radius: 16px;
  position: absolute;

}

.dropdown-content3 a {
  color: black;
  padding: 10px 20px;
  text-decoration: none;
  display: block;
}

.dropdown3 a:hover {background-color: #ddd;}

.show {display: block;}

.checkboxs3{
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 8px;
}
.checkboxs3 .check3{
  width: 20px;
  height: 20px;
  margin-top: 5px;
  margin-left: 25px;
  vertical-align: bottom;
  position: relative;
}

label {
  display: block;
  text-indent: -10px;
  font-size: 16px;
}
/* button1 */
.introduce{
  background-color: #ddd;
  color: black;
  padding: 10px 20px;
  width: 12%;
  height: 12%;
  font-size: 16px;
  border: none;
  border-radius: 16px;
  margin-left: 16px;
  float: left;
  position: relative;
}


/* pagination */
.page {
  text-align: center;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

}

.pagination {
  text-align: center;
}

.pagination a {
  color: black;
  float: left;
  padding: 8px 16px;
  text-decoration: none;
  transition: background-color .3s;
  border-radius: 18px;

}

.pagination a.active {
  background-color: dodgerblue;
  color: white;
  border-radius: 18px;

}

.pagination a:hover:not(.active) {background-color: #ddd;}
</style>
