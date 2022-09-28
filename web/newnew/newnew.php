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

$newnew = unserialize($_GET['newnew']);
throw new Exception('can can need new new');