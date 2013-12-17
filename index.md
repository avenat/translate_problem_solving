---
layout: page
title: Hello World!
tagline: Supporting tagline
---
{% include JB/setup %}

## Добро пожаловать на страницу перевода книги "Problem Solving with Algorithms and Data Structures Using Python"
    <canvas id="mycanvas"  height="500" width="800"
        style="border-style: solid;"></canvas>

<textarea id="code" rows="24" cols="80">
import turtle
wn = turtle.Screen()

babbage = turtle.Turtle()
babbage.shape("triangle")

n = 8
angle = 360/n

for i in range(n):
    babbage.right(angle)
    babbage.forward(90)
    babbage.stamp()

wn.exitonclick()
</textarea>
    <script>
        var prog = document.getElementById("code").value;
        function builtinRead(x) {
            if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                    throw "File not found: '" + x + "'";
            return Sk.builtinFiles["files"][x];
        }
        Sk.configure({read:builtinRead});
        Sk.canvas = "mycanvas";
        try {
            var module = Sk.importMainWithBody("<stdin>", false, prog);
        } catch (e) {
            alert(e);
        }
    </script>
