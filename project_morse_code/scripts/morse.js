let ddtime=0;
let blanktime=0;
var interval = 300
var id;
var word = "";
let words=[];


var morse_list = {
"ーー・ーー":"あ","・ー":"い","・・ー":"う","ー・ーーー":"え","・ー・・・":"お",
"・ー・・":"か","ー・ー・・":"き","・・・ー":"く","ー・ーー":"け","ーーーー":"こ",
"ー・ー・ー":"さ","ーー・ー・":"し","ーーー・ー":"す","・ーーー・":"せ","ーーー・":"そ",
"ー・":"た","・・ー・":"ち","・ーー・":"つ","・ー・ーー":"て","・・ー・・":"と",
"・ー・":"な","ー・ー・":"に","・・・・":"ぬ","ーー・ー":"ね","・・ーー":"の",
"ー・・・":"は","ーー・・ー":"ひ","ーー・・":"ふ","・":"へ","ー・・":"ほ",
"ー・・ー":"ま","・・ー・ー":"み","ー":"む","ー・・・ー":"め","ー・・ー・":"も",
"・ーー":"や","ー・・ーー":"ゆ","ーー":"よ",
"・・・":"ら","ーー・":"り","ー・ーー・":"る","ーーー":"れ","・ー・ー":"ろ",
"ー・ー":"わ","・ー・・ー":"ゐ","・ーー・・":"ゑ","・ーーー":"を","・ー・ー・":"ん",

"・・":"゛",//濁点
"・・ーー・":"゜",//半濁点
"・ーー・ー":"ー",//長音
"・ー・ー・ー":"、"//読点
}


//モールスを日本語に変換
function cnv(){
    morse = words.join("");
    if(morse_list[morse]!==NaN && morse_list[morse]!==undefined){
        word += morse_list[morse];
        rst.innerHTML = `${word}`;
    }else{
        rst.innerHTML = `入力が違います`;
    }
    words = [];
    console.log(word);
}


//入力をモールス信号に変換
function mousedown() {
    let start1 = performance.now();
    ddtime = start1;
    clearTimeout(id);
}
function mouseup() {
    let end1 = performance.now();
    let result = end1 - ddtime;
    if(result<=200){
        words.push("・"); //ドット
    }else{
        words.push("ー"); //バー
    }
    str = words.join("")
    id = setTimeout(cnv, interval);
    morse_ja.innerHTML = `${str}`;
}
