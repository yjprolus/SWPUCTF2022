 <?php
highlight_file(__FILE__);
error_reporting(0);
$a=0.58;
if (!preg_match('/[^0-9]/',$_GET['jiangnaij'])){
    if ((int)(substr(md5($_GET['jiangnaij']),0,6)) === 666666) {
        if (isset($_POST['pysnow']) and isset($_POST['M1sery']))
        {
            if ($_POST['pysnow'] != $_POST['M1sery'])
            {
                if (md5($_POST['pysnow']) == md5($_POST['M1sery'])){
                    if (isset($_POST['s0rry']) and isset($_POST['DSTBP']))
                    {
                        if ((string)$_POST['s0rry'] != (string)$_POST['DSTBP'])
                        {
                            if (md5($_POST['s0rry']) === md5($_POST['DSTBP'])) 
                            {
                                if ($_GET['csc8'] == intval($a * 100)){
                                    include '/flag.php';
                                    echo $flag;
                                }
                                else echo "csc8说你错了";
                            }
                            else echo 's0rry和DSTBP说你错了';
                        }
                        else echo "请输入不同的s0rry，DSTBP";
                    }
                    else echo "s0rry和DSTBP说快来玩";
                }
                else echo 'pysnow和M1sery说你错了';
            }
            else echo "请输入不同的pysnow，M1sery";
        }
        else echo "pysnow和M1sery说快来玩";
    }
    else echo "相等吗？？？";
}
else echo "输入一个数，这个数md5加密后前六位全是6！";
相等吗？？？