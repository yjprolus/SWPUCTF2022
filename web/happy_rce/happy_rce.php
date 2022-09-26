 <?php
error_reporting(0);
header("Content-Type:text/html;charset=utf-8");
highlight_file(__FILE__);
if (isset($_GET['url'])) {
  $ip=$_GET['url'];
  if(preg_match("/cat|flag| |[0-9]|\*|more|wget|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $ip)){
      die('换个方法吧？被过滤啦！');
  }
  eval($ip);
}
?> 
