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

class Morse{
    constructor(baseText,baseMorse){
        this.baseText = baseText;
        this.baseMorse = baseMorse;
    }
}


//モールスを日本語に変換
const cnv = () => {
    let morse = words;
    if(morse_list[morse]!==NaN && morse_list[morse]!==undefined){
        word += morse_list[morse];
        textJapanese.innerHTML = `${word}`;
    }else{
        textJapanese.innerHTML = `入力が違います`;
    }
    words = "";
}


var wordsBase = ["","ー・ー・・ーー・・ー・・・・ーー・・ー・ー・ーーーー・・・ーーーー・・・・・・・ーーー・ー・ー・"];

const deleteFirst = (text) => {
  return text.replace(/^./, "");
}

const judgeWords = (word, list) => {
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
const colorChange = (text) => {
            const colors = ["color-white", "color-gray"];
            let newText = "";
            newText = `<span class="${colors[0]}">${text[0]}</span>${text[1]}`;
            document.getElementById("morseJapanese").innerHTML = newText;
        };

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
    wordsBase = judgeWords(mo, wordsBase);
    colorChange(wordsBase);
    mo = "";
    words = wordsBase[0];
    console.log(words);
    id = setTimeout(cnv, interval);
}


/*document.addEventListener("DOMContentLoaded", function() {
            const textElement = document.getElementById("textJapanese");
            const text = textElement.textContent;
            const colors = ["color-red", "color-green", "color-blue", "color-yellow", "color-purple"];
            let newText = "";

            for (let i = 0; i < text.length; i++) {
                const colorClass = colors[i % colors.length];
                newText += `<span class="${colorClass}">${text[i]}</span>`;
            }

            textElement.innerHTML = newText;
        });*/