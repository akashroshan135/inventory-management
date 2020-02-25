//used to render a custom alert box
function custom_alert(){
    this.render = function(dialog){  
        var winW = window.innerWidth;
        var winH = window.innerHeight;
        var dialogoverlay = document.getElementById('dialogoverlay');
        var dialogbox = document.getElementById('dialogbox');
        dialogoverlay.style.display = "block";
        dialogoverlay.style.height = winH+"px";
        dialogbox.style.left = (winW/2) - (550 * .5)+"px";
        dialogbox.style.top = "100px";
        dialogbox.style.display = "block";
        
        document.getElementById('dialogboxhead').innerHTML = "Error";
        document.getElementById('dialogboxbody').innerHTML = dialog;
        document.getElementById('dialogboxfoot').innerHTML = '<button onclick="custom_alert.ok()" class="ghost-red">Okay</button>';
    }
    this.ok = function(){
        document.getElementById('dialogbox').style.display = "none";
        document.getElementById('dialogoverlay').style.display = "none";
    }
}
