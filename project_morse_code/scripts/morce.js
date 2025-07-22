let ddtime=0;
let blanktime=0;
var id;
var word;
let words=[];


var morse_list = {
"11011":"あ","01":"い","001":"う","10111":"え","01000":"お",
"0100":"か","10100":"き","0001":"く","1011":"け","1111":"こ",
"10101":"さ","11010":"し","11101":"す","01110":"せ","1110":"そ",
"10":"た","0010":"ち","0110":"つ","01011":"て","00100":"と",
"010":"な","1010":"に","0000":"ぬ","1101":"ね","0011":"の",
"1000":"は","11001":"ひ","1100":"ふ","0":"へ","100":"ほ",
"1001":"ま","00101":"み","1":"む","10001":"め","10010":"も",
"011":"や","10011":"ゆ","11":"よ",
"000":"ら","110":"り","10110":"る","111":"れ","0101":"ろ",
"101":"わ","01001":"ゐ","01100":"ゑ","0111":"を","01010":"ん",

"゛":"00",//濁点
"゜":"00110",//半濁点
"ー":"01101",//長音
"、":"010101"//読点
}


function count(){
    words.push(2)
}


function cnv(){
    morse = words.join(",");
    try {
        word = morse_list[morse];
    } catch (error) {}
    words = []
}


function mousedown() {
    let start1 = performance.now();
    ddtime = start1;
    clearTimeout(id)
}


function mouseup() {
    let end1 = performance.now();
    let result = end1 - ddtime;
    if(result<=200){
        words.push(0); //ドット
    }else{
        words.push(1); //バー
    }
    id = setTimeout(cnv, "2000");
    rst.innerHTML = `${words}ms`;
    console.log(words);
}
