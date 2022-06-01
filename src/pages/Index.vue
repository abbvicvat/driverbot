<template>
  <q-page id="body" class="bg-grey-3">
    <div id="buttons">

      <div id="row1">
        <div id="button-w" class="button">
          W
        </div>
      </div>

      <div id="row2">
        <div id="button-a" class="button">
          A
        </div>

        <div id="button-s" class="button">
          S
        </div>

        <div id="button-d" class="button">
          D
        </div>
      </div>
      
    </div>
    <div id="logdiv">
      <p v-for="message in log_list" :key="message"> {{message}} </p>
    </div>
  </q-page>
</template>

<script>
import { client } from "../boot/mqtt-boot";
export default {
  created() {
    client.on("connect", () => {
      console.log("Conntected!");
      client.subscribe("vicvat", function (err) {
        if (!err) {
          let info = JSON.stringify({
            user: "jeton",
            message: "Hello mqtt",
          });
          client.publish("vicvat", info);
        }
      });
    });
  },
  mounted() {
    function publish(topic, message) {
      let info = JSON.stringify({
        user: "vicvat",
        message: message,
      });
      client.publish("vicvat/" + topic, info);
    }

    document.onkeydown = (event) => {
      //console.log(event);
      let key = event.key.toLowerCase(), message, send = false;
  
      if(key==='w' && this.forward != 1) {
        send = true;
        this.forward=1;
        publish("speed", 1);

        message = "push W"
        this.speed += 1;
      }

      if(key==='a' && this.left != 1) {
        send = true;
        this.left=1;
        publish("turn", 1);

        message = "push A"
        this.turn += 1;
      }

      if(key==='s' && this.back != 1) {
        send = true;
        this.back=1;
        publish("speed", -1);

        message = "push S"
        this.speed -= 1;
      }

      if(key==='d' && this.right != 1) {
        send = true;
        this.right=1;
        publish("turn", -1);

        message = "push D"
        this.turn -= 1;
      }

      if(send) this.log_list.push(message);
    }

    document.onkeyup = (event) => {
      let key = event.key.toLowerCase(), message, send = false;
      if(key==='w') {
        send = true;
        this.forward = 0;
        publish("speed", -1);

        message = "release W"
        this.speed -= 1;
        console.log(this.speed);
      }

      if(key==='a') {
        send = true;
        this.left = 0;
        publish("turn", -1);
        
        message = "release A"
        this.turn -= 1;
      }

      if(key==='s') {
        send = true;
        this.back = 0;
        publish("speed", 1);

        message = "release S"
        this.speed += 1;
      }

      if(key==='d') {
        send = true;
        this.right = 0;
        publish("turn", 1);

        message = "release D"
        this.turn += 1;
      }
      
      if(send) this.log_list.push(message);
    }
  },

  data() {
    return {
      log_list: [],
      forward: 0,
      back: 0,
      left: 0,
      right: 0,
      speed: 0,
      turn: 0,
    };
  },

  watch: {
    speed: function(speed) {

      let message = "MOVING ";
      if(speed === -1)  message += "BACK";
      if(speed === 0)  message = "NOT MOVING";
      if(speed === 1)  message += "FORWARD";

      this.log_list.push(message);
    },

    turn: function(turn) {
      let message = "TURNING ";
      if(turn === -1)  message += "LEFT";
      if(turn === 0)  message = "NOT TURNING";
      if(turn === 1)  message += "RIGHT";

      this.log_list.push(message);
    }
  }
};
</script>

<style scoped>
  #body {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  #row2 {
    display: flex;
  }

  #buttons {
    height: 40vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
  }

  .button {
    display: flex;
    justify-content: center;
    align-items: center;

    background: grey;
    border-radius: 5px;
    width: 10vh;
    height: 10vh;


    
    margin-left: 2px;
    margin-right: 2px;
    margin-bottom: 5px;
  }

  #logdiv {
    display: inline-block;
    overflow-y: scroll;

    border-radius: 5px;

    margin-top: 3vh;  
    height: 50vh;
    width: 40vw;
    padding-left: 10px;

    background: #202020;
    color: #DDDDDD
  }

</style>