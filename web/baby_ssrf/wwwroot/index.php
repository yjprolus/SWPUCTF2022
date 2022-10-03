<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>欢迎大家</title>
    <style>
        *{box-sizing: border-box;}
        body{
            background: #000;
            margin: 0;
            padding: 0;
            overflow: hidden;
            text-shadow: 0px 0px 80px;
        }
        .jiangnaij{
            font-size: 120px;
        }
        h1{
            margin: 0;
            padding: 0;
            font-size: 90px;
            color: #fff;
            text-shadow: #d56238 0px 6px,
            #d56238 2px 0px,
            #d56238 -2px 0px,
            #d56238 0px -2px,
            #d56238 -1.4px -1.4px,
            #d56238 1.4px 1.4px,
            #d56238 1.4px -1.4px,
            #d56238 -1.4px 1.4px;

        }
        a{color: #fff;}
        /* 盒子↓ */
        p{
            margin: 0;
        }
        .box{
            /* 盒子宽度↓ ---最好别改*/
            width: 700px;
            /* 让视频居中对齐↓---最好别动 */
            text-align: center;
            /* border: 1px solid #f00; */
            color: #fff;

            position: absolute;
            margin: 20px auto 0;
            top: 20px;
            left: 0;
            right: 0;
        }
        /* 图片样式↓ */

        img{
            /* 视频宽度↓ ---最好不要大于上面盒子的宽度*/
            width: 700px;
            height: 390px;
            /* 灰色的描边↓ ---px是粗细 solid是实线 #555是颜色代码 可以百度html颜色代码修改*/
            border: 2px solid #222;
            /* 图片的圆角 */
            border-radius: 5px;
            /* 动画时间 */
            transition: 0.8s;
        }
        .img2:hover{border: 2px solid #980b18}

        .box>div{
            padding: 20px;
            /* border: 1px solid #f00; */
        }
        .szj{
            position: absolute;
            top: 0;
            left: 0;
            color: #fff;
            padding: 5px;
            border: 1px solid #eee;
            background-color: rgb(0,0,0,0.7)
        }
        .yl{
            display: inline;
            border-bottom:1px dotted #0ff;
        }
        .yl a{
            text-decoration: none;
            color:#c6d491;

        }
        .yl span{
            margin-right: 8px;
        }
    </style>
</head>
<body>
<canvas id="canvas"></canvas>
<div class="box">
    <!-- 图片部分 -->
    <br>
    <br>
    <br>
    <br>
    <br>
    <br><br>
    <br>

    <div class="text">
        <h1>听说源码泄露有好多种可能</h1>
        <h1 class="jiangnaij">
            ！！
        </h1>

        <br>


    </div>
</div>


<!-- 以下js -->


<script>
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');


    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
    // 下面的雷军就是代码雨的文字
    var texts = 'jiangnaij'.split('');

    var fontSize = 16;
    var columns = canvas.width/fontSize;
    // 用于计算输出文字时坐标，所以长度即为列数
    var drops = [];
    //初始值
    for(var x = 0; x < columns; x++){
        drops[x] = 1;
    }

    function draw(){
        //让背景逐渐由透明到不透明
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        //文字颜色
        ctx.fillStyle = '#ff0000';
        ctx.font = fontSize + 'px arial';
        //逐行输出文字
        for(var i = 0; i < drops.length; i++){
            var text = texts[Math.floor(Math.random()*texts.length)];
            ctx.fillText(text, i*fontSize, drops[i]*fontSize);

            if(drops[i]*fontSize > canvas.height || Math.random() > 0.95){
                drops[i] = 0;
            }

            drops[i]++;
        }
    }
    setInterval(draw, 33);
</script>
</body>



<?php
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
    $host=$x['host'];
    if((substr($host)<=7)){
        $swpu=curl_init($url);
        curl_setopt($swpu, CURLOPT_HEADER, 0);
        curl_setopt($swpu, CURLOPT_RETURNTRANSFER, 1);
        $result=curl_exec($swpu);
        curl_close($swpu);
        echo ($result);
    }
    else{
        die('hacker！');
    }
}
else{
    die('怎么做？');
}
?>
</html>