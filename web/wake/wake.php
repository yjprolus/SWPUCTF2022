<?php
highlight_file(__FILE__);
class A
{
    private $are_you_a_hacker;

    public function __destruct()
    {
        if ($this->are_you_a_hacker == 'yesyesyes')
        {
            echo "flag";
        } else {
            echo 'Night Night, Makka Pakka';
        }
    }

    public function __wakeup()
    {
        $this->are_you_a_hacker = 'nonono';
    }
}

unserialize($_POST['data']);