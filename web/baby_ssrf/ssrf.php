<?php
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
    $host=$x['host'];
    if((substr($host)<=7)){
        $swpu=curl_init($url);
        curl_setopt($swpu, CURLOPT_HEADER, 0);
        curl_setopt($swpu, CURLOPT_RETURNTRANSFER, 1);
        $result=curl_exec($swpu);
        curl_close($swpu);
        echo ($result);
    }
    else{
        die('hacker！');
    }
}
else{
    die('怎么做？');
}
?>