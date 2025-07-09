let ddtime=0;
let blanktime=0;
var id = 1;
let words=[];
var count = function addtwo(){
    words.push(2);
}
function mousedown() {
    let start1 = performance.now();
    ddtime = start1;
    clearTimeout(id);
    console.log(id + "mousedown");
    id = id + 1
}
function mouseup() {
    let end1 = performance.now();
    let result = end1 - ddtime;
    if(result<=200){
        words.push(0);
    }else{
        words.push(1);
    }
    setTimeout(count, "2000");
    rst.innerHTML = `${words}ms`;
    console.log(words);
    console.log(id + "mousoup");
}
