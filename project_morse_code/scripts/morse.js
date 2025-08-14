let ddtime=0;
let blanktime=0;
var interval = 300
var id;
var word = "";
var words=[];

const morse_list = {
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

const morsecodeMap = {
"あ":"ーー・ーー","い":"・ー","う":"・・ー","え":"ー・ーーー","お":"・ー・・・",
"か":"・ー・・","き":"ー・ー・・","く":"・・・ー","け":"ー・ーー","こ":"ーーーー",
"さ":"ー・ー・ー","し":"ーー・ー・","す":"ーーー・ー","せ":"・ーーー・","そ":"ーーー・",
"た":"ー・","ち":"・・ー・","つ":"・ーー・","て":"・ー・ーー","と":"・・ー・・",
"な":"・ー・","に":"ー・ー・","ぬ":"・・・・","ね":"ーー・ー","の":"・・ーー",
"は":"ー・・・","ひ":"ーー・・ー","ふ":"ーー・・","へ":"・","ほ":"ー・・",
"ま":"ー・・ー","み":"・・ー・ー","む":"ー","め":"ー・・・ー","も":"ー・・ー・",
"や":"・ーー","ゆ":"ー・・ーー","よ":"ーー",
"ら":"・・・","り":"ーー・","る":"ー・ーー・","れ":"ーーー","ろ":"・ー・ー",
"わ":"ー・ー","ゐ":"・ー・・ー","ゑ":"・ーー・・","を":"・ーーー","ん":"・ー・ー・",

"゛":"・・",//濁点
"゜":"・・ーー・",//半濁点
"ー":"・ーー・ー",//長音
"、":"・ー・ー・ー"//読点
};


var morseBase = ["","ー・ー・・ーー・・ーー・・・ーー・・ー・ー・ーーーー・・・ーーーー・・・・ー・・ーーー・ー・ー・"];
var wordsBase = ["", "きようはりんこ゛をたへ゛ました"];

const deleteFirst = (text) => {
  return text.replace(/^./, "");
}

const mapString = (str) => 
  str.split("").map((a) => {
    return morsecodeMap[a]
  }).join("");

const judgeMorse = (word, list) => {
  let correctWords = "";
  let newWords;
  if(list[1].startsWith(word)){
    correctWords = list[0] + word;
    newWords = deleteFirst(list[1]);
    return [correctWords,newWords];
  }else{
    return list;//間違えた時の処理１
  }
}

const colorChange = (text, file) => {
            const colors = ["color-white", "color-gray"];
            let newText = "";
            newText = `<span class="${colors[0]}">${text[0]}</span>${text[1]}`;
            document.getElementById(file).innerHTML = newText;
        };

//モールスを日本語に変換
const cnv = () => {
    let morse = words;
    if(morse_list[morse]!==NaN && morse_list[morse]!==undefined){
        word += morse_list[morse];
        wordsBase = judgeMorse(word,wordsBase);
        console.log(wordsBase);
        console.log(morseBase[0]);
        morseBase = [mapString(wordsBase[0]), mapString(wordsBase[1])];
        console.log(morseBase);
        colorChange(wordsBase, "textHurigana");
        colorChange(morseBase, "morseJapanese");
    }/*else{
        textJapanese.innerHTML = `入力が違います`;
    }*/
   word = "";
    words = "";
}

//入力をモールス信号に変換
function mousedown() {
    let start1 = performance.now();
    ddtime = start1;
    clearTimeout(id);
}
function mouseup() {
    let mo;
    let end1 = performance.now();
    let result = end1 - ddtime;
    if(result<=200){
        mo = "・"; //ドット
    }else{
        mo = "ー"; //バー
    }
    morseBase = judgeMorse(mo, morseBase);
    colorChange(morseBase, "morseJapanese");
    words += mo;
    mo = "";
    console.log(words);
    id = setTimeout(cnv, interval);
}