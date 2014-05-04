function runit(code, output, canvas) {
    var prog = document.getElementById(code).value;
    var mypre = document.getElementById(output);
    mypre.innerHTML = '';
    Sk.canvas = canvas;
    Sk.pre = output;
    Sk.configure({
        output:function(text) {
            var mypre = document.getElementById(output);
            mypre.innerHTML = mypre.innerHTML + text;
        },
        read:function(x) {
            if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                throw "File not found: '" + x + "'";
            return Sk.builtinFiles["files"][x];
        }
    });
    eval(Sk.importMainWithBody("<stdin>",false,prog));
}
