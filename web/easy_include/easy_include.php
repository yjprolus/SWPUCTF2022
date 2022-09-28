<?php
include_once "flag.php";
error_reporting(0);
function waf($file): bool
{
    if (preg_match('/http|info|https|utf|zlib|data|rot13|input|base64|log|sess/s', $file)) {
        return false;
    } else return true;
}

if (isset($_GET['key']) && waf(strtolower($_GET['key']))) {
    $key = call_user_func($_GET['key']);
    if ($key == "swpu") {
        $file = $_POST['file'];
        if (waf($file)) {
            include_once $file;
        } else {
            echo "Get Out Hacker!";
        }
    } else {
        echo "Wrong key!";
    }
} else {
    highlight_file(__FILE__);
}
