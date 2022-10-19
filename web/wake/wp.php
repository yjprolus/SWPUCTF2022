<?php
class A
{
    private $are_you_a_hacker='yesyesyes';
}
$a=new A();
echo(serialize($a));
echo(urlencode(serialize($a)));
?>